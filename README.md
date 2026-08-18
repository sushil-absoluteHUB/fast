# FastAPI Testing - Basic Knowledge

A beginner-friendly FastAPI project demonstrating basic API development and testing concepts.

## 📋 Project Overview

This project showcases a simple FastAPI application with basic endpoints and includes testing examples. It's designed to help you understand:
- Creating REST API endpoints with FastAPI
- Testing API endpoints using pytest and TestClient
- Basic CRUD operations concepts
- HTTP methods and status codes

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- pip (Python package manager)
- Virtual Environment (recommended)

### Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd fast
   ```

2. **Create and activate a virtual environment:**
   
   **Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install fastapi uvicorn pytest httpx
   ```

### Running the Server

Start the development server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

Access the interactive API documentation:
- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

### Running Tests

Execute the test suite:
```bash
pytest test_main.py -v
```

Run tests with coverage report:
```bash
pip install pytest-cov
pytest test_main.py --cov=. -v
```

## 📁 Project Structure

```
fast/
├── main.py              # FastAPI application with endpoint definitions
├── test_main.py         # Unit tests for API endpoints
└── README.md            # Project documentation
```

## 🔌 API Endpoints

### 1. Home Endpoint
- **URL:** `/`
- **Method:** `GET`
- **Description:** Returns a welcome message
- **Response Example:**
  ```json
  {
    "message": "welcome to sushil API venv"
  }
  ```

### 2. Contact Endpoint
- **URL:** `/contact`
- **Method:** `GET`
- **Description:** Returns a list of contacts
- **Response Example:**
  ```json
  {
    "hello": ["sushil", "viveka"]
  }
  ```

## 🧪 Testing Basics

### Understanding FastAPI Testing

FastAPI uses `TestClient` from `httpx` for testing. Here's what you need to know:

**Basic Test Structure:**
```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
```

### Common Assertions

```python
# Check status code
assert response.status_code == 200

# Check response data
data = response.json()
assert data["message"] == "welcome to sushil API venv"

# Check response contains key
assert "hello" in response.json()
```

### Test File Template

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_contact():
    response = client.get("/contact")
    assert response.status_code == 200
    assert "hello" in response.json()
```

## 📚 Key Concepts

### HTTP Methods
- **GET:** Retrieve data
- **POST:** Create new data
- **PUT:** Update existing data
- **DELETE:** Remove data

### Status Codes
- **200:** OK - Request successful
- **201:** Created - Resource created successfully
- **400:** Bad Request - Invalid input
- **404:** Not Found - Resource not found
- **500:** Internal Server Error

### Testing Best Practices
1. ✅ Test both success and failure cases
2. ✅ Use descriptive test names
3. ✅ Keep tests independent
4. ✅ Test with realistic data
5. ✅ Verify status codes and response structure

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| **fastapi** | Web framework for building APIs |
| **uvicorn** | ASGI server for running FastAPI |
| **httpx** | HTTP client (includes TestClient) |
| **pytest** | Testing framework |
| **pytest-cov** | Code coverage plugin (optional) |

Install all at once:
```bash
pip install fastapi uvicorn pytest httpx pytest-cov
```

## 🔍 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'fastapi'` | Run `pip install fastapi` |
| `Address already in use` | Server already running on port 8000, use `--port 8001` |
| `Tests not found` | Ensure test file starts with `test_` prefix |
| `ConnectionRefusedError in tests` | Ensure you're using TestClient, not actual HTTP requests |

## 🎯 Next Steps

1. **Add more endpoints** - Try adding POST, PUT, DELETE methods
2. **Add request validation** - Use Pydantic models for input validation
3. **Database integration** - Connect to a database (SQLite, PostgreSQL)
4. **Authentication** - Implement user authentication
5. **Error handling** - Add proper error responses and exception handling

## 📖 Useful Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [pytest Documentation](https://docs.pytest.org/)
- [HTTP Status Codes](https://httpwg.org/specs/rfc7231.html#status.codes)
- [REST API Best Practices](https://restfulapi.net/)

## 💡 Example: Creating a New Endpoint

```python
# In main.py
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}

# In test_main.py
def test_get_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["item_id"] == 1
```

## 🤝 Contributing

Feel free to extend this project with more endpoints, tests, and features to deepen your FastAPI knowledge!

## 📝 License

This is a learning project.

---

**Created:** 2024  
**Version:** 1.0  
**Author:** Sushil Kumar
