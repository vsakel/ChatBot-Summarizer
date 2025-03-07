# ChatBot Summarizer

An AI-powered application that simplifies document processing. 

You can upload your files, and the system will generate clear, concise summaries to help you better understand your documents.

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
2) Move to fronted folder: `cd frontend`
3) Install depedencies: `npm install`

### Running the Application
- Start the development server: `npm run dev`  
 -**Application runs on http://localhost:5173/**

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
  - The generated summary is returned, to frontend, as a JSON response.
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
2) Move to backend folder: `cd backend`
3) Create a virtual environment: `python -m venv virtual_env`
4) Activate a virtual environment: `.\venv\Scripts\activate`
5) Install depedencies: `pip install -r app\requirements.txt`
   

### Running the Application
- Start the development server: `python endpoints.py`
 -**Backend runs on http://localhost:5000/**

## LLM Integration

This section provide details about the integration and usage of an OpenAI' s model, in our backend.

We use OpenAI's GPT-4 model (gpt-4o-mini), which is hosted in OpenAI's cloud servers, to analyze and summarize tax-related uploaded documents.

### Integration Pipeline
We integrate the LLM using the followed pipeline:

1. Document parsing.
   - When a PDF is uploading, it is first **parsed into markdown format**. This structured format prepares the document for processing by the LLM.

2. **Set up the API key**.
   - To use OpenAI's models, we need to have an API key from OpenAI. The API key allow us to send requests and communicate with OpenAI's models.
   - Create a .env file in the backend/app folder and add the API key: `OPENAI_API_KEY=your-api-key`
     
3. Declaring system and user prompts.
   - We declare a system prompt that provide some instructions to guide the model to the desired output.
  
     Our **system prompt**:
   
      ```
      You are an assistant that analyze tax related documents and generate a short summary.
      You should follow these instructions:
      Keep the summary concise, focusing only on the most important details.
      Highlight the points you think most important. 
      If document contains unclear information highlight it, but avoid making assumptions.
      Respond in markdown.
   - Also we declare a user prompt that tells the model to summarize a specific document
  
     Our **user prompt**: `You are looking at a document. The content of this document is as follows. Please provide a short summary.`
   
4. Creating **augmented prompt**.
   - Augmented prompt, combines parsed document text with the user prompt.
     
5. Sending the augmented prompt to GPT-4 model for processing.
   - We **sent the context to API endpoint** of model, using the openai.chat.completions.create endpoint.
     
6. **Extracting** the generated **summary** from the API's response.


## Docker Setup

This project uses **Docker Compose** tool to build a **multi-container application** with frontend and backend services as separate containers, that communicate within a Docker network.

Follow these steps to containirize frontend and backend services.

### Prerequisites
You should have installed:
- Docker Desktop

### Build and run Docker containers
To build and run the multi-container architecture, we will run the following command, in the root project directory.

`docker-compose up -d`

**Note**: We run the containers in detached mode (-d flag), so our containers run in the background.
 

### Access the services Locally
Once the containers are up and running, we can access the services at the following URLs:
- Frontend: http://localhost:5173
- Backend: http://localhost:5000

### Stopping the containers:
To stop the containers, we run: `docker-compose down`

  





