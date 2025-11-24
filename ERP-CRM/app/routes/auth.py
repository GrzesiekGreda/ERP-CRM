from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.user import User
from flask_login import login_user, logout_user, login_required
from app import db

auth = Blueprint('auth', __name__, url_prefix='/auth')

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

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Zostałeś wylogowany', 'info')
    return redirect(url_for('auth.login'))
