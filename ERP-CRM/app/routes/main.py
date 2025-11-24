from flask import Blueprint, render_template, send_from_directory
from app.models.customer import Customer
from app.models.product import Product
from app.models.order import Order
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
