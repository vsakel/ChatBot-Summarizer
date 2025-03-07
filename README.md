# ChatBot Summarizer

An AI-powered application that simplifies document processing. Upload your files, and the system will generate clear, concise summaries to help you better understand your documents.

## Frontend Setup
This frontend is built with **React.js** and **Vite**.

It consists of key components such as:
- **main.jsx**: The entry point of our React application. It is responsible for rendering the top-level component, App, into the DOM.
- **App.jsx**: The core component of the application that acts as a container for the two main pages, managing the routing between them.
- **HomePage.jsx**: Displays the Home page, which is the root page of the application.
- **UploadPage.jsx**: Displays the Upload page, where users can upload their files. It handles the file upload process and displays the generated summary.
- **NavigationBar.jsx**: The navigation bar, which allows users to move between pages (Home and Upload).
- **Summary.jsx**: Renders the generated summary in Markdown format.


Follow these steps to set up and run the project locally.

### Prerequisites
You should have the following installed:
- Node.js
- Git (to clone repository)

### Installation
1) Clone the repository
2) `cd frontend`
3) Install depedencies: `npm install`

### Running the Application
- start the development server: `npm run dev`  

  **Application runs on http://localhost:5173/**

## API Documentation

This section provides details about the API endpoints used in the ChatBot Summarizer backend, built with **Flask**.

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
- We parse the PDF into Markdown format, because it preserves the hierarchical document's structure, which enhances the model's ability to understand the content.

Follow these steps to set up and run the project locally.

### Prerequisites
You should have the following installed:
- Python 3.10
- Git (to clone repository)

### Installation
1) Clone the repository (if you haven't cloned it)
2) `cd backend`
3) create a virtual environment: `python -m venv venv`
4) activate a virtual environment: `.\venv\Scripts\activate`
5) install depedencies: `pip install -r app\requirements.txt`
   

### Running the Application
- start the development server: `python endpoints.py`

  **Backend runs on http://localhost:5000/**

## LLM Integration

We use OpenAI's GPT-4 model, which is hosted in OpenAI's cloud servers, and integrate this into our backend. 

We use this model for analyzing and summarizing the content of tax-related uploaded documents.

To integrate the model we develop this pipeline:
1. Document parsing.
   - When a PDF is uploading, it is first parsed into markdown format and the document is prepared for processing by the AI model.
3. System and User prompts.
   - A system prompt that guide the model to the desire output.
   - A user prompt that gives the content that user wants to summarize
4. The parsed document text is combined with the user prompt to create an "augmented prompt" that is sent to the OpenAI API, which is hosted on OpenAI’s cloud servers. The request is made to the GPT-4 model.
5. summary generation






