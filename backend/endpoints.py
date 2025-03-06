from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from parse import parse_file
from llm_api import generate_summary

# during develompent of backend api endpoint
# i had faced 2 problems
# 1) CORS problem
# 2) to use pymupdf4llm and parse the file as markdown i had to save the file in server so i can parse it
# because library needs the filepath

# That's way we need to store it 
# If the file needs to be processed in some way 
# (e.g., for summarization, text extraction, or any analysis), 
# you may temporarily store it to access it later during processing.
# For example, if you're summarizing a document, you might need 
# to store it on the server temporarily to read and process its contents.

# why we use 400 and 500 statuts code in errors
# In your route, you correctly use:

# 400 for cases where the client sends a bad request (incorrect file type or no file attached).
# 500 for unexpected errors on the server side that the client has no control over 
# (e.g., issues with file saving or parsing).

app = Flask(__name__)
# enable CORS so frontend can get the response of backend enpoint
CORS(app, resources={r"/summarize": {"origins": "http://localhost:5173"}})
# CORS(app)


# we need to store the file so we can use pymupdf4llm library to parse pdfs
upload_folder = 'uploads/'
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)

@app.route('/summarize',methods=['POST'])
def summarize():
    # check it because we can have
    # The file does not properly attach due to a network issue, file corruption, or browser bugs.
    try:
        if 'userfile' not in request.files:
            return jsonify({"error": "No file attached."}), 400
        file = request.files['userfile']
        file_name = file.filename
        files_allowed = ['pdf']
        file_extension = file_name.split('.')[-1].lower()
        if file_extension not in files_allowed:
            return jsonify({"error": "Invalid file type. Please upload a PDF file."}), 400
        file_path = os.path.join(upload_folder,file_name)
        file.save(file_path)
        # call the llm to generate a summary
        summary = generate_summary(file_path)
        # Return the summary generated as a JSON response
        return jsonify({"summary": summary})       
    # try-except block captures errors that happen during the execution of route
    # for example if there is no folder to save the file we process
    # an error occurs 
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500 
        # we have to return the status 
        # code, because jsonify return 200 even if an error happens
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


if __name__ == '__main__':
    app.run(debug=True,port=5000)