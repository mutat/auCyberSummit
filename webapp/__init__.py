from flask import Flask

#from models import db
from controllers.main import main_blueprint

def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)

    #db.init_app(app)

    app.register_blueprint(main_blueprint)

    return app
