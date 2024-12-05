### **Sample Usage**

#### **1. Submit Anonymous Message**
**Endpoint**: `/submit`  
**Method**: `POST`  
**Content-Type**: `application/json`

**Request Body:**
```json
{
    "message": "test message",
    "device_type": "Mobile",
    "os": "Android 12",
    "browser": "Chrome 95",
    "screen_size": "1080x2400",
    "city": "Mumbai",
    "region": "Maharashtra",
    "isp_name": "Jio",
    "connection_type": "WiFi"
}
```

**Sample Response (Success):**
```json
{
    "success": true,
    "message": "Message stored and email sent successfully!"
}
```

**Sample Response (Error):**
```json
{
    "success": false,
    "error": "Failed to send email"
}
```

---

#### **2. View Stored Messages (for testing purposes)**
**Endpoint**: `/messages`  
**Method**: `GET`  

**Sample Response:**
```json
[
    {
        "message": "test message",
        "ip": "192.168.1.1",
        "device_type": "Mobile",
        "os": "Android 12",
        "browser": "Chrome 95",
        "screen_size": "1080x2400",
        "city": "Mumbai",
        "region": "Maharashtra",
        "isp_name": "Jio",
        "connection_type": "WiFi"
    }
]