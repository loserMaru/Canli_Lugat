import re

from flask import Blueprint, render_template

from models.words import Word

home_bp = Blueprint('home', __name__, template_folder='templates')


@home_bp.route('/')
def index():
    book = """Макаронлар, лезетли! малинаны. марлядан мархагъа мансурлы макъас одфоывд машалла, лаборантлыкъ! лагъабы"""
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
    translations = [[] for _ in range(len(words))]

    for i, word in enumerate(words):
        db_words = Word.get_word_from_db(word)
        print(db_words)
        if db_words.count() == 0:
            for suffix in ["дан", "тан", "лар", "лер", "гъа", "къа", "лы", "ли", "ны", "ни", "макъ", "мек", "гъы",
                           "къ"]:
                if word.endswith(suffix):
                    inf = word[:-len(suffix)]
                    db_words = Word.get_word_by_infinitive(inf)
                    break
            else:
                continue

        for db_word in db_words:
            translations[i].append([db_word.word, db_word.translation])

    return render_template('index.html', translations=translations, words=book_words)
