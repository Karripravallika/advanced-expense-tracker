from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db, Expense
import datetime

expenses_bp = Blueprint('expenses_bp', __name__)

@expenses_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_expense():
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        category = request.form['category']

        # Validation
        if not name or not amount or not category:
            flash("Please fill in all fields.", "warning")
            return redirect(url_for('expenses_bp.add_expense'))

        try:
            amount = float(amount)
        except ValueError:
            flash("Amount must be a number.", "danger")
            return redirect(url_for('expenses_bp.add_expense'))

        # Save to DB
        new_expense = Expense(
            name=name,
            amount=amount,
            category=category,
            user_id=current_user.id,
            date=datetime.datetime.now()
        )
        db.session.add(new_expense)
        db.session.commit()

        flash("Expense added successfully!", "success")
        return redirect(url_for('dashboard_bp.dashboard'))

    return render_template('index.html')
