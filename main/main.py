from flask import Blueprint, render_template, request
from functions import load_data_json, remove_from_string, search_posts
import logging

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename="basic.log", level=logging.INFO)


@main_blueprint.route('/')
def page_index():
    return render_template('index.html')


@main_blueprint.route('/search')
def search_tag():
    logging.info("Пользователь выполнил поиск")
    search_word = request.args['s']
    if search_word:
        posts = search_posts(load_data_json("posts.json"), search_word)
        return render_template('post_list.html', items=posts, search_word=search_word)
    else:
        return 'Вы не ввели слово для поиска'