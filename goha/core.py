import requests

def upload_pdf(file_path, api_key):
    files = [
        ('file', ('file', open(file_path, 'rb'), 'application/octet-stream'))
    ]
    headers = {
        'x-api-key': api_key
    }

    response = requests.post(
        'https://api.chatpdf.com/v1/sources/add-file', headers=headers, files=files)

    if response.status_code == 200:
        return response.json()['sourceId']
    else:
        return None, response.status_code, response.text

# # Example usage:
# file_path = '/path/to/file.pdf'
# api_key = 'sec_xxxxxx'
# source_id, status_code, error_message = upload_pdf(file_path, api_key)

# if source_id is not None:
#     print('Source ID:', source_id)
# else:
#     print('Status:', status_code)
#     print('Error:', error_message)

import requests

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

    response = requests.post(
        'https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['content']
    else:
        return None, response.status_code, response.text

# Example usage:
# source_id = "src_xxxxxx"
# message = "Who wrote the constitution?"
# api_key = 'sec_xxxxxx'
# result = send_message_to_pdf_chat(source_id, message, api_key)

# if result is not None:
#     print('Result:', result)
# else:
#     print('Status:', response.status_code)
#     print('Error:', response.text)
