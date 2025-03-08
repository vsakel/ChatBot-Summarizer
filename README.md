# ChatBot Summarizer

An AI-powered application that simplifies PDF document processing. 

You can upload your PDF files, and the system will generate clear, concise summaries to help you better understand your documents.

## Frontend Setup
This frontend is built with **React.js** and **Vite**.

The key components are:
- **main.jsx**: The entry point of our React application. It is responsible for rendering the top-level component, App, into the DOM.
- **App.jsx**: The core component of the application that acts as a container for the two main pages, managing the routing between them.
- **HomePage.jsx**: Displays the Home page, which is the root page of application.
- **UploadPage.jsx**: Displays the Upload page, where users can upload their files. It handles the file upload process and displays the generated summary.
- **NavigationBar.jsx**: The navigation bar, which allows users to move between pages (Home and Upload).
- **Summary.jsx**: Renders the generated summary in Markdown format.


Follow these steps to set up and run the project locally.

### Prerequisites
You should have the following installed:
- Node.js
- Git (to clone repository)

### Installation
1) Clone the repository: `git clone https://github.com/vsakel/ChatBot-Summarizer.git`
2) Move to fronted folder: `cd frontend`
3) Install depedencies: `npm install`

### Running the Application
- Start the development server: `npm run dev`  
 - **Application runs on http://localhost:5173/**

## API Documentation

This section provides details about the API endpoints used in the ChatBot Summarizer backend, built with **Flask**.

### Endpoints implementation:
- **Test Endpoint** (GET /)
  - Accesible at http://localhost:5000/
  - The endpoint checks if the backend is running and respond to a GET request.
   
- **Summarization Endpoint** (POST /summarize)
  - Accepts POST requests at http://localhost:5000/summarize
  - The endpoint allow clients to send a POST request (upload a PDF), and the endpoint will process it and return the generated summary.

### Summarization Endpoint Functionality
1. The user uploads a PDF file.
2. The document is temporarily stored on the backend server, for processing.
3. It is processed and parsed, using pymupdf4llm library.
4. The parsed document sent to OpenAI's LLM for summarization.
5. The generated summary is returned, to frontend, as a JSON response.
6. The temporary file is deleted after processing is complete.
7. Endpoint efficiently handles errors, including:
   - Missing file (No file attached).
   - Invalid file type (only PDF files allowed).
   - Unexpected server error.
 
### Additional Details
- Cross Origin Resource Sharing (CORS) is enabled to allow frontend to receive responses from backend enpdpoint.
- Pymupdf4llm is a popular library for parsing PDF files and enabling efficient document processing with LLMs.
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
 - Move to app folder: `cd app`
 - run flask app script, to start the development server: `python endpoints.py`
 - **Backend runs on http://localhost:5000/**

## LLM Integration

This section provide details about the integration and usage of an OpenAI' s model, in our backend.

We use OpenAI's GPT-4 model (specifically GPT-4o mini), which is hosted on OpenAI's cloud servers, to analyze and summarize uploaded tax-related documents.

### LLM Model

We use **GPT-4o mini**, which is designed to balance performance with cost efficiency. It provides powerful AI solutions at a lower price point than the GPT-4o model.


### Integration Pipeline
We integrate the LLM using the followed pipeline:

1. Document parsing.
   - When a PDF is uploading, it is first **parsed into markdown format**. This structured format prepares the document for processing by the LLM.

2. **Set up the API key**.
   - To use OpenAI's models, we need to have an API key from OpenAI. The API key allow us to send requests and communicate with OpenAI's models.
   - Create a .env file in the backend/app folder and add the API key: `OPENAI_API_KEY=your-api-key`
     
