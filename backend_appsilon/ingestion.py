import json
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Movie, IMDb
from config import DB_URL


def run():
    # Create the database engine and session
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the database tables (if they don't exist)
    Base.metadata.create_all(engine)

    # Open and parse the retrieved JSON data
    with open('data.json', 'r') as file:
        data = json.load(file)

    # Iterate over the parsed data and insert into the database
    for item in data:
        movie = Movie(
            title=item['title'],
            release_date=datetime.strptime(item['release_date'], '%Y-%m-%d').date()
        )
        imdb = IMDb(
            imdb_id=item['imdbId'],
            movie=movie
        )

        session.add(movie)
        session.add(imdb)

    # Commit the changes and close the session
    session.commit()
    session.close()
