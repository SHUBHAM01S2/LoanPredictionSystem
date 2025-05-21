````markdown
# 🏦 Loan Status Prediction Web App

A modern, responsive web application that predicts loan approval status based on user inputs like gender, marital status, education, employment, income, and loan amount. Built using HTML, CSS, and a backend integrated with a machine learning model (Django/Flask supported).

---

## 🚀 Features

- Beautiful dark-glassmorphic UI
- Responsive layout for all screen sizes
- Dropdown menus for key applicant details
- Input fields for income and loan amount
- Instant prediction result on submission

---

## 📸 Screenshot

![Loan Status Prediction UI](screenshot.png) <!-- Replace with actual path -->

---

## 🧠 How It Works

1. User fills in the form with personal and financial details.
2. Data is submitted to the backend via `GET` method (`/result` endpoint).
3. Backend uses a trained ML model to predict loan status.
4. Result is displayed directly on the frontend.

---

## ⚙️ Tech Stack

- **Frontend:** HTML5, CSS3 (Glassmorphism design)
- **Backend:** Flask or Django (choose one)
- **Model:** Pre-trained Machine Learning model for classification

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/loan-status-predictor.git
cd loan-status-predictor
````

### 2. Setup Python Environment (If Flask/Django)

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Run the App

#### Flask

```bash
python app.py
```

#### Django

```bash
python manage.py runserver
```

Then visit: `http://127.0.0.1:5000/` or `http://127.0.0.1:8000/`

---

## 📁 Project Structure

```bash
loan-status-predictor/
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── app.py or manage.py
├── model.pkl
├── requirements.txt
└── README.md
```

---

## 📝 Form Fields

* Gender (Male/Female)
* Marital Status (Yes/No)
* Education (Graduate/Not Graduate)
* Self-Employed (Yes/No)
* Applicant Income
* Loan Amount

---

## 📚 Future Improvements

* Add mobile-optimized form layout
* Include more prediction features (credit history, dependents)
* Use AJAX for seamless UX
* Deploy to cloud (Render, Vercel, or Heroku)

---

## 💡 License

MIT License - Feel free to use, share, and improve this project.

---

## 👨‍💻 Author

**Shubham Sharma**

