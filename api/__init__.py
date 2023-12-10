from flask import Flask
import psycopg2
from api.models import Content


def create_app(database, user):
    app = Flask(__name__)

    app.config.from_mapping(
        DATABASE=database, 
        USER=user)
    
    conn = psycopg2.connect(database=app.config['DATABASE'], user=app.config['USER'])

    @app.route('/')
    def content_list():
        query = 'SELECT * FROM content LIMIT 10;'
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
    
    @app.route('/release-year/<release_year>')
    def content_by_release_year(release_year):
        query = """SELECT * FROM content
                WHERE release_year = %s"""
        cursor = conn.cursor()
        cursor.execute(query, (release_year,))
        content = cursor.fetchall()
        content_objs = [Content(row).__dict__ for row in content]
        return content_objs
    
    # return content that has imdb_score greater than
    @app.route('/imdb_score/gt/<score>')
    def content_imdb_score_gt(score):
        query = """SELECT * FROM content
                WHERE imdb_score > %s"""
        cursor = conn.cursor()
        cursor.execute(query, (score,))
        content = cursor.fetchall()
        content_objs = [Content(row).__dict__ for row in content]
        return content_objs

    # return content that has imdb_votes greater than
    @app.route('/imdb_votes/gt/<votes_count>')
    def content_imdb_votes_gt(votes_count):
        query = """SELECT * FROM content
                WHERE imdb_votes > %s"""
        cursor = conn.cursor()
        cursor.execute(query, (votes_count,))
        content = cursor.fetchall()
        content_objs = [Content(row).__dict__ for row in content]
        return content_objs
    

    return app
