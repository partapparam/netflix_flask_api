from flask import Flask
from api.controllers import content_bp
from api.models import Content



def create_app(database, user):
    app = Flask(__name__)
    app.config['DATABASE'] = database
    app.config['USER'] = user

    # Register the routes
    @app.route('/')
    def home():
        return "This is the home page"
    # Routes for Content resource
    app.register_blueprint(content_bp, url_prefix='/content')

    return app
