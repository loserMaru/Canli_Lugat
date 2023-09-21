from extensions import db
from models.words import Word


class Page(db.Model):
    __tablename__ = 'page_words'

    id = db.Column(db.Integer, primary_key=True)
    word_index = db.Column(db.Integer, nullable=False)
    book_page = db.Column(db.Integer, nullable=False)
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'))

    word = db.relationship('Word', backref=db.backref('pages', lazy=True))
