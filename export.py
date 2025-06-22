from flask import Blueprint, send_file
from flask_login import login_required, current_user
from models import Expense
import csv
from io import BytesIO, StringIO

export_bp = Blueprint('export_bp', __name__)

@export_bp.route('/export/csv')
@login_required
def export_csv():
    # Use StringIO to write CSV in memory
    csv_buffer = StringIO()
    writer = csv.writer(csv_buffer)
    writer.writerow(['Name', 'Amount', 'Category', 'Date'])

    # Get user's expenses
    expenses = Expense.query.filter_by(user_id=current_user.id).all()
    for exp in expenses:
        writer.writerow([exp.name, exp.amount, exp.category, exp.date.strftime('%Y-%m-%d')])

    # Convert to BytesIO for Flask send_file
    bytes_buffer = BytesIO()
    bytes_buffer.write(csv_buffer.getvalue().encode('utf-8'))
    bytes_buffer.seek(0)
    csv_buffer.close()

    return send_file(
        bytes_buffer,
        mimetype='text/csv',
        as_attachment=True,
        download_name='expenses.csv'
    )