3. Declaring system and user prompts.
   - We declare a system prompt that provide some instructions to guide the model to the desired output.
  
   - Our **system prompt**:
   
      ```
      You are an assistant that analyze tax related documents and generate a short summary.
      You should follow these instructions:
      Keep the summary concise, focusing only on the most important details.
      Highlight the points you think most important. 
      If document contains unclear information highlight it, but avoid making assumptions.
      Respond in markdown.
   - Also we declare a user prompt that tells the model to summarize a specific document
  
   - Our **user prompt**: `You are looking at a document. The content of this document is as follows. Please provide a short summary.`
   
4. Creating **augmented prompt**.
   - Augmented prompt, combines parsed document text with the user prompt.
     
5. Sending the augmented prompt to GPT-4 model for processing.
   - We **sent the context to API endpoint** of model, using the openai.chat.completions.create endpoint.
     
6. **Extracting** the generated **summary** from the API's response.


## Docker Setup

This project uses **Docker Compose** tool to build a **multi-container application** with frontend and backend services as separate containers, that communicate within a Docker network.

Follow these steps to containirize frontend and backend services.

### Port Mapping
In the **docker-compose.yml**, the **ports** of services are **mapped from containers to host machine**.

To access frontend container from host machine , we modify **vite.config.js** as above:

```
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    watch: {
      usePolling: true,
    },
    host: true, // without this we cant reach the container from the outside world
    strictPort: true,
    port: 5173, 
  }
});
```

To access backend container, we need to include `--host=0.0.0.0` when running Flask (`flask run --host=0.0.0.0 `).

So it listen on any other network the container is connected to. 

### Prerequisites
You should have installed:
- Docker Desktop.

### Build and run Docker containers
To build and run the multi-container architecture, we will run the following command, in the root project directory.

`docker-compose up -d`

**Notes**: 
- Docker Desktop should run in background.
- We run the containers in detached mode (-d flag), so our containers run in the background.
 

### Access the services Locally
Once the containers are up and running, we can access the services at the following URLs:
- Frontend: http://localhost:5173
- Backend: http://localhost:5000

### Stop the containers
To stop the containers, we run: `docker-compose down`.

## Continuous Integration (CI) Setup

This project uses a CI pipeline, set up with **GitHub Actions** to automate the **testing of the backend** service every time **code is pushed** to the repository.

### CI Pipeline Explained

Explaination of file `.github/workflows/ci.yml`.

- Triggered on every push to the main branch.
- Defines a job called test-backend, which is responsible for testing the backend service.
  - This job is run on an ubuntu-latest virtual environment.
- Uses the latest version of the code from the repository using `actions/checkout@v3`.
- Installs Python 3.10 environment using `actions/setup-python@v4`.
- Installs the required dependencies listed in `backend/app/requirements.txt`.
- Creates a dynamically .env in CI workflow to store the OpenAI API key.
  - Uses **Github Secrets** to **store sensitive information**, that should not be exposed.
  - The OPENAI_API_KEY secret is retrieved from GitHub Secrets and written to a .env file located in the `backend/app` folder.
- Runs the tests located in the `backend/app` folder.
  - Uses **pytest** library to run the defined test cases, ensuring that the backend works as expected.



### Pytest Fixtures

Pytest fixtures are functions that provide a fixed baseline for tests. They allow for reusability, by sharing common set up across multiple tests.
Test functions can use them to perform actions.

We implemented a **client fixture** that simulate HTTP requests to the Flask backend. 
It allows us to send requests to the backend without actually running a server.


### Test Cases

The following Test Cases were developed, to ensure that the backend handles file uploads and returning proper responses.
These tests use the **pytest** library and its **fixtures** to simulate HTTP requests to the Flask backend.


1. **test_api_start**
- This test ensures that the API is running by sending a GET request to the root endpoint (/).
- The expected response should have a status code of 200 and `{"message": "Backend is running"}`.
2. **test_no_file**
- This test checks the condition where no file reaching the server.
- It sending an empty POST request to the /summarize endpoint of backend.
- The expected response should have a 400 status code and return the message `{"error": "No file attached."}`.
3. **test_invalid_extension**
- This test ensures that an invalid file (.txt file) is not processed by the server.
- It sends a POST request to /summarize with a .txt file attached.
- The expected response should have a 400 status code and return the message  `{"error":"Invalid file type. Please upload a PDF file."}`

4 and 5. **test_extension** and **test_valid_extension**
- These tests check that a valid PDF file is uploaded and processed correctly.
- Both tests send the PDF file to the /summarize endpoint and expect the server to return summary as response.


### Difference between 4 and 5 test cases

- **test_extension**: This test generates a PDF from scratch using the ReportLab library and stores it in memory (as byte stream with BytesIO). The in-memory PDF is then sent to the server for processing.

- **test_valid_extension**: This test uses a real PDF file that is stored on disk. It uploads this actual PDF file to the server and checks if the server processes it correctly.






