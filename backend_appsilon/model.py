from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movie'

    movie_id = Column(Integer, primary_key=True)  # Primary key for the Movie table
    title = Column(String(255))  # Column to store the movie title
    release_date = Column(Date)  # Column to store the movie release date
    imdb = relationship('IMDb', back_populates='movie')  # Relationship between Movie and IMDb tables


class IMDb(Base):
    __tablename__ = 'imdb'

    imdb_id = Column(String(255), primary_key=True)  # Primary key for the IMDb table
    movie_id = Column(Integer, ForeignKey('movie.movie_id'))  # Foreign key referencing Movie table
    movie = relationship('Movie', back_populates='imdb')  # Relationship between IMDb and Movie tables
