from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

# Create Blueprint for auth routes
auth_bp = Blueprint('auth_bp', __name__)

# ---------------------------
# Register Route
# ---------------------------
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email'].lower().strip()
        password = request.form['password'].strip()

        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('⚠️ Email already exists.', 'warning')
            return redirect(url_for('auth_bp.register'))

        # ✅ Hash password securely using pbkdf2:sha256
        hashed_pw = generate_password_hash(password, method='pbkdf2:sha256')

        # Create new user
        new_user = User(email=email, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()

        flash('✅ Registration successful! Please log in.', 'success')
        return redirect(url_for('auth_bp.login'))

    return render_template('register.html')

# ---------------------------
# Login Route
# ---------------------------
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email'].lower().strip()
        password = request.form['password'].strip()

        # Look up user
        user = User.query.filter_by(email=email).first()

        # Check password
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('✅ Login successful.', 'success')
            return redirect(url_for('dashboard_bp.dashboard'))

        flash('❌ Invalid email or password.', 'danger')
        return redirect(url_for('auth_bp.login'))

    return render_template('login.html')

# ---------------------------
# Logout Route
# ---------------------------
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('👋 Logged out successfully.', 'info')
    return redirect(url_for('auth_bp.login'))
