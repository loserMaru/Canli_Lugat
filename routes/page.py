from flask import Blueprint, render_template

from extensions import db
from models.page_words import Page
from models.words import Word

page_bp = Blueprint("page", __name__, template_folder='templates')


@page_bp.route('/page/<int:page_number>')
def page(page_number):
    words = 'Макъас мансурлы, миллет, лезетли! лугъат? машалла.'

    return render_template('page.html', page_number=page_number, words=words)