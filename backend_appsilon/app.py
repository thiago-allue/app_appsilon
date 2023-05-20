from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ingestion import run as ingest_data
from model import Movie, IMDb
from retrieve_data import run as retrieve_data
from config import DB_URL

app = Flask(__name__)
CORS(app)


# Endpoint to retrieve movie data from Wikidata and create data.json
@app.route('/retrieve', methods=['GET'])
def retrieve_data_from_wikedata():
    retrieve_data()
    return jsonify({'message': 'Data exported to data.json.'})


# Endpoint to ingest data from data.json into PostgreSQL
@app.route('/ingest', methods=['GET'])
def ingest_data_to_db():
    ingest_data()
    return jsonify({'message': 'Data ingested into PostgreSQL.'})


# Endpoint to load imbds data from PostgreSQL and return as JSON
@app.route('/load_imdbs', methods=['GET'])
def load_imdbs_from_db():
    # Create the database engine and session
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all imdbs and their IMDb information from the database
    imdbs = session.query(IMDb).all()
    imdbs_data = []
    for imdb in imdbs:
        imdb_data = {
            'imdb_id': imdb.imdb_id,
            'movie_id': imdb.movie_id,
        }
        imdbs_data.append(imdb_data)

    # Close the session
    session.close()

    return jsonify(imdbs_data)


# Endpoint to load movies data from PostgreSQL and return as JSON
@app.route('/load_movies', methods=['GET'])
def load_movies_from_db():
    # Create the database engine and session
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all movies and their IMDb information from the database
    movies = session.query(Movie).all()
    movies_data = []
    for movie in movies:
        movie_data = {
            'movie_id': movie.movie_id,
            'title': movie.title,
            'release_date': movie.release_date.strftime('%Y-%m-%d')
        }
        movies_data.append(movie_data)

    # Close the session
    session.close()

    return jsonify(movies_data)


# Endpoint to delete all data from PostgreSQL
@app.route('/delete', methods=['GET'])
def delete_data_data_db():
    # Create the database engine and session
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Delete all data from the Movie and IMDb tables
    session.query(IMDb).delete()
    session.query(Movie).delete()

    # Commit the changes and close the session
    session.commit()
    session.close()

    return jsonify({'message': 'All data deleted from PostgreSQL.'})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
