<div align="center">

<!-- Animated Health Bot SVG -->
<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="bodyGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" style="stop-color:#4ade80"/>
      <stop offset="100%" style="stop-color:#16a34a"/>
    </radialGradient>
    <radialGradient id="headGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" style="stop-color:#4ade80"/>
      <stop offset="100%" style="stop-color:#15803d"/>
    </radialGradient>
  </defs>

  <!-- Body -->
  <rect x="30" y="60" width="60" height="45" rx="10" fill="url(#bodyGrad)">
    <animate attributeName="y" values="60;57;60" dur="2s" repeatCount="indefinite"/>
  </rect>

  <!-- Head -->
  <rect x="25" y="20" width="70" height="50" rx="12" fill="url(#headGrad)">
    <animate attributeName="y" values="20;17;20" dur="2s" repeatCount="indefinite"/>
  </rect>

  <!-- Eyes -->
  <circle cx="45" cy="38" r="7" fill="white"/>
  <circle cx="75" cy="38" r="7" fill="white"/>
  <circle cx="45" cy="38" r="3.5" fill="#1e3a2f">
    <animate attributeName="r" values="3.5;2;3.5" dur="3s" repeatCount="indefinite"/>
  </circle>
  <circle cx="75" cy="38" r="3.5" fill="#1e3a2f">
    <animate attributeName="r" values="3.5;2;3.5" dur="3s" repeatCount="indefinite"/>
  </circle>

  <!-- Smile -->
  <path d="M 45 55 Q 60 65 75 55" stroke="white" stroke-width="3" fill="none" stroke-linecap="round">
    <animate attributeName="d" values="M 45 55 Q 60 65 75 55;M 45 53 Q 60 63 75 53;M 45 55 Q 60 65 75 55" dur="2s" repeatCount="indefinite"/>
  </path>

  <!-- Antenna -->
  <line x1="60" y1="20" x2="60" y2="8" stroke="#4ade80" stroke-width="3" stroke-linecap="round">
    <animate attributeName="y1" values="20;17;20" dur="2s" repeatCount="indefinite"/>
    <animate attributeName="y2" values="8;5;8" dur="2s" repeatCount="indefinite"/>
  </line>
  <circle cx="60" cy="6" r="4" fill="#f43f5e">
    <animate attributeName="cy" values="6;3;6" dur="2s" repeatCount="indefinite"/>
    <animate attributeName="fill" values="#f43f5e;#fb7185;#f43f5e" dur="1s" repeatCount="indefinite"/>
  </circle>

  <!-- Arms -->
  <rect x="8" y="63" width="22" height="10" rx="5" fill="#16a34a">
    <animate attributeName="y" values="63;60;63" dur="2s" repeatCount="indefinite"/>
  </rect>
  <rect x="90" y="63" width="22" height="10" rx="5" fill="#16a34a">
    <animate attributeName="y" values="63;60;63" dur="2s" repeatCount="indefinite"/>
  </rect>

  <!-- Legs -->
  <rect x="38" y="100" width="16" height="18" rx="5" fill="#15803d">
    <animate attributeName="y" values="100;97;100" dur="2s" repeatCount="indefinite"/>
  </rect>
  <rect x="66" y="100" width="16" height="18" rx="5" fill="#15803d">
    <animate attributeName="y" values="100;97;100" dur="2s" repeatCount="indefinite"/>
  </rect>

  <!-- Heart on chest -->
  <text x="52" y="87" font-size="14" fill="white">
    <animate attributeName="font-size" values="14;16;14" dur="1s" repeatCount="indefinite"/>
    ❤️
  </text>
</svg>

# 🏥 Health Agent Bot

