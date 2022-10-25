# TODO: Feature 2
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

movie_repos = get_movie_repository()

def test_movie_name():
    movie_repos.create_movie('Star Wars', 'George Lucas', 5)
    starwars = Movie('Star Wars', 'George Lucas', 5)
    assert movie_repos.get_all_movies()[0].title == starwars.title

def test_movie_director():
    movie_repos.create_movie('Star Wars', 'George Lucas', 5)
    starwars = Movie('Star Wars', 'George Lucas', 5)
    assert movie_repos.get_all_movies()[0].director == starwars.director