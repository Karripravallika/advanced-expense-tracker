from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from models import db, Expense
from datetime import datetime
from collections import defaultdict

dashboard_bp = Blueprint('dashboard_bp', __name__)

# ---------------------------
# Dashboard View
# ---------------------------
@dashboard_bp.route('/')
@login_required
def dashboard():
    # Fetch all expenses for the current user
    expenses = Expense.query.filter_by(user_id=current_user.id).order_by(Expense.date.desc()).all()

    # Prepare chart data: category totals
    category_totals = defaultdict(float)
    for exp in expenses:
        category_totals[exp.category] += exp.amount

    labels = list(category_totals.keys())
    totals = list(category_totals.values())

    return render_template(
        'dashboard.html',
        expenses=expenses,
        labels=labels,
        totals=totals
    )

# ---------------------------
# Summary API (Optional AJAX)
# ---------------------------
@dashboard_bp.route('/summary-data')
@login_required
def summary_data():
    # API endpoint to return summary data as JSON (if needed for JS)
    expenses = Expense.query.filter_by(user_id=current_user.id).all()
    category_totals = defaultdict(float)
    total_spent = 0

    for exp in expenses:
        category_totals[exp.category] += exp.amount
        total_spent += exp.amount

    return jsonify({
        'categories': list(category_totals.keys()),
        'totals': list(category_totals.values()),
        'total_spent': total_spent
    })
