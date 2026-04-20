# ♾️ BoT — AI Chatbot App

AI-powered chatbot web app built with FastAPI, Streamlit, and Groq LLM. Supports user authentication and conversational AI with chat history.

Demo link: https://hurisrdnhftjjsxp4jhbvb.streamlit.app

---

## 🛠️ Tech Stack

| Layer      | Technology               |
|------------|--------------------------|
| Frontend   | Streamlit                |
| Backend    | FastAPI + Uvicorn        |
| AI / LLM   | Groq (LLaMA 3.3 70B)     |
| Database   | MySQL (Clever Cloud)     |
| Deployment | Render + Streamlit Cloud |

---

## ✨ Features

- 🔐 User Registration & Login
- 💬 AI Chatbot with full conversation history
- 📄 File upload support (PDF, CSV, XLSX, TXT)
- 🔒 Secure authentication with password validation
- ⚡ Fast LLM responses via Groq API

---

## 📁 Project Structure

```
bot/
├── app.py                  # FastAPI entry point
├── Home.py                 # Streamlit main page
├── requirements.txt
├── .env                    # Environment variables (not uploaded)
├── routers/
│   └── users.py            # All API routes
├── model/
│   └── schemas.py          # Pydantic models
├── data/
│   └── connection.py       # MySQL connection
├── dependencies/
│   └── dependency.py       # DB dependency injection
├── llm/
│   └── response.py         # Groq LLM logic
└── pages/
    ├── 1_Register.py
    ├── 2_Login.py
    └── 3_Settings.py
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/register_user` | Register a new user |
| POST | `/login_user` | Login existing user |
| POST | `/history_chat` | Chat with AI (with history) |
| POST | `/file_upload` | Upload a file |

---

## ⚙️ Setup Locally

### 1. Clone the repo
```bash
git clone https://github.com/your-username/bot.git
cd bot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create `.env` file
```
DB_HOST=your_mysql_host
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_NAME=your_database_name
DB_PORT=3306
groq_api_key=your_groq_api_key
```

### 4. Run the backend
```bash
uvicorn app:app --reload
```

### 5. Run the frontend
```bash
streamlit run Home.py
```

---

## 🌐 Deployment

| Service | Purpose | Free? |
|---|---|---|
| [Render](https://render.com) | FastAPI backend | ✅ |
| [Streamlit Cloud](https://streamlit.io/cloud) | Frontend UI | ✅ |
| [Clever Cloud](https://clever-cloud.com) | MySQL database | ✅ |

---

## 📝 Notes

- Render free tier **sleeps after inactivity** — first request may take ~30 seconds
- `.env` file is **not included** in the repo for security
- Passwords must be 8–16 characters, email must be a Gmail address

---

## 👤 Author

**Sanidhya** — [GitHub](https://github.com/sanidhya2803)
