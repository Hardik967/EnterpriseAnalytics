# 🚀 Enterprise Analytics

An AI-Powered Recruitment Analytics Platform built using **FastAPI**, **Streamlit**, **SQLite**, and **Google Gemini AI**.

Enterprise Analytics transforms large recruitment datasets into interactive dashboards and AI-powered insights, helping recruiters, HR professionals, students, and researchers analyze hiring trends, salary distributions, company statistics, and skill demand.

---

## 📌 Features

- 📊 Interactive Recruitment Dashboard
- 💼 Job Explorer
- 🏢 Company Analytics
- 💰 Salary Analysis
- 🧠 Skills Analysis
- 🤖 AI Recruitment Assistant (Google Gemini)
- ⚡ FastAPI REST APIs
- 📈 Interactive Plotly Charts
- 🗄️ SQLite Database
- 🔍 Recruitment Data Search

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| FastAPI | Backend API |
| Streamlit | Frontend Dashboard |
| SQLite | Database |
| SQLAlchemy | ORM |
| Pandas | Data Processing |
| Plotly | Visualization |
| Google Gemini AI | AI Recruitment Assistant |

---

## 📂 Project Structure

```text
EnterpriseAnalytics/

│── backend/
│   ├── api/
│   ├── services/
│   ├── app.py
│   ├── database.py
│   ├── models.py
│   ├── load_data.py
│
│── frontend/
│   ├── Home.py
│   ├── pages/
│   │   ├── Dashboard.py
│   │   ├── Job_Explorer.py
│   │   ├── Company_Analytics.py
│   │   └── AI_Insights.py
│
│── data/
│
│── README.md
```

---

## 📊 Dataset

The project uses a real-world recruitment dataset containing:

- Companies
- Job Postings
- Salary Records
- Skills
- Job-Skill Relationships

> **Note:** Large dataset files are excluded from this repository because they exceed GitHub's file size limit.

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Hardik967/EnterpriseAnalytics.git

cd EnterpriseAnalytics
```

---

### Install Backend Dependencies

```bash
cd backend

pip install -r requirements.txt
```

---

### Create Environment File

Create a `.env` file inside the **backend** folder.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

### Load Dataset

```bash
python load_data.py
```

---

### Start Backend

```bash
python3 -m uvicorn app:app --reload
```

Backend will run on:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

### Start Frontend

Open another terminal.

```bash
cd frontend

streamlit run Home.py
```

---

## 📈 Modules

### Dashboard

- Total Jobs
- Companies
- Skills
- Average Salary
- Recruitment Charts

### Job Explorer

- Search Jobs
- Browse Recruitment Records

### Company Analytics

- Hiring Companies
- Recruitment Statistics

### AI Recruitment Assistant

Ask questions like:

- Which companies are hiring the most?
- What are the highest-paying jobs?
- Which skills are in demand?
- Generate recruitment analytics.
- Give hiring recommendations.

The AI combines recruitment database statistics with Google Gemini AI to provide intelligent responses.

---

## 🏗️ Architecture

```
Streamlit Frontend
        │
        ▼
FastAPI REST APIs
        │
 ┌──────┴───────┐
 │              │
 ▼              ▼
SQLite      Gemini AI
```

---

## 📷 Screenshots

You can add screenshots here after uploading images.

Example:

- Home Page
- Dashboard
- Job Explorer
- Company Analytics
- AI Assistant

---

## 🔮 Future Improvements

- Resume Matching
- Salary Prediction using Machine Learning
- Job Recommendation System
- Real-time Job API Integration
- Cloud Deployment
- Authentication & User Management

---

## 👨‍💻 Author

**Hardik Prajapati**

B.Tech – Artificial Intelligence & Machine Learning

---

## 📄 License

This project is developed for educational and academic purposes.
