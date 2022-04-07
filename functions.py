import json
from json import JSONDecodeError


def load_data_json(json_d):
    try:
        with open(f'{json_d}', 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return 'Файл не найден'
    except JSONDecodeError:
        print("Файл не удается преобразовать")


def remove_from_string(string, *symbol):
    for symb in symbol:
        string = string.replace(symb , '')
    return string


def search_posts(data_json, word):
    list_contents = []
    for index in data_json:
        for key, value in index.items():
            if word.lower() in remove_from_string(value.lower(), '!',".",',','-',':').split(' '):
                list_contents.append(index)
    return list_contents


def json_dump(read, data):
    with open('posts.json', "w") as f:
        read.append(data)
        j_s = json.dump(read, f, ensure_ascii=False)

