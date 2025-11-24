from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Zaloguj się, aby uzyskać dostęp do tej strony.'
    login_manager.login_message_category = 'warning'

    # Import models
    from app.models import user, customer, product, order, invoice, company

    # Register blueprints
    from app.routes.main import main
    from app.routes.auth import auth
    from app.routes.crm import crm
    from app.routes.inventory import inventory
    from app.routes.sales import sales
    from app.routes.invoices import invoices

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(crm)
    app.register_blueprint(inventory)
    app.register_blueprint(sales)
    app.register_blueprint(invoices)

    # Create database tables
    with app.app_context():
        db.create_all()

        # Create admin user if not exists
        from app.models.user import User
        admin = User.query.filter_by(email=app.config['ADMIN_EMAIL']).first()
        if not admin:
            admin = User(
                username='grzegorz',
                email=app.config['ADMIN_EMAIL'],
                is_admin=True
            )
            admin.set_password(app.config['ADMIN_PASSWORD'])
            db.session.add(admin)
            db.session.commit()
            print(' Utworzono użytkownika admin: ' + app.config['ADMIN_EMAIL'])

        # Create default company if not exists
        from app.models.company import Company
        company = Company.query.first()
        if not company:
            company = Company(
                name='Moja Firma Sp. z o.o.',
                address='ul. Przykładowa 123',
                postal_code='00-001',
                city='Warszawa',
                country='Polska',
                tax_id='123-456-78-90',
                phone='+48 123 456 789',
                email='kontakt@mojafirma.pl'
            )
            db.session.add(company)
            db.session.commit()
            print(' Utworzono domyślne dane firmy')

    return app
