# 💰 Advanced Expense Tracker

A full-featured web application built with **Flask**, **SQLite**, and **Bootstrap** for managing personal expenses. It supports authentication, dashboard analytics, chart visualizations, and CSV export.

---

## 🚀 Features

- ✅ User Registration & Login (secure password hashing with Werkzeug)
- 🧾 Add, View, and Categorize Expenses
- 📊 Interactive Dashboard with Chart.js (category-wise expense charts)
- 💾 Export Expenses to CSV
- 🔐 Login-protected routes using Flask-Login
- 📂 Modular Flask Blueprints structure
- 🎨 Clean, responsive UI using Bootstrap 5

---

## 📁 Folder Structure

# 💰 Advanced Expense Tracker

A full-featured web application built with **Flask**, **SQLite**, and **Bootstrap** for managing personal expenses. It supports authentication, dashboard analytics, chart visualizations, and CSV export.

---

## 🚀 Features

- ✅ User Registration & Login (secure password hashing with Werkzeug)
- 🧾 Add, View, and Categorize Expenses
- 📊 Interactive Dashboard with Chart.js (category-wise expense charts)
- 💾 Export Expenses to CSV
- 🔐 Login-protected routes using Flask-Login
- 📂 Modular Flask Blueprints structure
- 🎨 Clean, responsive UI using Bootstrap 5

---


## 📁 Folder Structure

```plaintext
advanced-expense-tracker/
│
├── app.py                  # Main Flask app
├── auth.py                 # Authentication routes (register, login, logout)
├── config.py               # App configuration
├── dashboard.py            # Dashboard routes (summary, charts)
├── expenses.py             # Add/view expenses logic
├── export.py               # Export expenses as CSV
├── models.py               # SQLAlchemy models for User and Expense
├── requirements.txt        # Project dependencies
│
├── instance/
│   └── expenses.db         # SQLite database file
│
├── static/
│   ├── style.css           # Custom styles
│   ├── script.js           # JS for interactivity
│   └── charts.js           # Chart.js configuration
│
├── templates/
│   ├── base.html           # Base template with Bootstrap
│   ├── login.html          # User login page
│   ├── register.html       # User registration page
│   ├── index.html          # Add/view expense form
│   └── dashboard.html      # Dashboard with charts and summary
│
└── README.md               # Project documentation



