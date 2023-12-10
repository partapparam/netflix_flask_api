from flask import Flask
import psycopg2
from api.models import Content


def create_app(database, user):
    app = Flask(__name__)

    app.config.from_mapping(
        DATABASE=database, 
        USER=user)
    
    conn = psycopg2.connect(database=app.config['DATABASE'], user=app.config['USER'])
        # cursor = conn.cursor()

    @app.route('/')
    def content_list():
        query = 'SELECT * FROM content LIMIT 10;'
        # conn = psycopg2.connect(database=app.config['DATABASE'], user=app.config['USER'])
        cursor = conn.cursor()
        cursor.execute(query)
        content = cursor.fetchall()
        content_objs = [Content(row).__dict__ for row in content]
        return content_objs
    
    @app.route('/<type>')
    def content_by_type(type):
        query = """SELECT * FROM content
                WHERE type = %s"""
        cursor = conn.cursor()
        type = type.upper()
        cursor.execute(query, (type,))
        content = cursor.fetchall()
        content_objs = [Content(row).__dict__ for row in content]
        return content_objs

    return app
