from extensions import db
from models.words import Word


class Page(db.Model):
    __tablename__ = 'words_on_page'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    index = db.Column(db.Integer, nullable=False)
    page = db.Column(db.Integer, nullable=False)
    words_id = db.Column(db.Integer, db.ForeignKey('words.id'))

    word = db.relationship('Word', backref='page', foreign_keys=[words_id])
