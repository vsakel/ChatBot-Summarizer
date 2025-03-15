from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from llm_api import generate_summary
from dotenv import load_dotenv

# This Flask module provides an API for summarizing PDF files using an external 
# function (generate_summary) that integrates an LLM. 
# The module includes error handling for missing files, incorrect formats, 
# and unexpected server errors.

# Status codes for errors:
# 400 status code, informs us for cases where the client sends a bad request (incorrect file type or no file attached).
# 500 status code, informs us for unexpected errors on the server side that the client has no control.

# we enable CORS so frontend can get the response of backend enpoint.
# we enable the HTTP requests when we reach the endpoint from localhost 
# and when we reach from frontend container using the internal DNS name of service == chatbot_ui
# we will make CORS configuration dynamic with a .env file so we can update the allowed origins
# without modifying the code

dotenv_path = "../../.env"
load_dotenv(dotenv_path,override=True)
cors_origin_local = os.getenv('CORS_ORIGIN_LOCAL')
cors_origin_docker = os.getenv('CORS_ORIGIN_DOCKER')

app = Flask(__name__)    

CORS(app, resources={r"/summarize": {"origins": [cors_origin_local, cors_origin_docker]}})
# CORS(app)


# we need to store the file so we can use pymupdf4llm library to for parsing
app.config['UPLOADER_FOLDER'] = 'uploads/'
if not os.path.exists(app.config['UPLOADER_FOLDER']):
    os.makedirs(app.config['UPLOADER_FOLDER'] )

@app.route('/', methods=['GET'])
def test():
    return jsonify({"message": "Backend is running"})

@app.route('/summarize',methods=['POST'])
def summarize():
     # try-except block captures errors that happen during the execution of route
    try:
        # ensure that the file_path variable exists, but it is initially set to None
        # so i dont have problems if an error occurs before file is saved
        file_path = None

        # The file may not properly attach due to a network issue, file corruption, or browser bugs.
        if 'userfile' not in request.files:
            return jsonify({"error": "No file attached."}), 400
        
        file = request.files['userfile']
        file_name = file.filename
        files_allowed = ['pdf']
        file_extension = file_name.split('.')[-1].lower()

        # check for the file extension
        if file_extension not in files_allowed:
            return jsonify({"error": "Invalid file type. Please upload a PDF file."}), 400
            
        file_path = os.path.join(app.config['UPLOADER_FOLDER'] ,file_name)
        file.save(file_path)
        summary = generate_summary(file_path) # call the llm integration function to generate a summary
        return jsonify({"summary": summary})  # Return the summary generated as a JSON response      
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500 
        # we have to return the status code, because jsonify return 200 even if an error happens

    finally:
        if file_path and os.path.exists(file_path):
            os.remove(file_path)

if __name__ == '__main__':
    app.run(debug=True,port=5000)