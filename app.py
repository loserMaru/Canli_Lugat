import re

from flask import Flask, render_template

from config import Config
from extensions.database_extension import db
from models.words import Word


def create_app():
    # App configs
    app = Flask(__name__)
    app.config.from_object(Config)
    # Inits
    db.init_app(app)
    return app


app = create_app()


@app.route('/')
def index():
    book = """Макаронлар, лезетли! малинаны. марлядан мархагъа мансурлы макъас одфоывд"""
    words_and_punctuation = re.findall(r'\w+|\W+', book)

    counter = 0
    book_words = []
    for item in words_and_punctuation:
        if item.isalpha():
            book_words.append([counter, item])
            counter += 1
        else:
            book_words.append([-1, item.replace(' ', '&nbsp;')])

    print(book_words)

    a = (book
         .replace(',', '')
         .replace('!', '')
         .replace(':', '')
         .replace('.', ''))
    words = a.split()
    translations = {}

    for i, word in enumerate(words):
        db_words = Word.query.filter(Word.word.ilike(f'{word}%'))
        if db_words.count() == 0:
            for suffix in ["дан", "лер", "гъа", "лар", "лы", "ли", "ны", "ни", "макъ", "мек", "къ"]:
                if word.endswith(suffix):
                    inf = word[:-len(suffix)]
                    db_words = Word.query.filter(Word.word.ilike(f'{inf}'))
                    break
            else:
                continue

        for db_word in db_words:
            print(f'{word} => {db_word.word} - {db_word.translation}')
            translations[i] = (db_word.word, db_word.translation)

    return render_template('index.html', translations=translations, words=book_words)


if __name__ == '__main__':
    app.run(debug=True)
