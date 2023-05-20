CREATE TABLE movie (
    movie_id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_date DATE
);

CREATE TABLE imdb (
    imdb_id VARCHAR(255) PRIMARY KEY,
    movie_id INTEGER REFERENCES movie(movie_id)
);
