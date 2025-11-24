from flask import Blueprint, render_template, send_from_directory, request, redirect, url_for, flash
from app.models.customer import Customer
from app.models.product import Product
from app.models.order import Order
from app.models.company import Company
from app import db
from flask_login import login_required
from sqlalchemy import func
import os

main = Blueprint('main', __name__)

@main.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(main.root_path, '..', 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@main.route('/')
@login_required
def dashboard():
    # Statistics
    total_customers = Customer.query.count()
    total_products = Product.query.count()
    total_orders = Order.query.count()
    total_revenue = db.session.query(func.sum(Order.total_amount)).scalar() or 0

    # Recent customers
    recent_customers = Customer.query.order_by(Customer.created_at.desc()).limit(5).all()

    # Low stock products
    low_stock_products = Product.query.filter(
        Product.stock_quantity <= Product.reorder_level
    ).limit(5).all()

    return render_template('dashboard.html',
                         total_customers=total_customers,
                         total_products=total_products,
                         total_orders=total_orders,
                         total_revenue=total_revenue,
                         recent_customers=recent_customers,
                         low_stock_products=low_stock_products)

@main.route('/settings/company', methods=['GET', 'POST'])
@login_required
def company_settings():
    company = Company.query.first()
    
    if request.method == 'POST':
        if not company:
            company = Company()
            db.session.add(company)
        
        company.name = request.form['name']
        company.address = request.form.get('address', '')
        company.postal_code = request.form.get('postal_code', '')
        company.city = request.form.get('city', '')
        company.country = request.form.get('country', 'Polska')
        company.tax_id = request.form.get('tax_id', '')
        company.phone = request.form.get('phone', '')
        company.email = request.form.get('email', '')
        company.bank_account = request.form.get('bank_account', '')
        company.bank_name = request.form.get('bank_name', '')
        
        db.session.commit()
        flash('Dane firmy zostały zaktualizowane', 'success')
        return redirect(url_for('main.company_settings'))
    
    return render_template('settings/company.html', company=company)
