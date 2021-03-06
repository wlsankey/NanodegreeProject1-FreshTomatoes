import webbrowser


class Movie():

	"""
	Movies needs to store the following data points:
	-title
	-youtube trailer
	-Storyline
	-poster image
	-review	
	"""

	 #__init__ function establishes class object for storing all movies with common attributes title, trailer, poster, and storyline
	def __init__(self, movie_title, trailer_youtube_url, image_url, storyline):
		self.title = movie_title
		self.trailer_youtube_url = trailer_youtube_url
		self.poster_image_url = image_url
		self.storyline = storyline
		#self.review = review
	
	#show_trailer function opens the Movie youtube link in the default web browser."""
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

	
	
