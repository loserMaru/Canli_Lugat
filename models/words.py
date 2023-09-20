from extensions import db


class Word(db.Model):
    __tablename__ = 'words'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    word = db.Column(db.String(255), nullable=False)
    word_formatted = db.Column(db.String(255), nullable=False)
    word_latin = db.Column(db.String(255), nullable=False)
    word_latin_formatted = db.Column(db.String(255), nullable=False)
    translation = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.TIMESTAMP, nullable=True)
    updated_at = db.Column(db.TIMESTAMP, nullable=True)
    status = db.Column(db.Integer, default=0, nullable=False)
    language_id = db.Column(db.Integer, nullable=False)
    targetLanguage_id = db.Column(db.Integer, nullable=False)