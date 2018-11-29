from flask import (
    Blueprint,
    flash,
    request
)
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_rq import get_queue

from app import db
from app.models import User

account = Blueprint('account', __name__)


@account.route('/login', methods=['GET', 'POST'])
def login():
    user = User.query.filter_by(email=request.form.get("email")).first()
    if user is not None and user.password_hash is not None and \
            user.verify_password(request.form.get("password")):
        login_user(user, remember=True)
        flash('You are now logged in. Welcome back!', 'success')
        return 'You are now logged in. Welcome back!'
    else:
        flash('Invalid email or password.', 'form-error')
    return 'Invalid email or password.'

@account.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return 'You have been logged out.'
