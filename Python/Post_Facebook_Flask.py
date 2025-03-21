from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/post_facebook', methods=['POST'])
def post_on_facebook():
    data = request.json
    access_token = "your_access_token"
    
    url = f"https://graph.facebook.com/v12.0/me/feed?message={data['message']}&access_token={access_token}"
    response = requests.post(url)
    
    if response.status_code == 200:
        return jsonify({"message": "Post published successfully!"})
    else:
        return jsonify({"error": response.text})

if __name__ == '__main__':
    # To run this Flask application:
    # 1. Save this script as app.py
    # 2. Install Flask and Requests using 'pip install flask requests'
    # 3. Run the script with 'python app.py'
    # 4. Use Postman or Curl to send a POST request to 'http://127.0.0.1:5000/post_facebook'
    #    with JSON body: {"message": "your_facebook_post_message"}
    app.run(debug=True)
