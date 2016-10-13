import json, urllib.request

import new_init_db

from new_init_db import Film, session

def add_movie(moviedata):	
	film_runtime = ''.join(filter(lambda x: x.isdigit(), moviedata['Runtime']))
	new_film = Film(
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

def get_moviedata(raw_title):
	title = raw_title.replace(' ', '+')
	# Download movie data
	data = urllib.request.urlretrieve('http://www.omdbapi.com/?t='+title+'&y=&plot=short&r=json') 
	# Read data to string
	with open(data[0], 'r') as f:
		moviedata = json.loads(f.read());
	return moviedata

if __name__ == '__main__':
	while True:
		raw_title = input("Movie title? ")

		moviedata = get_moviedata(raw_title)
		if moviedata['Response'] == 'False':
			print('No movie matching "{0}" title found. Try again.'.format(raw_title))
			continue
		print('Did you mean "{0}" ({1})? '.format(moviedata['Title'], moviedata['Year']), end='')
		response = input()
		if response != 'n':
			add_movie(moviedata)
			print('Added succesfully.')
			'''
			response = input("Do you want to add more movies? ")
			if response == 'n':
				break
			'''
		else:
			print("You probably mistyped movie title. Try again.")
