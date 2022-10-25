# TODO: Feature 1
from typing_extensions import assert_type
from src.repositories.movie_repository import get_movie_repository
movie_repository = get_movie_repository()

#test unit given, make a random array add a movie and it should match
def test_movie_name_similar():
    movie_repository.create_movie("hhh", "h", 4)
    assert movie_repository[0].title == "hhh"
def test_movie_in_list():
    movie_repository.create_movie("aaa", "a", 4)
    movie_repository.create_movie("bbb", "b", 3)
    movie_repository.create_movie("ccc", "c", 2)
    movies = movie_repository.get_all_movies()
    assert movies[1].title == "aaa"

#test for if there are no movies displayed:
#assert movie_repository[0].title == ""