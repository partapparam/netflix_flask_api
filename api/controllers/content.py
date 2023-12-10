from flask import Blueprint, current_app
from api.models import Content
import psycopg2


content_bp = Blueprint(
    # name we want to give our blueprint. Used for internal routing
    'content_bp',
    # name of the Blueprint package, helps locate "root_path"
    __name__,
    ###########
    # optional keyword arguments
    ############
    # template_folder='views',
    # static_folder='static
)

conn = psycopg2.connect(database=current_app.config['DATABASE'], user=current_app.config['USER'])


@content_bp.route('/')
def content_list():
    query = 'SELECT * FROM content LIMIT 10;'
    conn = psycopg2.connect(database=current_app.config['DATABASE'], user=current_app.config['USER'])
    cursor = conn.cursor()
    cursor.execute(query)
    content = cursor.fetchall()
    content_objs = [Content(row).__dict__ for row in content]
    return content_objs

@content_bp.route('/<type>')
def content_by_type(type):
    query = """SELECT * FROM content
            WHERE type = %s"""
    cursor = conn.cursor()
    type = type.upper()
    cursor.execute(query, (type,))
    content = cursor.fetchall()
    content_objs = [Content(row).__dict__ for row in content]
    return content_objs

@content_bp.route('/release-year/<release_year>')
def content_by_release_year(release_year):
    query = """SELECT * FROM content
            WHERE release_year = %s"""
    cursor = conn.cursor()
    cursor.execute(query, (release_year,))
    content = cursor.fetchall()
    content_objs = [Content(row).__dict__ for row in content]
    return content_objs

# return content that has imdb_score greater than
@content_bp.route('/imdb_score/gt/<score>')
def content_imdb_score_gt(score):
    query = """SELECT * FROM content
            WHERE imdb_score > %s"""
    cursor = conn.cursor()
    cursor.execute(query, (score,))
    content = cursor.fetchall()
    content_objs = [Content(row).__dict__ for row in content]
    return content_objs

# return content that has imdb_votes greater than
@content_bp.route('/imdb_votes/gt/<votes_count>')
def content_imdb_votes_gt(votes_count):
    query = """SELECT * FROM content
            WHERE imdb_votes > %s"""
    cursor = conn.cursor()
    cursor.execute(query, (votes_count,))
    content = cursor.fetchall()
    content_objs = [Content(row).__dict__ for row in content]
    return content_objs