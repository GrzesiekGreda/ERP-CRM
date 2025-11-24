from flask import Blueprint, render_template, request
from app.models.invoice import Invoice
from flask_login import login_required

invoices = Blueprint('invoices', __name__, url_prefix='/invoices')

@invoices.route('/')
@login_required
def invoice_list():
    page = request.args.get('page', 1, type=int)
    invoices = Invoice.query.order_by(Invoice.created_at.desc()).paginate(page=page, per_page=20)
    return render_template('invoices/invoices.html', invoices=invoices)

@invoices.route('/<int:id>')
@login_required
def invoice_detail(id):
    invoice = Invoice.query.get_or_404(id)
    return render_template('invoices/invoice_detail.html', invoice=invoice)
