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

The backend runs on http://localhost:5000/

### Endpoints implementation:
- Test Endpoint (GET /) – Checks if the backend is running
- Summarization Endpoint (POST /summarize) – Uploads a **PDF document**, processes it, and returns the generated summary.
- 
  **Summarization Endpoint Logic**:
  - User uploads a PDF file.
  - The document is stored temporarily on the backend server, for processing.
  - The document is processed and parsed, using pymupdf4llm library.
  - The parsed document sent to OpenAI's LLM for summarization.
  - The generated summary is returned as a JSON response.
  - The temporary file is deleted after processing is complete.





