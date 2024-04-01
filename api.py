from flask import Flask, request, jsonify,render_template
from Extractor import extract_data_from_pdf
import base64

app = Flask(__name__)

def pdf_extractor(pdf_data):

    decoded_data = base64.b64decode(pdf_data)
    return {'text': decoded_data.decode('utf-8')}
@app.route('/')
def init():
    return render_template("index.html")

@app.route('/api/conneqtion/upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.json:
        return jsonify({'error': 'No file part in JSON payload'})
    # Decode the base64 encoded PDF data
    pdf_data = base64.b64decode(request.json['file'])
    # Call the extraction function
    extracted_data = extract_data_from_pdf(pdf_data)
    
    return extracted_data

    return jsonify({'error': 'Invalid file type'})

if __name__ == '__main__':
    app.run(debug=True)
