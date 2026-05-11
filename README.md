# 🏥 CareDesk AI — AI-Powered Hospital Receptionist System

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

> An AI-based receptionist system that reduces hospital waiting time by automatically collecting patient details and assigning them to the correct ward.

---

## 📌 Problem Statement

Hospitals face several challenges at the front desk:
- 🕐 Long waiting times for patients
- 👨‍⚕️ Shortage of reception staff
- 📝 Manual and error-prone form filling
- 🔀 Inefficient patient routing to correct departments

---

## 💡 Solution

**CareDesk AI** is an AI-powered virtual receptionist that:
- Accepts patient details through a simple web interface
- Understands the patient's health complaint in natural language
- Automatically classifies and assigns the patient to the correct ward
- Returns a structured digital registration instantly — no paper, no waiting

---

## 🚀 Features

| Feature | Description |
|---|---|
| 🤖 AI Ward Classification | Assigns Emergency, Mental Health, or General ward based on symptoms |
| 🌐 Web Interface | Clean and simple form for patients to fill |
| ⚡ FastAPI Backend | Built with FastAPI for quick and reliable responses |
| 🌍 Multilingual Ready | Can be extended to support multiple languages |
| 📱 Responsive Design | Works on mobile, tablet, and desktop |

---

## 🏗️ System Architecture

```
Patient (Browser)
      │
      ▼
  index.html  ──── HTTP POST ────▶  FastAPI Backend (main.py)
  (Frontend)                              │
                                          ▼
                                   AI Classification Logic
                                          │
                                          ▼
                                   Ward Assignment Response
```

### Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, FastAPI |
| AI Logic | Rule-based keyword classification |
| Server | Uvicorn |
| Database (Planned) | Supabase |

---

## 📁 Project Structure

```
caredesk-ai/
│
├── main.py          # FastAPI backend with ward classification logic
├── index.html       # Frontend web interface
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.11 or higher
- Git

### Step 1 — Clone the Repository
```bash
git clone https://github.com/vivekjadhav5740-sketch/caredesk-ai.git
cd caredesk-ai
```

### Step 2 — Create Virtual Environment
```bash
python -m venv venv
```

### Step 3 — Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### Step 4 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5 — Run the Server
```bash
uvicorn main:app --reload
```

### Step 6 — Open the App
- Backend running at: `http://127.0.0.1:8000`
- Open `index.html` in your browser

---

## 🔗 API Reference

### Base URL
```
http://127.0.0.1:8000
```

### Endpoints

#### GET `/`
Check if server is running.

**Response:**
```json
{
  "message": "CareDesk AI is running!"
}
```

#### POST `/process_patient`
Submit patient details and get ward assignment.

**Request Body:**
```json
{
  "name": "Vivek Jadhav",
  "age": 22,
  "query": "I have severe chest pain"
}
```

**Response:**
```json
{
  "patient_name": "Vivek Jadhav",
  "patient_age": 22,
  "patient_query": "I have severe chest pain",
  "ward": "Emergency Ward",
  "timestamp": "2026-05-11 09:11:00"
}
```

---

## 🧠 Ward Classification Logic

| Keywords Detected | Ward Assigned |
|---|---|
| chest pain, accident, bleeding, heart attack, stroke, fracture, injury, faint, unconscious | 🔴 Emergency Ward |
| anxiety, stress, depression, mental, suicidal, panic, trauma, psychiatric | 🟣 Mental Health Ward |
| anything else | 🟢 General Ward |

---

## 📸 Screenshots

### Web Interface
> Patient fills in their name, age, and health complaint and gets instantly assigned to the correct ward.

### API Response (FastAPI Swagger UI)
> Visit `http://127.0.0.1:8000/docs` to test the API directly in the browser.

---

## 🔮 Future Scope

- [ ] 💬 Chat interface for conversational input
- [ ] 🎙️ Voice input support
- [ ] 🏥 Real hospital management system integration
- [ ] 🗄️ Supabase database for storing patient records
- [ ] 🤖 LLM-based AI classification (replace rule-based logic)
- [ ] 📊 Admin dashboard with analytics
- [ ] 🌐 Multi-language support (Hindi, Marathi, etc.)

---

## 👨‍💻 Author

**Vivek Jadhav**

- GitHub: [@vivekjadhav5740-sketch](https://github.com/vivekjadhav5740-sketch)

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/) — Modern Python web framework
- [Uvicorn](https://www.uvicorn.org/) — Lightning-fast ASGI server
- Lean Canvas methodology for business model planning
