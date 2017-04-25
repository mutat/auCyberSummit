from flask import Flask

from models import db
from controllers.main import main_blueprint
from controllers.speaker import speaker_blueprint
from controllers.agenda import event_blueprint
from controllers.poi import poi_blueprint
from webapp.extensions import bootstrap, bcrypt, login_manager


def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)

    #initialize add ons
    db.init_app(app)
    bootstrap.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    #Register BluePrints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(speaker_blueprint)
    app.register_blueprint(event_blueprint)
    app.register_blueprint(poi_blueprint)

    return app
