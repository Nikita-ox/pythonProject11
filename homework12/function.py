import json
from constant import *


#
def load_posts_json(filename=JSON_FILE):
    try:
        file = open(filename, encoding='UTF-8')
        candidates = json.load(file)
        file.close()
        return candidates
    except ValueError:
        return 'Ошибка чтения файла'  # includes simplejson.decoder.JSONDecodeError (согласно стаковерфлоу)
    except FileNotFoundError:
        return 'Ошибка. Файл json не найден'

