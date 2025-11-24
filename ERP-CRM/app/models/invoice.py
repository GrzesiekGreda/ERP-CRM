from app import db
from datetime import datetime, timedelta

class Invoice(db.Model):
    __tablename__ = 'invoices'

    id = db.Column(db.Integer, primary_key=True)
    invoice_number = db.Column(db.String(50), unique=True, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    issue_date = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime, default=lambda: datetime.utcnow() + timedelta(days=30))
    notes = db.Column(db.Text)
    status = db.Column(db.String(20), default='unpaid')  # unpaid, partial, paid, overdue
    paid_amount = db.Column(db.Numeric(10, 2), default=0.00)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    customer = db.relationship('Customer', backref='invoices')
    items = db.relationship('InvoiceItem', backref='invoice', lazy=True, cascade='all, delete-orphan')

    @property
    def total_net(self):
        return sum(item.net_amount for item in self.items)

    @property
    def total_vat(self):
        return sum(item.vat_amount for item in self.items)

    @property
    def total_gross(self):
        return sum(item.gross_amount for item in self.items)

    @property
    def balance(self):
        return float(self.total_gross) - float(self.paid_amount)

    @property
    def is_overdue(self):
        return self.due_date < datetime.utcnow() and self.status != 'paid'

    def __repr__(self):
        return f'<Invoice {self.invoice_number}>'


class InvoiceItem(db.Model):
    __tablename__ = 'invoice_items'

    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoices.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=True)
    description = db.Column(db.String(500), nullable=False)
    quantity = db.Column(db.Numeric(10, 2), nullable=False)
    unit = db.Column(db.String(20), default='szt.')
    unit_price = db.Column(db.Numeric(10, 2), nullable=False)
    vat_rate = db.Column(db.Integer, default=23)  # VAT in percentage

    # Relationships
    product = db.relationship('Product', backref='invoice_items')

    @property
    def net_amount(self):
        return float(self.quantity) * float(self.unit_price)

    @property
    def vat_amount(self):
        return self.net_amount * (float(self.vat_rate) / 100)

    @property
    def gross_amount(self):
        return self.net_amount + self.vat_amount

    def __repr__(self):
        return f'<InvoiceItem {self.description}>'
