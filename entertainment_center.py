import media
import fresh_tomatoes

toy_story = media.Movie(
    "Toy Story",
    "http://parkwaynews.net/corral/wp-content/uploads/2014/04/Toy-Story-Poster.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX640_SY720_.jpg",
    "https://www.youtube.com/watch?v=d1_JBMrrYw8")

interstellar = media.Movie(
    "Interstellar",
    "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SX640_SY720_.jpg",
    "https://www.youtube.com/watch?v=0vxOhd4qlnA")

martian = media.Movie(
    "The Martian",
    "https://i.imgur.com/kKS7neK.jpg",
    "https://www.youtube.com/watch?v=ej3ioOneTy8")

"""Creates a list of movies that is fast to the fresh_tomatoes module
   to generate the HTML page"""
movies = [toy_story, avatar, interstellar, martian]
fresh_tomatoes.open_movies_page(movies)
