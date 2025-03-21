"""
Flask Application to Send SMS

Steps to run this script:
1. Save this script as `send_sms.py`
2. Install Flask and Twilio using `pip install flask twilio`
3. Set up a Twilio account and get your Account SID, Auth Token, and Twilio phone number
4. Run the script with `python send_sms.py`
5. Use Postman or Curl to send a POST request to `http://127.0.0.1:5000/send_sms`
   with JSON body:
   {
       "recipient_phone": "recipient_number",
       "message": "your_message"
   }
"""

from flask import Flask, request, jsonify
from twilio.rest import Client

app = Flask(__name__)

@app.route('/send_sms', methods=['POST'])
def send_sms():
    data = request.json
    account_sid = "your_account_sid"
    auth_token = "your_auth_token"
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        body=data['message'],
        from_="your_twilio_number",
        to=data['recipient_phone']
    )
    
    return jsonify({"message": "SMS sent successfully!", "sid": message.sid})

if __name__ == '__main__':
    app.run(debug=True)
