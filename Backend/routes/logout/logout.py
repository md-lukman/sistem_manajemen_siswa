from flask import Blueprint, redirect, url_for, session


logout_bp = Blueprint('logout_bp', __name__, url_prefix = '/logout')

@logout_bp.route('/back')
def logout():
    session.clear()
    return redirect(url_for('login_form'))