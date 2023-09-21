from flask import Blueprint, render_template

page_bp = Blueprint("page", __name__, template_folder='templates')


@page_bp.route('/page/<int:page_number>')
def page(page_number):
    return render_template('page.html', page_number=page_number)
