# ChatBot Summarizer

An AI-powered application that simplifies document processing. Upload your files, and the system will generate clear, concise summaries to help you better understand your documents.

## Frontend Setup
This frontend is built with **React.js** and **Vite**.

Follow these steps to set up and run the project locally.

### Prerequisites
You should have the following installed:
- Node.js
- Git (to clone repository)

### Installation
1) Clone the repository
2) cd frontend
3) npm install - Install depedencies

### Running the Application
- npm run dev - start the development server 

  Open http://localhost:5173/ in your browser to access the application.

## API Documentation

This section provides details about the API endpoints used in the ChatBot Summarizer backend, built with **Flask**.

Follow these steps to set up and run the project locally.

### Prerequisites
You should have the following installed:
- Python

### Installation
1) cd backend
2) create a virtual environment - python -m venv venv
3) activate a virtual environment - .\venv\Scripts\activate
4) install depedencies - pip install -r requirements.txt
   

### Running the Application
- start the development server - python endpoints.py

  Backend runs http://localhost:5000/ 

### Endpoints implementation:
- Test Endpoint (GET /) – Checks if the backend is running
- Summarization Endpoint (POST /summarize) – Uploads a **PDF document**, processes it, and returns the generated summary.

  **Summarization Endpoint Logic**:
  - User uploads a PDF file.
  - The document is stored temporarily on the backend server, for processing.
  - The document is processed and parsed, using pymupdf4llm library.
  - The parsed document sent to OpenAI's LLM for summarization.
  - The generated summary is returned as a JSON response.
  - The temporary file is deleted after processing is complete.
 
### Additional Details
- Cross Origin Resource Sharing (CORS), is enabled to allow frontend receive responses from backend enpdpoint.
- Uploaded files are temporarily stored in the backend, because the pymupdf4llm library requires a file path to process the PDF.
- We parse the PDF into Markdown format because it preserves the hierarchical document's structure, which enhances the model's ability to understand the content.






