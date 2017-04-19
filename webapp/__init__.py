from flask import Flask

from models import db
from controllers.main import main_blueprint
from controllers.speaker import speaker_blueprint
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()


def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)

    #initialize add ons
    db.init_app(app)
    bootstrap.init_app(app)

    #Register BluePrints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(speaker_blueprint)

    return app
