# 🚀 FlowState AI

> AI-powered productivity assistant that fights procrastination through micro-steps and smart planning.

[![Status](https://img.shields.io/badge/status-MVP-blue)]()
[![Backend](https://img.shields.io/badge/backend-FastAPI-009688)]()
[![Mobile](https://img.shields.io/badge/mobile-React%20Native-61DAFB)]()
[![AI](https://img.shields.io/badge/AI-Google%20Gemini-4285F4)]()

---

## 📖 Overview

FlowState AI is a mobile productivity app that helps you overcome procrastination by:

- 🤖 Breaking down complex tasks into micro-steps using AI
- 🎯 Showing you ONE task at a time (Focus Mode)
- 📋 Smart task planning with swipe gestures
- 💡 Providing personalized productivity tips

**Tech Stack:**

- **Backend:** Python, FastAPI, PostgreSQL, Docker
- **Mobile:** React Native (Expo), Axios
- **AI:** Google Gemini API
- **Database:** PostgreSQL

---

## 🏗 Architecture

```
flowstate-ai/
├── backend/                 # Python FastAPI server
│   ├── database/
│   │   ├── models.py       # SQLAlchemy models (Users, Tasks)
│   │   └── db.py           # Database connection
│   ├── schemas.py          # Pydantic validation schemas
│   ├── crud.py             # CRUD operations
│   ├── auth.py             # Password hashing
│   ├── ai_service.py       # Gemini API integration
│   └── main.py             # FastAPI app & routes
├── mobile/                  # React Native (Expo) app
│   ├── app/                # Screens (Focus, Planning, Profile)
│   ├── components/         # Reusable UI components
│   └── services/
│       └── api.js          # Backend API client
├── docker-compose.yml      # PostgreSQL container
└── requirements.txt        # Python dependencies
```

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.10+
- Node.js 18+
- Docker Desktop
- Expo Go app (for mobile testing)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Adilet-tech/Flow-State.git
cd Flow-State
```

### 2️⃣ Setup Backend

```bash
# Start PostgreSQL in Docker
docker-compose up -d

# Install Python dependencies
pip install -r requirements.txt

# Create .env file
echo "DATABASE_URL=postgresql://postgres:adik@localhost:5432/flowstate_db" > .env
echo "GEMINI_API_KEY=your_gemini_api_key_here" >> .env

# Run FastAPI server
uvicorn backend.main:app --reload
```

**Backend will be available at:** `http://localhost:8000`  
**Swagger UI (API docs):** `http://localhost:8000/docs`

### 3️⃣ Setup Mobile App

```bash
cd mobile

# Install dependencies
npm install

# Start Expo development server
npx expo start
```

**Note:** Update API base URL in `mobile/services/api.js` with your local IP address:

```javascript
// Replace localhost with your computer's IP
const API_URL = "http://192.168.1.X:8000";
```

---

## 📡 API Endpoints

### Users

- `POST /users/` - Register new user

### Tasks

- `POST /tasks/` - Create task
- `GET /tasks/?status=today` - Get tasks (with optional filter)
- `PATCH /tasks/{id}` - Update task status
- `DELETE /tasks/{id}` - Delete task

### AI

- `POST /ai/decompose` - Get AI task decomposition

  ```json
  // Request
  {"task_title": "Write thesis"}

  // Response
  {
    "first_step": "Create a new document and write the title page",
    "complexity": "high",
    "tip": "Start with the easiest section to build momentum"
  }
  ```

---

## 🗄 Database Schema

### Table: `users`

| Column          | Type         | Description        |
| --------------- | ------------ | ------------------ |
| id              | Integer (PK) | Unique identifier  |
| email           | String       | User email (login) |
| hashed_password | String       | Encrypted password |
| created_at      | DateTime     | Registration date  |

### Table: `tasks`

| Column     | Type         | Description                       |
| ---------- | ------------ | --------------------------------- |
| id         | Integer (PK) | Unique identifier                 |
| title      | String       | Task name                         |
| status     | String       | `backlog`, `today`, `done`        |
| complexity | String       | `low`, `medium`, `high` (from AI) |
| ai_tip     | String       | Cached AI advice                  |
| owner_id   | Integer (FK) | Reference to user                 |
| created_at | DateTime     | Creation date                     |

---

## 🎯 Current Progress

### ✅ Completed

- [x] Git repository setup
- [x] Docker configuration (PostgreSQL)
- [x] Backend structure (`backend/database/`)
- [x] Database connection (`db.py`)
- [x] SQLAlchemy models (`models.py`)
- [x] Auto-create tables on server start

### 🚧 In Progress

- [ ] Pydantic schemas
- [ ] CRUD operations
- [ ] API routes
- [ ] AI integration

### ⏳ Planned

- [ ] Mobile app UI
- [ ] Authentication
- [ ] Push notifications

---

## 🧪 Testing

### Test Backend

```bash
# Start server
uvicorn backend.main:app --reload

# Open Swagger UI
open http://localhost:8000/docs

# Try endpoints manually or use curl:
curl -X POST http://localhost:8000/users/ \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"secret123"}'
```

### Test Mobile

```bash
cd mobile
npx expo start

# Scan QR code with Expo Go app
# Or press 'i' for iOS simulator / 'a' for Android emulator
```

---

## 🔧 Troubleshooting

**Database connection failed?**

```bash
# Reset Docker container
docker-compose down -v
docker-compose up -d

# Check if running
docker ps
```

**Mobile can't connect to backend?**

- Use your computer's local IP, not `localhost`
- Find IP: `ipconfig` (Windows) or `ifconfig` (Mac/Linux)
- Update `API_URL` in `mobile/services/api.js`

**Port 8000 already in use?**

```bash
# Change port in uvicorn command
uvicorn backend.main:app --reload --port 8001
```

---

## 🤝 Contributing

1. Pick an issue from GitHub Issues
2. Create a branch: `git checkout -b feature/issue-number`
3. Make changes and commit: `git commit -m "feat: description"`
4. Push: `git push origin feature/issue-number`
5. Open Pull Request

---

## 📝 License

This project is part of an educational portfolio.

---

## 🙋‍♂️ Author

**Adilet**  
GitHub: [@Adilet-tech](https://github.com/Adilet-tech)

---

## 📚 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Native Docs](https://reactnative.dev/)
- [Google Gemini API](https://ai.google.dev/)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)

---

**Built with ❤️ to fight procrastination, one micro-step at a time.**