### *Your AI-Powered Personal Health Coach*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1.2-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Gemini](https://img.shields.io/badge/Gemini-2.5_Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://aistudio.google.com)
[![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://health-agent-bot.onrender.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**[🚀 Live Demo](https://health-agent-bot.onrender.com)** • **[📖 Documentation](#-how-it-works)** • **[🛠 Installation](#-local-setup)**

</div>

---

## 📋 Table of Contents

| # | Section |
|---|---------|
| 01 | [About the Project](#-about-the-project) |
| 02 | [Features](#-features) |
| 03 | [Tech Stack](#-tech-stack) |
| 04 | [Architecture](#-architecture) |
| 05 | [How It Works](#-how-it-works) |
| 06 | [Project Structure](#-project-structure) |
| 07 | [Local Setup](#-local-setup) |
| 08 | [Environment Variables](#-environment-variables) |
| 09 | [Deployment](#-deployment-on-render) |
| 10 | [API Reference](#-api-reference) |

---

## 🌟 About the Project

**Health Agent Bot** is a conversational AI health coach powered by **Google Gemini 2.5 Flash**. It provides personalized advice on fitness, nutrition, sleep, mental wellness, and more — all through a beautiful, responsive chat interface.

> ⚠️ *This is an informational tool only. It does not replace professional medical advice.*

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 💬 **Conversational AI** | Natural chat powered by Gemini 2.5 Flash |
| 🏋️ **Fitness Advice** | Personalized workout routines and exercise tips |
| 🥗 **Nutrition Guidance** | Meal planning and dietary recommendations |
| 😴 **Sleep Optimization** | Sleep hygiene tips and schedule advice |
| 📊 **Health Metrics** | BMI calculation, caloric needs analysis |
| 🧠 **Mental Wellness** | Stress management and mindfulness tips |
| 🎯 **Goal Tracking** | Motivation and accountability support |
| 📱 **Responsive UI** | Works on desktop, tablet, and mobile |
| ⚡ **Fast Responses** | Waitress WSGI server for production performance |
| 🔒 **Secure** | API keys protected via environment variables |

---

## 🛠 Tech Stack

### Backend
| Technology | Version | Purpose |
|-----------|---------|---------|
| **Python** | 3.10+ | Core language |
| **Flask** | 3.1.2 | Web framework |
| **Waitress** | latest | Production WSGI server |
| **Google Generative AI** | 0.8.6 | Gemini 2.5 Flash LLM |
| **python-dotenv** | 1.2.1 | Environment variable management |

### Frontend
| Technology | Purpose |
|-----------|---------|
| **HTML5 / CSS3** | Structure and styling |
| **Vanilla JavaScript** | Chat interaction logic |
| **Jinja2 Templates** | Server-side rendering |

### Deployment
| Service | Purpose |
|---------|---------|
| **Render** | Cloud hosting (free tier) |
| **GitHub** | Version control & CI/CD trigger |

---

## 🏗 Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     USER BROWSER                        │
│         templates/index.html  +  static/                │
│         (HTML · CSS · Vanilla JS)                       │
└──────────────────────┬──────────────────────────────────┘
                       │  HTTP POST /chat
                       │  { "message": "..." }
                       ▼
┌─────────────────────────────────────────────────────────┐
│                  FLASK APP  (server.py)                 │
│                                                         │
│   GET  /          →  render_template("index.html")      │
│   POST /chat      →  parse JSON → call get_health_      │
│                       advice() → format → return JSON   │
│                                                         │
│   format_health_advice()                                │
│   Converts Gemini markdown → clean HTML                 │
│   (h1/h2/h3, ul, ol, p, strong)                        │
└──────────────────────┬──────────────────────────────────┘
                       │  Python function call
                       ▼
┌─────────────────────────────────────────────────────────┐
│                   health.py (AI Layer)                  │
│                                                         │
│   get_health_advice(user_message)                       │
│   ┌─────────────────────────────────────────────────┐  │
│   │  System Prompt (Health Coach persona)           │  │
│   │  + User Message                                 │  │
│   │        ↓                                        │  │
│   │  genai.GenerativeModel("gemini-2.5-flash")      │  │
│   │  model.start_chat(history=[])                   │  │
│   │  chat.send_message(full_prompt,                 │  │
│   │    temperature=0.8, top_p=0.95,                 │  │
│   │    max_output_tokens=8192)                      │  │
│   │        ↓                                        │  │
│   │  response.text  ←── Gemini API Response         │  │
│   └─────────────────────────────────────────────────┘  │
└──────────────────────┬──────────────────────────────────┘
                       │  HTTPS API Call
                       ▼
┌─────────────────────────────────────────────────────────┐
│              GOOGLE GEMINI 2.5 FLASH API                │
│                                                         │
│   • Large Language Model                                │
│   • Health domain knowledge                             │
│   • Conversational responses                            │
│   • Markdown formatted output                           │
└─────────────────────────────────────────────────────────┘
```

---

## 🔄 How It Works

### Request Flow — Step by Step

```
① User types a health question in the chat UI
        │
        ▼
② JavaScript sends POST /chat with JSON body
   { "message": "How do I lose weight?" }
        │
        ▼
③ Flask server.py receives the request
   → Validates message is not empty
        │
        ▼
④ Calls get_health_advice(user_message) in health.py
        │
        ▼
⑤ Builds full prompt:
   [System Instruction: Health Coach persona]
   + "User: How do I lose weight?"
   + "Health Coach AI:"
        │
        ▼
⑥ Sends to Gemini 2.5 Flash API
   temperature=0.8 (creative but focused)
   max_output_tokens=8192 (detailed responses)
        │
        ▼
⑦ Receives markdown-formatted response from Gemini
        │
        ▼
⑧ format_health_advice() converts markdown → HTML
   **bold** → <strong>
   ## Header → <h2>
   - bullet  → <ul><li>
   1. list   → <ol><li>
        │
        ▼
⑨ Returns JSON:
   { "success": true, "response": "<p>...</p>" }
        │
        ▼
⑩ JavaScript renders HTML response in chat bubble
```

---

## 📁 Project Structure

```
Health-agent-bot/
│
├── server.py              # Flask app — routes, markdown formatter
├── health.py              # AI layer — Gemini integration & prompts
├── check_models.py        # Utility to list available Gemini models
├── requirements.txt       # Python dependencies
├── Procfile               # Render deployment config
├── .gitignore             # Git ignore rules
│
├── templates/
│   └── index.html         # Main chat UI (Jinja2 template)
│
└── static/
    ├── css/               # Stylesheets
    └── js/                # Client-side JavaScript
```

---

## 🚀 Local Setup

### Prerequisites
- Python 3.10+
- A free Gemini API key from [aistudio.google.com](https://aistudio.google.com/app/apikey)

### Step 1 — Clone the repository
```bash
git clone https://github.com/soumyajyoti2005/Health-agent-bot.git
cd Health-agent-bot
```

### Step 2 — Create a virtual environment
```bash
# Linux / macOS
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Set up environment variables
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### Step 5 — Run the server
```bash
python server.py
```

### Step 6 — Open in browser
```
http://localhost:5000
```

---

## ⚙️ Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GEMINI_API_KEY` | ✅ Yes | Your Google Gemini API key. Get it free at [aistudio.google.com](https://aistudio.google.com/app/apikey) |

---

## 🌐 Deployment on Render

### Step 1 — Push to GitHub
Make sure your code is pushed to GitHub with the `Procfile` included.

### Step 2 — Create Web Service on Render
1. Go to [render.com](https://render.com) → **New → Web Service**
2. Connect your `Health-agent-bot` GitHub repo
3. Fill in the settings:

| Field | Value |
|-------|-------|
| **Runtime** | Python 3 |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `python server.py` |
| **Instance Type** | Free |

4. Add environment variable: `GEMINI_API_KEY` = your key
5. Click **Deploy Web Service**

Your app will be live at `https://health-agent-bot.onrender.com` 🎉

> ⚠️ Free tier sleeps after 15 min of inactivity. First request after sleep takes ~30 seconds.

---

## 📡 API Reference

### `GET /`
Returns the main chat interface HTML page.

---

### `POST /chat`
Send a health question and receive an AI response.

**Request Body:**
```json
{
  "message": "How many calories should I eat per day?"
}
```

**Success Response:**
```json
{
  "success": true,
  "response": "<p>Your daily caloric needs depend on...</p>"
}
```

**Error Response:**
```json
{
  "success": false,
  "error": "Please enter a message."
}
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Open an **Issue** for bugs or feature requests
- Submit a **Pull Request** with improvements

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Built with ❤️ by [soumyajyoti2005](https://github.com/soumyajyoti2005)

⭐ **Star this repo if you found it helpful!** ⭐

[Flask](https://flask.palletsprojects.com) · [Google Gemini](https://aistudio.google.com) 
</div>
