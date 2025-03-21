"""
Python Script to Send SMS using Twilio

Steps to run this script:
1. Save this script as `send_sms.py`
2. Install Twilio SDK using `pip install twilio`
3. Set up a Twilio account and get your Account SID, Auth Token, and Twilio phone number
4. Update the script with your Twilio credentials and recipient phone number
5. Run the script with `python send_sms.py`
"""

from twilio.rest import Client

def send_sms():
    account_sid = "your_account_sid"
    auth_token = "your_auth_token"
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        body="Hello, this is a test SMS from Python!",
        from_="your_twilio_number",
        to="recipient_phone_number"
    )
    
    print("SMS sent successfully! Message SID:", message.sid)

send_sms()
