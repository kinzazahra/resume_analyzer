# 🤖 AI Resume Analyzer

## 🚀 Overview

**AI Resume Analyzer** is a web-based application that evaluates resumes against a given job description. It extracts key skills using NLP techniques, compares them with job requirements, and generates an **ATS (Applicant Tracking System) score**, along with missing skills and improvement suggestions.

---

## 💡 Features

* 📄 **Upload Resume (PDF)**
* 🧠 **Automatic Text Extraction**
* 🔍 **Skill Extraction from Resume & Job Description**
* 📊 **ATS Score Calculation**
* 📌 **Missing Skills Identification**
* 💬 **Smart Suggestions for Improvement**
* 🌐 **User-Friendly Web Interface**

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **NLP:** Basic NLP + Keyword Matching (Upgradeable to spaCy)
* **Machine Learning:** Cosine Similarity (Scikit-learn)
* **PDF Processing:** PyMuPDF
* **Frontend:** HTML, CSS

---

## 📁 Project Structure

```bash
resume_analyzer/
│
├── app.py                  # Main Flask application
│
├── utils/
│   ├── parser.py           # Extract text from PDF
│   ├── skills.py           # Skill extraction logic
│   ├── matcher.py          # ATS score calculation
│
├── templates/
│   └── index.html          # Frontend UI
│
├── uploads/                # Uploaded resumes
│
├── skills_db.txt           # Skills database
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/kinzazahra/resume_analyzer.git
cd resume_analyzer
```

### 2️⃣ Install Dependencies

```bash
pip install flask pymupdf scikit-learn
```

### 3️⃣ Run Application

```bash
python app.py
```

### 4️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

## 📊 How It Works

1. User uploads a resume (PDF).
2. The system extracts text using PyMuPDF.
3. Skills are identified from both resume and job description.
4. Cosine similarity is used to calculate ATS score.
5. Missing skills are displayed for improvement.

---

## 🎯 Example Usage

### ✔ Job Description Input

```
Looking for a Python developer with skills in flask, sql, machine learning, and communication.
```

### ✔ Output

* 📊 ATS Score: 75%
* ✅ Matched Skills: Python, Flask
* ❌ Missing Skills: SQL, Machine Learning

---

## 📈 Future Enhancements

* 🤖 Advanced NLP using spaCy
* 📊 Interactive charts (Chart.js)
* 🎨 Modern UI (Tailwind CSS)
* 📱 Mobile responsiveness
* 🌐 Deployment (Render / Railway)
* 🧠 LLM-based suggestions (AI feedback)

---

## 👩‍💻 Author

**Kinza Zahra**

---


