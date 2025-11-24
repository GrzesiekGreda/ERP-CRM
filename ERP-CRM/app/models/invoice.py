from app import db
from datetime import datetime, timedelta

class Invoice(db.Model):
    __tablename__ = 'invoices'
    
    id = db.Column(db.Integer, primary_key=True)
    invoice_number = db.Column(db.String(50), unique=True, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    issue_date = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime, default=lambda: datetime.utcnow() + timedelta(days=30))
    total_amount = db.Column(db.Numeric(10, 2), nullable=False)
    paid_amount = db.Column(db.Numeric(10, 2), default=0.00)
    status = db.Column(db.String(20), default='unpaid')  # unpaid, partial, paid, overdue
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    @property
    def balance(self):
        return float(self.total_amount) - float(self.paid_amount)
    
    @property
    def is_overdue(self):
        return self.due_date < datetime.utcnow() and self.status != 'paid'
    
    def __repr__(self):
        return f'<Invoice {self.invoice_number}>'
