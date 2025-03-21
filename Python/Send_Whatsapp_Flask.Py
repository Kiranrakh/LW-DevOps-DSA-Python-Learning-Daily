from flask import Flask, request, jsonify
from twilio.rest import Client

app = Flask(__name__)

@app.route('/send_whatsapp', methods=['POST'])
def send_whatsapp_message():
    data = request.json
    account_sid = "your_account_sid"
    auth_token = "your_auth_token"
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        body=data['message'],
        from_="whatsapp:your_twilio_whatsapp_number",
        to=f"whatsapp:{data['recipient_phone']}"
    )
    
    return jsonify({"message": "WhatsApp message sent successfully!", "sid": message.sid})

if __name__ == '__main__':
    # To run this Flask application:
    # 1. Save this script as app.py
    # 2. Install Flask and Twilio using 'pip install flask twilio'
    # 3. Run the script with 'python app.py'
    # 4. Use Postman or Curl to send a POST request to 'http://127.0.0.1:5000/send_whatsapp'
    #    with JSON body: {"recipient_phone": "recipient_number", "message": "your_message"}
    app.run(debug=True)
