

# 🛡️ FastAPI JWT Authentication API

A simple REST API built with **FastAPI**, supporting:

✅ User registration
✅ Login with JWT authentication
✅ Protected routes
✅ Secure password hashing (bcrypt)
✅ SQLite database (can upgrade to PostgreSQL/MySQL)

---

## 📂 Project Structure

```
fastapi_jwt_auth/
├── main.py             # Main FastAPI app
├── models.py           # SQLAlchemy models (User)
├── schemas.py          # Pydantic schemas
├── auth.py             # JWT token generation/validation
├── utils.py            # Password hashing utilities
├── database.py         # DB connection & session
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
```

---

## 🚀 Getting Started

### 1️⃣ Clone the repo

```bash
git clone https://github.com/kabirhiking/FASTAPI_PRG.git
cd AUTH
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
uvicorn main:app --reload
```

---

## 📬 API Endpoints

### 🔐 Auth Routes

| Method | Endpoint    | Description             |
| ------ | ----------- | ----------------------- |
| POST   | `/register` | Register a new user     |
| POST   | `/login`    | Login and get JWT token |

### 🛡️ Protected Route

| Method | Endpoint | Description             |
| ------ | -------- | ----------------------- |
| GET    | `/me`    | Get logged-in user info |

---

## 📖 API Usage

### 🔑 Register User

```bash
POST /register
Content-Type: application/json

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "supersecret"
}
```

### 🔑 Login

```bash
POST /login
Content-Type: application/x-www-form-urlencoded

username=john_doe&password=supersecret
```

Response:

```json
{
  "access_token": "JWT_TOKEN_HERE",
  "token_type": "bearer"
}
```

### 📦 Access Protected Route

Include `Authorization: Bearer JWT_TOKEN_HERE` header.

```bash
GET /me
Authorization: Bearer JWT_TOKEN_HERE
```

---

## 🔧 Technologies Used

* [FastAPI](https://fastapi.tiangolo.com/) 🏃‍♂️ - High performance Python web framework
* [SQLAlchemy](https://www.sqlalchemy.org/) 🗄️ - ORM for database access
* [Pydantic](https://pydantic-docs.helpmanual.io/) 📦 - Data validation
* [Python-Jose](https://python-jose.readthedocs.io/) 🔑 - JWT handling
* [Passlib](https://passlib.readthedocs.io/) 🔒 - Password hashing
* [Uvicorn](https://www.uvicorn.org/) ⚡ - ASGI server

---

## 📌 Features

* Secure password storage using bcrypt
* JWT-based stateless authentication
* Simple SQLite database (easy to switch to PostgreSQL/MySQL)
* Interactive API docs at `/docs` (Swagger UI)

---

## 📖 API Docs

FastAPI auto-generates docs:

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📦 Future Improvements

* Refresh Tokens support
* Role-based permissions (Admin/User)
* Switch to PostgreSQL for production
* Dockerize the application
* Integration with frontend (React, Vue, etc.)

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

