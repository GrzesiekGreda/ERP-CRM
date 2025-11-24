from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.order import Order, OrderItem
from app.models.customer import Customer
from app.models.product import Product
from app import db
from flask_login import login_required
from datetime import datetime

sales = Blueprint('sales', __name__, url_prefix='/sales')

@sales.route('/')
@login_required
def orders():
    page = request.args.get('page', 1, type=int)
    orders = Order.query.order_by(Order.created_at.desc()).paginate(page=page, per_page=20)
    return render_template('sales/orders.html', orders=orders)

@sales.route('/new', methods=['GET', 'POST'])
@login_required
def new_order():
    if request.method == 'POST':
        # Generate order number
        today = datetime.now().strftime('%Y%m%d')
        last_order = Order.query.filter(Order.order_number.like(f'ORD-{today}%')).order_by(Order.order_number.desc()).first()
        if last_order:
            last_num = int(last_order.order_number.split('-')[-1])
            order_number = f'ORD-{today}-{str(last_num + 1).zfill(4)}'
        else:
            order_number = f'ORD-{today}-0001'
        
        order = Order(
            order_number=order_number,
            customer_id=int(request.form['customer_id']),
            status=request.form.get('status', 'pending'),
            notes=request.form.get('notes')
        )
        db.session.add(order)
        db.session.flush()
        
        # Add order items
        product_ids = request.form.getlist('product_id[]')
        quantities = request.form.getlist('quantity[]')
        unit_prices = request.form.getlist('unit_price[]')
        
        for prod_id, qty, price in zip(product_ids, quantities, unit_prices):
            if prod_id and qty and price:
                item = OrderItem(
                    order_id=order.id,
                    product_id=int(prod_id),
                    quantity=int(qty),
                    unit_price=float(price)
                )
                db.session.add(item)
        
        order.calculate_total()
        db.session.commit()
        flash('Zamówienie zostało dodane pomyślnie!', 'success')
        return redirect(url_for('sales.orders'))
    
    customers = Customer.query.filter_by(is_active=True).all()
    products = Product.query.filter_by(is_active=True).all()
    return render_template('sales/order_form.html', order=None, customers=customers, products=products)

@sales.route('/<int:id>')
@login_required
def order_detail(id):
    order = Order.query.get_or_404(id)
    return render_template('sales/order_detail.html', order=order)
