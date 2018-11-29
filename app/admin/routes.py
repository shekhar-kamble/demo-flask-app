from flask import (
    Blueprint,
    abort,
    redirect,
    request,
    url_for,
)
from flask_login import current_user, login_required
from flask_rq import get_queue
import json
from app import db
from app.decorators import admin_required
from app.models import Bank, Role, User

admin = Blueprint('admin', __name__)


@admin.route('/new_user', methods=['GET', 'POST'])
@login_required
@admin_required
def new_user():
    user = User(
        role=form.role.data,
        first_name=form.first_name.data,
        last_name=form.last_name.data,
        email=form.email.data,
        password=form.password.data)
    db.session.add(user)
    db.session.commit()
    return "yes"

@admin.route('/users', methods=['GET'])
@login_required
@admin_required
def registered_users():
    users = User.query.all()
    roles = Role.query.all()
    return " ".join([str(u) for u in users])


@admin.route('/user/<int:user_id>/delete', methods=['DELETE'])
@login_required
@admin_required
def delete_user(user_id):
    """Delete a user's account."""
    if current_user.id == user_id:
        return "cannot delete self" 
    else:
        user = User.query.filter_by(id=user_id).first()
        db.session.delete(user)
        db.session.commit()
    return "yes"
