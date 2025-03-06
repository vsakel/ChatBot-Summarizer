import pytest
from endpoints import app  # import flask app

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

def test_valid_extension(client):
    """Test a valid PDF file upload"""
    with open('backend/app/invoice.pdf', 'rb') as pdf:  # Provide a valid PDF file path
        data = {'userfile': (pdf, 'invoice.pdf')}
        response = client.post('/summarize', data=data, content_type='multipart/form-data')
        assert response.status_code == 200
        json_data = response.get_json()
        assert 'summary' in json_data  # Check that a summary is returned