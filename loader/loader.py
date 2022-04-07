from flask import Blueprint, render_template, request
from functions import load_data_json, json_dump
import logging

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder="templates")
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
logging.basicConfig(filename="basic.log", level=logging.INFO)


@loader_blueprint.route("/post", methods=["GET", "POST"])
def page_post_form():
    return render_template("post_form.html")


@loader_blueprint.route("/upload", methods=["POST"])
def page_post_upload():
    try:
        content = request.values['content']
        picture = request.files["picture"]
        filename = picture.filename
        extension = filename.split(".")[-1]
        if len(extension) >= 3:
            if extension not in ALLOWED_EXTENSIONS:
                logging.info(f"Попытка загрузить неверный формат файла '{extension}'")
                return f'Файл должен быть формата {", ".join(ALLOWED_EXTENSIONS)}'

        picture.save(f'./uploads/images/{filename}')
        json_dump(load_data_json('posts.json'), {'pic': f'/uploads/images/{filename}', 'content': content})
        return render_template('post_uploaded.html', content=content, picture=f'./uploads/images/{filename}')

    except IsADirectoryError:
        logging.error('Ошибка при загрузке файла')
        return f'Ошибка загрузки поста, загрузите файл'
