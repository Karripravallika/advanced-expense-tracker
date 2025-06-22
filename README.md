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

'''
advanced-expense-tracker/
│
├── app.py # Main Flask app
├── models.py # SQLAlchemy models
├── auth.py # Authentication routes
├── dashboard.py # Dashboard analytics & views
├── expenses.py # Add/view expense logic
├── export.py # Export expenses to CSV
├── config.py # App configuration
├── requirements.txt # Python dependencies
│
├── templates/ # HTML templates (Jinja2)
│ ├── base.html
│ ├── login.html
│ ├── register.html
│ ├── index.html
│ └── dashboard.html
│
├── static/ # CSS & JS assets
│ ├── style.css
│ ├── script.js
│ └── charts.js
│
├── instance/
│ └── expenses.db # SQLite database
└── README.md
'''

---

## 🛠 Setup Instructions

### ✅ Prerequisites

- Python 3.10+
- `pip` (Python package manager)
- Optional: `venv` for virtual environments

### 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/Karripravallika/advanced-expense-tracker.git
cd advanced-expense-tracker

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate  # On macOS/Linux

# Install required packages
pip install -r requirements.txt

# Run the Flask app
python app.py
