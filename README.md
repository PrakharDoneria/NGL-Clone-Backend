# NGL Clone Backend

This is the backend for the NGL Clone, built using Flask and connected to a MySQL database. Below are the available API endpoints, along with sample requests and responses.

---

## Endpoints

### 1. **Submit Message**  
- **URL**: `/submit`  
- **Method**: `POST`  
- **Description**: Submits a new anonymous message to the database.

#### Sample Request:
```json
POST /submit
Content-Type: application/json

{
  "message": "Hello, this is a test message",
  "device_type": "Mobile",
  "os": "iOS",
  "browser": "Safari",
  "screen_size": "375x667",
  "city": "New York",
  "region": "NY",
  "isp_name": "ISP Corp",
  "connection_type": "WiFi"
}
```

#### Sample Response:
```json
{
  "success": true,
  "message": "Message stored successfully!"
}
```

---

### 2. **Get All Messages**  
- **URL**: `/messages`  
- **Method**: `GET`  
- **Description**: Retrieves all the messages stored in the database.

#### Sample Request:
```bash
GET /messages
```

#### Sample Response:
```json
{
  "success": true,
  "messages": [
    {
      "id": 1,
      "message": "Hello, this is a test message",
      "ip": "192.168.1.1",
      "device_type": "Mobile",
      "os": "iOS",
      "browser": "Safari",
      "screen_size": "375x667",
      "city": "New York",
      "region": "NY",
      "isp_name": "ISP Corp",
      "connection_type": "WiFi"
    },
    {
      "id": 2,
      "message": "Another test message",
      "ip": "192.168.1.2",
      "device_type": "Desktop",
      "os": "Windows",
      "browser": "Chrome",
      "screen_size": "1366x768",
      "city": "Los Angeles",
      "region": "CA",
      "isp_name": "Another ISP",
      "connection_type": "Ethernet"
    }
  ]
}
```

---

## Error Responses

For both endpoints, if something goes wrong (like missing required fields or server errors), you'll get a response like:

#### Sample Error Response:
```json
{
  "success": false,
  "error": "Invalid input or internal server error"
}
```

---

### Requirements
- Python 3.7+
- Flask
- Flask-Cors
- Flask-SQLAlchemy
- PyMySQL

To install the required dependencies, use:

```bash
pip install -r requirements.txt
```