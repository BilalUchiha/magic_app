from flask import Flask, request, jsonify
from flask_cors import CORS

import requests
import base64

app = Flask(__name__)
CORS(app)

# Replace with your Telegram bot token and the list of chat IDs
BOT_TOKEN = '6571310778:AAH_Fa_DpeHG9UkZ2WKq1FKmU0emogyQZd8'
CHAT_IDS = ['754199821', '6571310778']  # Add multiple chat IDs here

@app.route('/', methods=['POST'])
def send_to_telegram():
    data = request.get_json()
    image_data_url = data.get('image')
    
    # Extract the image data from the Data URL
    image_data = image_data_url.split(',')[1]
    image_binary = base64.b64decode(image_data)
    
    # Send the image to each chat ID
    responses = []
    for chat_id in CHAT_IDS:
        files = {'photo': image_binary}
        response = requests.post(
            f'https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto',
            data={'chat_id': chat_id},
            files=files
        )
        
        if response.status_code == 200:
            responses.append({'chat_id': chat_id, 'success': True, 'data': response.json()})
        else:
            responses.append({'chat_id': chat_id, 'success': False, 'error': response.text})
    
    return jsonify(responses)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
