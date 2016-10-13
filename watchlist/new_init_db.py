import sqlalchemy
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text


# DB classes

engine = create_engine('sqlite:///watchlist.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Film(Base):
    __tablename__ = 'films1'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(Integer)
    director = Column(String)
    actors = Column(String)
    plot = Column(String)
    imdb_rating = Column(Float)
    runtime = Column(Integer)
    genre = Column(String)
    language = Column(String)
    country = Column(String)
    poster = Column(String)
    metascore = Column(Integer)
    imdb_votes = Column(Integer)
    imdb_id = Column(String)
    type = Column(String)


    def __repr__(self):
    	return "{0} ({1}) - IMDB: {2} - Director: {3}".format(self.title, self.year, self.imdb_rating, self.director)

    def long(self):
    	return "{0}(I) - {1} ({2}) - Director: {3} - Cast: {4}\nPlot: {5}".format(
    		self.imdb_rating, self.title, self.year, self.director, self.actors, self.plot)

def print_db():
    for film in session.query(Film).order_by(Film.imdb_rating.desc()).all():
        print(film)

Base.metadata.create_all(engine)

init = False
'''
if init:
    for title, in session.query(Film.title).all():
        print("Processing ", title)
        moviedata = get_moviedata(title)
        film_runtime = ''.join(filter(lambda x: x.isdigit(), moviedata['Runtime']))
        print(film_runtime)
        new_film = Film1(
                    title=moviedata['Title'],
                    year=moviedata['Year'],
                    director=moviedata['Director'],
                    actors=moviedata['Actors'],
                    plot=moviedata['Plot'],
                    imdb_rating=moviedata['imdbRating'],
                    runtime=film_runtime,
                    genre=moviedata['Genre'],
                    language=moviedata['Language'],
                    country=moviedata['Country'],
                    poster=moviedata['Poster'],
                    metascore=moviedata['Metascore'],
                    imdb_votes=moviedata['imdbVotes'],
                    imdb_id=moviedata['imdbID'],
                    type=moviedata['Type'],
                    )
        session.add(new_film)
    session.commit()
'''