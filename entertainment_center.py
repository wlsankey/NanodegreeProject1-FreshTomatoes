import media
import fresh_tomatoes

#EXAMPLE DATA used to populate movie site
#Each object below is based on the Movie class and its inheritances-- in a more sophisticated application convert these objects to database rows

toy_story = media.Movie(
	"Toy Story", 
	"http://youtu.be/KYz2wyBy3kc", 
	"http://2.bp.blogspot.com/_IYPZY2FVRrw/TPlwzrVFMbI/AAAAAAAAAJQ/155KF1TnSjs/s1600/Toy-Story-DVD95.jpg",
	"A story of a boy and his toys that come to life."
	)

avatar = media.Movie(
	"Avatar",
	"https://www.youtube.com/watch?v=cRdxXPV9GNQ",
	"http://meefland.webs.com/photos/Avatar/avatar%20cover.jpg",
	"A marine on an alien planet."
	)

matrix = media.Movie(
	"The Matrix",
	"https://www.youtube.com/watch?v=m8e-FF8MsqU",
	"http://moeatthemovies.files.wordpress.com/2012/10/wpid-photo-oct-21-2012-809-pm.jpg",
	"A dystopian thriller where humankind unwittingly lives in a computer construct."
	)

#TESTING CODE ONLY BELOW:
#print toy_story.storyline
#print avatar.storyline
#matrix.show_trailer()



#Store movie objects into a list for retrival from open_movies function
movies = [toy_story, avatar, matrix]
fresh_tomatoes.open_movies_page(movies)