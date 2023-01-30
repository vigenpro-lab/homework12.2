from flask import Blueprint, request, render_template
from function import add_post

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='.templates')


@loader_blueprint.route('/post', methods=['GET'])
def post_uploaded():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def post_upload():
    picture = request.files.get("picture")
    if picture:
        content = request.form.get("content")
        picture = request.files.get("picture")
        filename = picture.filename
        picture.save(f'./uploads/images/{filename}')
        link = f'./uploads/images/{filename}'
        post = add_post({"pic": link, "content": content})
        return render_template('post_uploaded.html', path=link, content=content, post=post)
    else:
        return ("Вы не загрузили картинку")
