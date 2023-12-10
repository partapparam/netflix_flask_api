DROP TABLE IF EXISTS content;

CREATE TABLE IF NOT EXISTS content (
    id serial PRIMARY KEY,
    netflix_id VARCHAR(255) UNIQUE,
    title VARCHAR(255),
    type VARCHAR(32),
    description TEXT,
    release_year INT,
    age_certification VARCHAR(4),
    runtime INT,
    imdb_id VARCHAR(32) UNIQUE,
    imdb_score NUMERIC(3, 1),
    imdb_votes NUMERIC(9, 1)
)