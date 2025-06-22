import os

# Get the absolute path of the current directory
basedir = os.path.abspath(os.path.dirname(__file__))

# SQLite database path using absolute reference
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'expenses.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Secret key for session management and CSRF protection
SECRET_KEY = 'your-secret-key'  # 🔐 Change this to something secure in production
