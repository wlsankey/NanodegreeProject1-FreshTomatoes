import webbrowser

class Movie():

	def __init__(self, movie_title, trailer_youtube_url, image_url, storyline):
		self.title = movie_title
		self.trailer_youtube_url = trailer_youtube_url
		self.poster_image_url = image_url
		self.storyline = storyline
		#self.review = review
	
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
	
	
	
"""
Movies needs to store the following data points:
-title
-youtube trailer
-Storyline
-poster image
-review
"""