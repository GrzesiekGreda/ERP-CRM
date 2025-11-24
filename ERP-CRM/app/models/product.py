from app import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    sku = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(100))
    unit = db.Column(db.String(20), default='szt.')
    price = db.Column(db.Numeric(10, 2), nullable=False, default=0.00)
    cost = db.Column(db.Numeric(10, 2), default=0.00)
    stock_quantity = db.Column(db.Integer, default=0)
    reorder_level = db.Column(db.Integer, default=10)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    order_items = db.relationship('OrderItem', backref='product', lazy=True)
    
    @property
    def in_stock(self):
        return self.stock_quantity > 0
    
    @property
    def needs_reorder(self):
        return self.stock_quantity <= self.reorder_level
    
    @property
    def margin(self):
        return float(self.price) - float(self.cost)
    
    @property
    def margin_percent(self):
        if self.cost > 0:
            return (self.margin / float(self.cost)) * 100
        return 0
    
    def __repr__(self):
        return f'<Product {self.name}>'
