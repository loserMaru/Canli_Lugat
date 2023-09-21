import re

from flask import Blueprint, render_template

from models.words import Word

page_bp = Blueprint("page", __name__, template_folder='templates')


@page_bp.route('/page/<int:page_number>')
def page(page_number):
    words = 'Макъас мансурлы, миллет, лезетли! лугъат? машалла.'

    # Разделить текст на слова и знаки препинания
    words_and_punctuation = re.findall(r'\w+|\W+', words)
    print(words_and_punctuation)

    # Подготовить список для хранения данных слов на странице
    words_on_page = []
    translations = {}

    # Итерироваться по словам и знакам препинания, создавая записи для слов
    word_index = 0  # Индекс слова
    for item in words_and_punctuation:
        if item.isalpha():
            words_on_page.append([word_index, item])
            word_index += 1
        else:
            words_on_page.append([-1, item.replace(' ', '&nbsp;')])
    print(words_on_page)

    for index, item in words_on_page:
        if index != -1:
            db_words = Word.query.filter(Word.word.ilike(f'{item}%'))
            if db_words.count() == 0:
                for suffix in ["дан", "тан", "лар", "лер", "гъа", "къа", "лы", "ли", "ны", "ни", "макъ", "мек", "гъы",
                               "къ"]:
                    if item.endswith(suffix):
                        inf = item[:-len(suffix)]
                        db_words = Word.query.filter(Word.word.ilike(f'{inf}'))
                        break
                else:
                    continue

            for db_word in db_words:
                print(f'{item} => {db_word.word} - {db_word.id}')
                translations[index] = (db_word.word, db_word.translation)

    return render_template('page.html', page_number=page_number, words=words_on_page, translations=translations)
