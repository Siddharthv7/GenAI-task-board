# Gen-AI Task Board

A Gen-AI inspired full-stack task management application designed to demonstrate AI-style reasoning, prioritization, and productivity insights using a clean and lightweight architecture.

The system simulates LLM-like behavior without relying on external AI APIs, making it cost-effective, deterministic, and easily extensible for real Gen-AI integrations.

---

## 🚀 Live Application
🔗 https://<your-username>-genai-task-board.hf.space

---

## 🧠 Key Features

- AI-inspired task understanding and intent detection
- Automatic task categorization and priority assignment
- Task scoring and ranking based on importance
- Smart AI-style recommendations on what to work on next
- Productivity analytics and completion insights
- Clean REST APIs built with FastAPI
- Modern, minimal frontend using React and Tailwind CSS
- Fully containerized using Docker
- Free deployment on Hugging Face Spaces

---

## 🏗️ Architecture Overview

Frontend (React + Tailwind)
↓
FastAPI Backend (REST APIs)
↓
AI-Style Reasoning & Scoring Engine


The backend serves both the API layer and the frontend UI, allowing the entire application to run as a single service.

---

## 🛠️ Tech Stack

**Backend**
- Python
- FastAPI
- Uvicorn

**Frontend**
- React (CDN)
- Tailwind CSS

**Deployment**
- Docker
- Hugging Face Spaces

---

## 📡 API Endpoints

| Endpoint | Method | Description |
|--------|--------|-------------|
| `/tasks` | GET | Get all tasks (ranked by score) |
| `/tasks` | POST | Create a new task |
| `/tasks/{id}` | PUT | Toggle task completion |
| `/tasks/{id}` | DELETE | Delete a task |
| `/analytics` | GET | Task analytics and completion stats |
| `/ai-insights` | GET | AI-style productivity recommendations |
| `/docs` | GET | Interactive API documentation |

---

## 🧠 Gen-AI Design Notes

- The application includes a **reasoning layer** that simulates how an LLM interprets user intent.
- Task categorization, prioritization, and scoring are isolated from business logic.
- The architecture is **LLM-ready** and can be extended with OpenAI, Claude, or other Gen-AI APIs with minimal changes.

---

## 🧪 Example Tasks

Build Gen-AI task board
Study FastAPI concepts
Client meeting discussion
Go to gym


Each task is automatically analyzed and enriched with AI-style metadata.

---

## ▶️ Run Locally (Optional)

docker build -t genai-task-board .
docker run -p 7860:7860 genai-task-board

📌 Deployment

The project is deployed using Docker on Hugging Face Spaces, ensuring:

Free hosting

Reproducible builds

No external service dependencies

👤 Author

Siddharth Vaishnav
Computer Engineering | Gen-AI & Backend Enthusiast

📄 License

This project is released under the MIT License.

---

# 🏆 WHY THIS README WORKS

✔ Professional tone  
✔ Clear Gen-AI positioning  
✔ Recruiter-friendly  
✔ Not over-verbose  
✔ Explains reasoning, not just features  

---

If you want next, I can:
- ✉️ Write **final submission email**
- 🎯 Prepare **interview Q&A**
- 🧠 Help you explain this as a **Gen-AI project on resume**

Just tell me 👍
