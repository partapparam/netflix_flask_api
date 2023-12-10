from flask import Flask
import psycopg2
from api.models import Content


def create_app(database, user):
    app = Flask(__name__)

    app.config.from_mapping(DATABASE=database, USER=user)

    @app.route('/')
    def content_list():
        query = 'SELECT * FROM content LIMIT 10;'
        conn = psycopg2.connect(database=app.config['database'], user=app.config['user'])
        cursor = conn.cursor()
        cursor.execute(query)
        content = cursor.fetchall()
        content_objs = [Content(row).__dict__ for row in content]
        return content_objs
    

    return app
