import pytest
from endpoints import app  # import flask app
from reportlab.pdfgen import canvas 
from io import BytesIO

# BytesIO, it is used to work with binary data as if it were a file.
# ReportLab is another powerful library for creating PDFs from scratch. 
# It is best used when you need to generate PDFs dynamically

@pytest.fixture
def client():
    """Fixture for providing a test client.
       we can use client to simulate HTTP requests."""
    with app.test_client() as client:
        yield client

def test_api_start(client):
    """Test if the api starts."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Backend is running"}

def test_no_file(client):
    """Test no file reach the server due to network issue, file corruption, or browser bugs"""
    response = client.post('/summarize', data={})  # No file attached
    assert response.json == {"error": "No file attached."},400


def test_invalid_extension(client):
    """Test an invalid file type (not PDF) upload"""
    with open('backend/app/summary.txt', 'rb') as txt:  
        data = {"userfile": (txt, "summary.txt")}
        response = client.post('/summarize', data=data, content_type='multipart/form-data')
        assert response.json == {"error": "Invalid file type. Please upload a PDF file."},400



# This test uses a real PDF file that is stored on disk. It uploads this actual PDF file to the server and checks if the server processes it correctly.
def test_valid_extension(client):
    """Test a valid PDF file upload"""
    with open('backend/app/invoice.pdf', 'rb') as pdf:  # provide a valid PDF file path
        data = {'userfile': (pdf, 'invoice.pdf')}
        response = client.post('/summarize', data=data, content_type='multipart/form-data')
        assert response.status_code == 200
        json_data = response.get_json()
        assert 'summary' in json_data  # check that a summary is returned


# def generate_test_pdf():
#     pdf_buffer = BytesIO() # This creates an in-memory byte stream
#     c = canvas.Canvas(pdf_buffer) # This initializes a ReportLab Canvas that will write PDF content directly to the pdf_buffer
#     c.drawString(100, 750, "This is a TEST!!!")
#     c.showPage()
#     c.save()
#     pdf_buffer.seek(0)
#     return pdf_buffer


# # This test generates a PDF from scratch using the ReportLab library and stores 
# # it in memory (as byte stream with BytesIO). The in-memory PDF is then sent to the server for processing.
# def test_extension(client):
#     """Test a valid PDF file upload"""
#     pdf_buffer = generate_test_pdf()
#     data = {"userfile": (pdf_buffer, "test.pdf")}
#     response = client.post('/summarize', data=data, content_type='multipart/form-data')
#     assert response.status_code == 200
#     json_data = response.get_json()
#     assert 'summary' in json_data  # check that a summary is returned