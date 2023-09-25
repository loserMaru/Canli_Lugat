from extensions import db


class Page(db.Model):
    __tablename__ = 'words_on_page'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    index = db.Column(db.Integer, nullable=False)
    page = db.Column(db.Integer, nullable=False)
    words_id = db.Column(db.Integer, db.ForeignKey('words.id'), nullable=True)

    word = db.relationship('Word', backref='page', foreign_keys=[words_id])
