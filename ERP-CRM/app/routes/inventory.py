from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.product import Product
from app import db
from flask_login import login_required

inventory = Blueprint('inventory', __name__, url_prefix='/inventory')

@inventory.route('/')
@login_required
def products():
    page = request.args.get('page', 1, type=int)
    products = Product.query.paginate(page=page, per_page=20)
    return render_template('inventory/products.html', products=products)

@inventory.route('/new', methods=['GET', 'POST'])
@login_required
def new_product():
    if request.method == 'POST':
        product = Product(
            name=request.form['name'],
            sku=request.form['sku'],
            description=request.form.get('description'),
            category=request.form.get('category'),
            unit=request.form.get('unit', 'szt.'),
            price=float(request.form['price']),
            cost=float(request.form.get('cost', 0)),
            stock_quantity=int(request.form.get('stock_quantity', 0)),
            reorder_level=int(request.form.get('reorder_level', 10)),
            is_active='is_active' in request.form
        )
        db.session.add(product)
        db.session.commit()
        flash('Produkt został dodany pomyślnie!', 'success')
        return redirect(url_for('inventory.products'))
    return render_template('inventory/product_form.html', product=None)

@inventory.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_product(id):
    product = Product.query.get_or_404(id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.sku = request.form['sku']
        product.description = request.form.get('description')
        product.category = request.form.get('category')
        product.unit = request.form.get('unit', 'szt.')
        product.price = float(request.form['price'])
        product.cost = float(request.form.get('cost', 0))
        product.stock_quantity = int(request.form.get('stock_quantity', 0))
        product.reorder_level = int(request.form.get('reorder_level', 10))
        product.is_active = 'is_active' in request.form
        db.session.commit()
        flash('Produkt został zaktualizowany pomyślnie!', 'success')
        return redirect(url_for('inventory.products'))
    return render_template('inventory/product_form.html', product=product)
