import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
CORS(app)

DB_URI = os.getenv("DATABASE_URL")

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(500), nullable=False)
    ip = db.Column(db.String(50), nullable=False)
    device_type = db.Column(db.String(50))
    os = db.Column(db.String(50))
    browser = db.Column(db.String(50))
    screen_size = db.Column(db.String(50))
    city = db.Column(db.String(50))
    region = db.Column(db.String(50))
    isp_name = db.Column(db.String(50))
    connection_type = db.Column(db.String(50))

@app.before_request
def before_request():
    try:
        db.engine.connect()
        print("Successfully connected to the database!")
    except Exception as e:
        print(f"Error connecting to the database: {str(e)}")

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

        message_data = Message(
            message=anonymous_message,
            ip=ip,
            device_type=device_type,
            os=os,
            browser=browser,
            screen_size=screen_size,
            city=city,
            region=region,
            isp_name=isp_name,
            connection_type=connection_type
        )

        db.session.add(message_data)
        db.session.commit()

        return jsonify({"success": True, "message": "Message stored successfully!"}), 200

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/messages', methods=['GET'])
def get_messages():
    try:
        messages = Message.query.all()
        messages_list = []

        for message in messages:
            messages_list.append({
                "id": message.id,
                "message": message.message,
                "ip": message.ip,
                "device_type": message.device_type,
                "os": message.os,
                "browser": message.browser,
                "screen_size": message.screen_size,
                "city": message.city,
                "region": message.region,
                "isp_name": message.isp_name,
                "connection_type": message.connection_type
            })

        return jsonify({"success": True, "messages": messages_list}), 200

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
