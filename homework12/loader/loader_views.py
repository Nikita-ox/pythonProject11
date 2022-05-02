from flask import Blueprint, request, render_template
import logging
import json
from constant import ALLOWED_IMG_EXTENSIONS
from constant import IMAGES_FOLDER

menu = [{'name': 'Главная', 'url': '/'}]

# Включаем логирование
logging.basicConfig(encoding='utf-8', level=logging.INFO)

# Затем создаем новый блюпринт, выбираем для него имя
catalog_blueprint = Blueprint('catalog_blueprint', __name__, template_folder='templates')

from flask import render_template


@catalog_blueprint.route('/post/')
def page_form():
    return render_template('post_form.html')


@catalog_blueprint.route('/upload/', methods=['POST'])
def page_upload():
    if request.method == 'POST':
        name = request.form['picture']
    picture = request.files.get("picture")
    filename = picture.filename
    extension = filename.split(".")[-1]
    if extension in ALLOWED_IMG_EXTENSIONS:
        picture.save(f"./uploads/images{filename}")
        return render_template('post_uploaded.html', picture=f'/upload/images{filename}', filename=filename, menu=menu, name=name)

    else:
        return f"Тип файлов {extension} не поддерживается"
