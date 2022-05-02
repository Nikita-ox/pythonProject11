from flask import Blueprint, request
# Импортируем функции
from function import load_posts_json
# Импортируем логирование
import logging
from flask import Blueprint, request, render_template
import json


# print(post_list)
# Затем создаем новый блюпринт, выбираем для него имя
profile_blueprint = Blueprint('profile_blueprint', __name__, template_folder='templates')
candidates = load_posts_json()

@profile_blueprint.route('/')
def home_page():
    return render_template('index.html')


@profile_blueprint.route('/search/')
def search_posts():
    s = request.args['s']
    return render_template('post_list.html', s=s, r=candidates)


