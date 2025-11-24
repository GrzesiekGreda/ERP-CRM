from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.user import User
from flask_login import login_user, logout_user, login_required
from app import db
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

auth = Blueprint('auth', __name__, url_prefix='/auth')

def send_registration_email(user_data):
    """Wysyła email z informacją o nowej rejestracji"""
    try:
        sender_email = "system@erp-crm.local"
        recipient_email = "kontakt@greda.pl"
        
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = f"Nowa rejestracja w systemie ERP/CRM - {user_data['username']}"
        
        body = f"""
Nowa rejestracja użytkownika w systemie ERP/CRM

Data rejestracji: {user_data['timestamp']}
Nazwa użytkownika: {user_data['username']}
Email: {user_data['email']}
Adres IP: {user_data['ip_address']}

---
System ERP/CRM
© 2025 GREDA
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Uwaga: Wymaga konfiguracji SMTP serwera
        # W produkcji użyj SendGrid, Mailgun lub innego serwisu email
        # Na razie tylko logujemy do konsoli
        print(f"[EMAIL] Wysłano powiadomienie o rejestracji: {user_data['email']}")
        
    except Exception as e:
        print(f"[ERROR] Błąd wysyłania emaila: {str(e)}")

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Nieprawidłowy email lub hasło', 'danger')
    
    return render_template('auth/login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')
        
        # Walidacja
        if not username or not email or not password:
            flash('Wszystkie pola są wymagane', 'danger')
            return render_template('auth/register.html')
        
        if password != password_confirm:
            flash('Hasła nie są identyczne', 'danger')
            return render_template('auth/register.html')
        
        if len(password) < 6:
            flash('Hasło musi mieć co najmniej 6 znaków', 'danger')
            return render_template('auth/register.html')
        
        # Sprawdź czy użytkownik już istnieje
        if User.query.filter_by(email=email).first():
            flash('Użytkownik z tym adresem email już istnieje', 'danger')
            return render_template('auth/register.html')
        
        if User.query.filter_by(username=username).first():
            flash('Nazwa użytkownika jest już zajęta', 'danger')
            return render_template('auth/register.html')
        
        # Utwórz nowego użytkownika
        new_user = User(
            username=username,
            email=email,
            is_admin=False
        )
        new_user.set_password(password)
        
        db.session.add(new_user)
        db.session.commit()
        
        # Wysyłka emaila z powiadomieniem
        user_data = {
            'username': username,
            'email': email,
            'timestamp': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
            'ip_address': request.remote_addr
        }
        send_registration_email(user_data)
        
        flash('Rejestracja zakończona pomyślnie! Możesz się teraz zalogować.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Zostałeś wylogowany', 'info')
    return redirect(url_for('auth.login'))
