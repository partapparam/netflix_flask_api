from flask import Flask
from api.controllers import content_bp


def create_app(database, user):
    app = Flask(__name__)

    # app.config.from_mapping(
    #     DATABASE=database, 
    #     USER=user)
    app.config['DATABASE'] = database
    app.config['USER'] = user
    with app.app_context():
        app.register_blueprint(content_bp, url_prefix='/content')

    return app
