from api import create_app
from api.models import Content
import psycopg2
import pytest 
import json

# Scope = module means it will only run once per file
@pytest.fixture(scope='module')
def app():
    flask_app = create_app('movies_test', 'param')
    
    with flask_app.app_context():
        conn = psycopg2.connect(database='movies_test', user='param')
        cursor = conn.cursor()
        query = """INSERT INTO content (id, netflix_id, title, type, description, release_year, age_certification, runtime, imdb_id, imdb_score, imdb_votes) VALUES (%s, %s, %s, %s,%s, %s,%s, %s,%s, %s, %s)"""
        data = (1, 'tm84618','Taxi Driver','MOVIE','A mentally unstable Vietnam War veteran works as a night-time taxi driver in New York City where the perceived decadence and sleaze feed his urge for violent action, attempting to save a preadolescent prostitute in the process.',1976,'R',113,'tt0075314',8.3,795222.0)
        cursor.execute(query, data)
        conn.commit()
        cursor.close()
    
    yield flask_app

    with flask_app.app_context():
        conn = psycopg2.connect(database='movies_test', user='param')
        cursor = conn.cursor()
        query = """DELETE FROM content WHERE id = 1"""
        cursor.execute(query)
        conn.commit()
        cursor.close()

@pytest.fixture
def client(app):
    """A test client for our app"""
    return app.test_client()

def test_root_url(app, client):
    response = client.get('/')
    assert b'This is the home page' in response.data


def test_content_list(app, client):
    response = client.get('/content/')
    # breakpoint()
    json_response = json.loads(response.data)

    assert len(json_response) == 1
    assert json_response[0]['title'] == 'Taxi Driver'

def test_content_by_type(app, client):
    response = client.get('/content/type/movie')
    json_response = json.loads(response.data)

    assert len(json_response) == 1

def test_content_by_release_year(app, client):
    response = client.get('/content/release-year/1976')
    json_response = json.loads(response.data)

    assert len(json_response) == 1
    assert json_response[0]['title'] == 'Taxi Driver'