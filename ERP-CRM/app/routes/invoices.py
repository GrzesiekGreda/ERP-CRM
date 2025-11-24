from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.invoice import Invoice, InvoiceItem
from app.models.customer import Customer
from app.models.product import Product
from app.models.company import Company
from app import db
from flask_login import login_required
from datetime import datetime

invoices = Blueprint('invoices', __name__, url_prefix='/invoices')

@invoices.route('/')
@login_required
def invoice_list():
    page = request.args.get('page', 1, type=int)
    invoices = Invoice.query.order_by(Invoice.created_at.desc()).paginate(page=page, per_page=20)
    return render_template('invoices/invoices.html', invoices=invoices)

@invoices.route('/new', methods=['GET', 'POST'])
@login_required
def invoice_new():
    if request.method == 'POST':
        try:
            # Generate invoice number
            today = datetime.now()
            date_str = today.strftime('%Y%m%d')
            last_invoice = Invoice.query.filter(
                Invoice.invoice_number.like(f'INV-{date_str}-%')
            ).order_by(Invoice.invoice_number.desc()).first()
            
            if last_invoice:
                last_number = int(last_invoice.invoice_number.split('-')[-1])
                new_number = last_number + 1
            else:
                new_number = 1
            
            invoice_number = f'INV-{date_str}-{new_number:04d}'
            
            # Create invoice
            invoice = Invoice(
                invoice_number=invoice_number,
                customer_id=request.form['customer_id'],
                notes=request.form.get('notes', '')
            )
            
            # Add invoice items
            product_ids = request.form.getlist('product_id[]')
            descriptions = request.form.getlist('description[]')
            quantities = request.form.getlist('quantity[]')
            units = request.form.getlist('unit[]')
            unit_prices = request.form.getlist('unit_price[]')
            vat_rates = request.form.getlist('vat_rate[]')
            
            for i in range(len(descriptions)):
                if descriptions[i].strip():
                    item = InvoiceItem(
                        product_id=product_ids[i] if product_ids[i] else None,
                        description=descriptions[i],
                        quantity=float(quantities[i]),
                        unit=units[i],
                        unit_price=float(unit_prices[i]),
                        vat_rate=int(vat_rates[i])
                    )
                    invoice.items.append(item)
            
            db.session.add(invoice)
            db.session.commit()
            
            flash(f'Faktura {invoice_number} została utworzona', 'success')
            return redirect(url_for('invoices.invoice_detail', id=invoice.id))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Błąd podczas tworzenia faktury: {str(e)}', 'danger')
    
    customers = Customer.query.filter_by(is_active=True).order_by(Customer.name).all()
    products = Product.query.filter_by(is_active=True).order_by(Product.name).all()
    return render_template('invoices/invoice_form.html', customers=customers, products=products)

@invoices.route('/<int:id>')
@login_required
def invoice_detail(id):
    invoice = Invoice.query.get_or_404(id)
    company = Company.query.first()
    return render_template('invoices/invoice_detail.html', invoice=invoice, company=company)
