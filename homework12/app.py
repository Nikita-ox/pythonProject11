from flask import Flask, send_from_directory

from flask import Flask, request, render_template

# Импортируем блюпринты из их пакетов
from constant import IMAGES_FOLDER
from main.main_views import profile_blueprint
from loader.loader_views import catalog_blueprint

app = Flask(__name__)

# Регистрируем первый блюпринт
app.register_blueprint(profile_blueprint)
# И второй тоже регистрируем
app.register_blueprint(catalog_blueprint)


@app.route(f'/upload/<path:path>/')
def img_dir(path):
    return send_from_directory(IMAGES_FOLDER, path)


if __name__ == "__main__":
    app.run(debug=True)

