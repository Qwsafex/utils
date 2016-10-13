import json, urllib.request

import init_db

from init_db import Film, session

def add_movie(moviedata, filmlist_file):
	'''
	filmlist_file.write("{0}(I) - {1} ({2}) - Director: {3} - Cast: {4}\nPlot: {5}\n\n".format(
							moviedata['imdbRating'],
							moviedata['Title'],
							moviedata['Year'],
							moviedata['Director'],
							moviedata['Actors'],
							moviedata['Plot']
							))
	'''
	
	new_film = Film(title=moviedata['Title'],
					year=moviedata['Year'],
					director=moviedata['Director'],
					actors=moviedata['Actors'],
					plot=moviedata['Plot'],
					imdb_rating=moviedata['imdbRating'])
	session.add(new_film)
	session.commit()

filmlist = open('gen_filmlist.txt', 'a')

while True:
	raw_title = input("Movie title? ")
	title = raw_title.replace(' ', '+')
	# Download movie data
	data = urllib.request.urlretrieve('http://www.omdbapi.com/?t='+title+'&y=&plot=short&r=json') 
	# Read data to string
	with open(data[0], 'r') as f:
		moviedata = json.loads(f.read());

	if moviedata['Response'] == 'False':
		print('No movie matching "{0}" title found. Try again.'.format(raw_title))
		continue
	print('Did you mean "{0}" ({1})? '.format(moviedata['Title'], moviedata['Year']), end='')
	response = input()
	if response != 'n':
		add_movie(moviedata, filmlist)
		print('Added succesfully.')
		'''
		response = input("Do you want to add more movies? ")
		if response == 'n':
			break
		'''
	else:
		print("You probably mistyped movie title. Try again.")

filmlist.close()
