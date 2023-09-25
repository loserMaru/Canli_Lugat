from extensions import db
from models import Word, Page


def initialize_database(app):
    with app.app_context():
        db.create_all()
