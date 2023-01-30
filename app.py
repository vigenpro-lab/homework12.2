from flask import Blueprint, request, render_template, Flask
from function import *
from json import JSONDecodeError
import logging


app = Flask(__name__)

app_blueprint = Blueprint('main_blueprint', __name__)


@app_blueprint.route('/')
def main_page():
    logging.info('Ладно')
    return render_template('index.html')


@app_blueprint.route('/search')
def search_page():
    s = request.args.get('s')
    posts = search_key(s)
    logging.info('он что-то ищет...')
    return render_template('post_list.html', posts=posts, s=s)

app.run()