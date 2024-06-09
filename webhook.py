from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.post(url, json=payload)
    return response

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.json
        message = data.get('message', 'No message found')
        send_telegram_message(message)
        return jsonify({"status": "success", "message": "Alert received"}), 200
    else:
        return jsonify({"error": "Invalid request method"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
