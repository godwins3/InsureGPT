from flask import Flask, request, Response, render_template
from goha.core import extract_text_from_pdf

app = Flask(__name__)

@app.route('/')
def upload_form():
    return render_template('upload_form.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the POST request has a file part
        if 'file' not in request.files:
            return 'No file part'
        
        file = request.files['file']

        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            return 'No selected file'

        # Save the uploaded PDF file
        pdf_path = 'tmp/' + file.filename
        file.save(pdf_path)

        # Extract text from the PDF file
        pdf_text = extract_text_from_pdf(pdf_path)

        # Get user's question from the form
        question = request.form['question']

        # Answer the user's question based on the PDF content (simple example)
        answer = "Placeholder answer"
        # You can implement a more sophisticated logic here to analyze the PDF content and generate appropriate answers

        return render_template('result.html', question=question, answer=answer)

@app.route('/incoming-messages', methods=['POST'])
def incoming_messages():
   data = request.get_json(force=True)
   print(f'Incoming message...\n ${data}')
   return Response(status=200)

@app.route('/delivery-reports', methods=['POST'])
def delivery_reports():
   data = request.get_json(force=True)
   print(f'Delivery report response...\n ${data}')
   return Response(status=200) 

if __name__ == '__main__':
    app.run(debug=True)