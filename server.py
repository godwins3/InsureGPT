from flask import Flask, render_template, request, Response
import requests

app = Flask(__name__)

# Function to upload PDF to the chat PDF API
def upload_pdf(file_path, api_key):
    files = [('file', ('file', open(file_path, 'rb'), 'application/octet-stream'))]
    headers = {'x-api-key': api_key}
    response = requests.post('https://api.chatpdf.com/v1/sources/add-file', headers=headers, files=files)
    if response.status_code == 200:
        return response.json()['sourceId']
    else:
        return None

# Function to send message to PDF chat
def send_message_to_pdf_chat(source_id, message, api_key):
    headers = {
        'x-api-key': api_key,
        "Content-Type": "application/json",
    }
    data = {
        'sourceId': source_id,
        'messages': [
            {
                'role': "user",
                'content': message,
            }
        ]
    }
    response = requests.post('https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['content']
    else:
        return None

# Route to render the upload form
@app.route('/')
def upload_form():
    return render_template('upload_form.html')

# Route to handle the file upload and question submission
@app.route('/chatbot', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        msg_received = request.get_json()
        # Check if the POST request has a file part
        # if 'file' not in request.files:
        #     return 'No file part'
        
        # file = request.files['file']

        # If the user does not select a file, the browser submits an empty file without a filename
        # if file.filename == '':
        #     return 'No selected file'

        # Save the uploaded PDF file
        pdf_path = 'uploads/faqs.pdf'
        # file.save(pdf_path)

        # Upload PDF to chat PDF API
        api_key = 'sec_krPXTZLBgir0WGcHMq9L1hTriluOEHJq'
        source_id = upload_pdf(pdf_path, api_key)

        if source_id is None:
            return 'Failed to upload PDF'

        # Get user's question from the form
        question = msg_received['question']

        # Send message to PDF chat
        result = send_message_to_pdf_chat(source_id, question, api_key)

        
        if result is not None:
            res = {
                "answer": result,
                "statusCode": 200
            }
            # return render_template('result.html', question=question, answer=result)
            return res
        else:
            res = {
                "message": "Error sending message to pdf",
                "statusCode": 401
            }
            return res

# @app.route('/incoming-messages', methods=['POST'])
# def incoming_messages():
#     data = request.get_json(force=True)
#     print(f'Incoming message...\n ${data}')
#     # Upload PDF to chat PDF API
#     # Save the uploaded PDF file
#     pdf_path = 'uploads/' + file.filename
#     file.save(pdf_path)
#     api_key = 'sec_krPXTZLBgir0WGcHMq9L1hTriluOEHJq'
#     source_id = upload_pdf(pdf_path, api_key)

#     if source_id is None:
#         return 'Failed to upload PDF'

#     # Get user's question from the form
#     question = request.form['question']

#     # Send message to PDF chat
#     result = send_message_to_pdf_chat(source_id, question, api_key)
    
#     res ={
#         "result": result,

#     }

#     return Response(status=200)

@app.route('/delivery-reports', methods=['POST'])
def delivery_reports():
   data = request.get_json(force=True)
   print(f'Delivery report response...\n ${data}')
   return Response(status=200) 

if __name__ == '__main__':
    app.run(debug=True)