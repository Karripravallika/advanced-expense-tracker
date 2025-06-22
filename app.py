from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from models import db, User
from auth import auth_bp
from dashboard import dashboard_bp
from expenses import expenses_bp
from export import export_bp  # ✅ Import the export blueprint

import os

app = Flask(__name__)
app.config.from_pyfile('config.py')

# Initialize extensions
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth_bp.login'
login_manager.init_app(app)

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ✅ Register all blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(expenses_bp)
app.register_blueprint(export_bp)  # ✅ Register export routes

# ✅ Create instance directory and DB if not exist
if not os.path.exists('instance'):
    os.makedirs('instance')

if not os.path.exists('instance/expenses.db'):
    with app.app_context():
        db.create_all()

# ✅ Run the app
if __name__ == '__main__':
    app.run(debug=True)
