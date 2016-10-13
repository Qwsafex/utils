import sqlalchemy
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base


# DB classes

engine = create_engine('sqlite:///watchlist.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Film(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(Integer)
    director = Column(String)
    actors = Column(String)
    plot = Column(String)
    imdb_rating = Column(Float)

    def __repr__(self):
    	return "{0} ({1}) - IMDB: {2}".format(self.title, self.year, self.imdb_rating)

    def long(self):
    	return "{0}(I) - {1} ({2}) - Director: {3} - Cast: {4}\nPlot: {5}".format(
    		self.imdb_rating, self.title, self.year, self.director, self.actors, self.plot)

Base.metadata.create_all(engine)


def print_db():
    for film in session.query(Film).order_by(Film.imdb_rating.desc()).all():
        print(film)