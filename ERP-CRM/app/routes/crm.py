from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.customer import Customer
from app import db
from flask_login import login_required

crm = Blueprint('crm', __name__, url_prefix='/crm')

@crm.route('/')
@login_required
def customers():
    page = request.args.get('page', 1, type=int)
    customers = Customer.query.paginate(page=page, per_page=20)
    return render_template('crm/customers.html', customers=customers)

@crm.route('/new', methods=['GET', 'POST'])
@login_required
def new_customer():
    if request.method == 'POST':
        customer = Customer(
            name=request.form['name'],
            email=request.form['email'],
            phone=request.form.get('phone'),
            address=request.form.get('address'),
            city=request.form.get('city'),
            postal_code=request.form.get('postal_code'),
            country=request.form.get('country', 'Polska'),
            tax_id=request.form.get('tax_id'),
            notes=request.form.get('notes'),
            is_active='is_active' in request.form
        )
        db.session.add(customer)
        db.session.commit()
        flash('Klient został dodany pomyślnie!', 'success')
        return redirect(url_for('crm.customers'))
    return render_template('crm/customer_form.html', customer=None)

@crm.route('/<int:id>')
@login_required
def customer_detail(id):
    customer = Customer.query.get_or_404(id)
    total_value = sum(order.total_amount for order in customer.orders)
    return render_template('crm/customer_detail.html', customer=customer, total_value=total_value)

@crm.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_customer(id):
    customer = Customer.query.get_or_404(id)
    if request.method == 'POST':
        customer.name = request.form['name']
        customer.email = request.form['email']
        customer.phone = request.form.get('phone')
        customer.address = request.form.get('address')
        customer.city = request.form.get('city')
        customer.postal_code = request.form.get('postal_code')
        customer.country = request.form.get('country', 'Polska')
        customer.tax_id = request.form.get('tax_id')
        customer.notes = request.form.get('notes')
        customer.is_active = 'is_active' in request.form
        db.session.commit()
        flash('Klient został zaktualizowany pomyślnie!', 'success')
        return redirect(url_for('crm.customer_detail', id=customer.id))
    return render_template('crm/customer_form.html', customer=customer)
