from flask import (render_template, Blueprint)

#from webapp.models import db, User

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='../templates/main',
    url_prefix="/"
)


@main_blueprint.route('/')
def home():
    return "Hello World" #render_template('home.html')

