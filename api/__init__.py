from flask import Flask
import psycopg2
from api.models import Content
from api.controllers import content_bp


def create_app(database, user):
    app = Flask(__name__)

    app.config.from_mapping(
        DATABASE=database, 
        USER=user)
    
    conn = psycopg2.connect(database=app.config['DATABASE'], user=app.config['USER'])

    app.register_blueprint(content_bp, url_prefix='/content')

   
    

    return app
