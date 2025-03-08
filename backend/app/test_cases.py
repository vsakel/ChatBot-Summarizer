import pytest
from endpoints import app  # import flask app
from io import BytesIO
from reportlab.pdfgen import canvas

# This code uses ReportLab to write text to a PDF. 
# This way we generate a test pdf using the BytesIO object that works as in-memory file

@pytest.fixture
def client():
    """Fixture for providing a test client.
       we can use client to simulate HTTP requests.
    """
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
        assert response.status_code == 400
        json_data = response.get_json()
        assert json_data['error'] == 'Invalid file type. Please upload a PDF file.'


## This test is successfully passed when i run it locally
## but when i run it with github actions, i get an error from server
## so it returns response.status_code == 500

# def test_valid_extension(client):
#     """Test a valid PDF file upload"""
#     # with open('backend/app/invoice.pdf', 'rb') as pdf:  # provide a valid PDF file path
#     #     data = {'userfile': (pdf, 'invoice.pdf')}
#     # Simulating a bytes object of a PDF file.
#     pdf_bytes = b'%PDF-1.4 ...'
#     # Wrapping the bytes object with BytesIO class to create a file-like object.
#     pdf_buffer = io.BytesIO(pdf_bytes)
#     data = {"userfile": (pdf_buffer, "invoice.pdf")}
#     response = client.post('/summarize', data=data, content_type='multipart/form-data')
#     assert response.status_code == 200
#     json_data = response.get_json()
#     assert 'summary' in json_data  # check that a summary is returned


def generate_test_pdf():
    pdf_buffer = BytesIO()
    c = canvas.Canvas(pdf_buffer)
    c.drawString(100, 750, "This is a TEST!!!")
    c.showPage()
    c.save()
    pdf_buffer.seek(0)
    return pdf_buffer

def test_valid_extension(client):
    """Test a valid PDF file upload"""
    pdf_buffer = generate_test_pdf()
    data = {"userfile": (pdf_buffer, "invoice.pdf")}
    response = client.post('/summarize', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'summary' in json_data  # check that a summary is returned