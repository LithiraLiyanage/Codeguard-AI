# CodeGuard AI — AI Code Review & Bug Detection Platform

Production-quality full-stack portfolio project for **Full Stack Developer | AI Engineer** internship roles.

CodeGuard AI lets users paste code, upload source files, or submit a public GitHub repository URL. The system analyzes JavaScript/TypeScript, Python, and Java code and returns defensive code review results: bugs, security issues, code smells, quality score, maintainability score, complexity score, and safe refactoring suggestions.

## Safety Scope
This tool is for defensive secure coding education and code quality improvement only. It does not generate exploit payloads, malware, credential theft logic, or instructions for abusing vulnerabilities.

## Tech Stack

| Layer | Stack |
|---|---|
| Frontend | React, Vite, Tailwind CSS, React Router, Axios, Monaco Editor, Recharts, Lucide React |
| Backend | Node.js, Express.js, MongoDB, Mongoose, JWT, bcryptjs, Multer, simple-git |
| Security | Helmet, CORS, express-rate-limit, express-validator |
| AI Service | Python, FastAPI, Pydantic, AST parsing, Radon, rule-based static analysis |
| Database | MongoDB |

## Features

- Register/login with JWT authentication
- Developer and admin roles
- Paste-code analyzer with Monaco Editor
- File upload analyzer for `.js`, `.jsx`, `.ts`, `.tsx`, `.py`, `.java`
- Public GitHub repository analyzer
- Defensive security issue detection
- Bug and code-smell detection
- Complexity and maintainability scoring
- Review history with search/filter
- Detailed review page
- JSON report download
- Admin analytics dashboard

## Architecture

```text
React Frontend
   |
   | REST API + JWT
   v
Express Backend
   |
   | Mongoose
   v
MongoDB
   |
   | HTTP JSON
   v
FastAPI AI Service
   |
   | AST + Static Rules
   v
Bugs / Security / Complexity / Suggestions
```

## Run Locally

### 1. Start MongoDB

```bash
docker compose up -d mongo
```

### 2. Start AI Service

```bash
cd ai-service
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Start Backend

```bash
cd backend
npm install
copy .env.example .env
npm run dev
```

### 4. Start Frontend

```bash
cd frontend
npm install
copy .env.example .env
npm run dev
```

Frontend: `http://localhost:5173`  
Backend: `http://localhost:5000`  
AI Service: `http://localhost:8000`

## Admin Account

Register using this email to become admin:

```text
admin@example.com
```

## API Endpoints

### Auth

```text
POST /api/auth/register
POST /api/auth/login
GET  /api/auth/me
```

### Reviews

```text
POST   /api/reviews/analyze-code
POST   /api/reviews/analyze-file
POST   /api/reviews/analyze-github
GET    /api/reviews/history
GET    /api/reviews/:id
DELETE /api/reviews/:id
```

### Admin

```text
GET /api/admin/stats
GET /api/admin/reviews
GET /api/admin/users
```

## CV Bullet

Developed an AI-powered code review platform that analyzes JavaScript, Python, and Java code to detect bugs, security issues, code smells, and complexity problems using a React frontend, Node.js backend, MongoDB, and Python FastAPI static analysis microservice.
