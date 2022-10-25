# TODO: Feature 3
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

movie_repos = get_movie_repository()

def test_movie_by_title():
    movie_repos.create_movie('Star Wars', 'George Lucas', 5)
    assert type(movie_repos.get_movie_by_title('Star Wars')) == Movie
    
def test_movie_by_title_failure():
    movie_repos.create_movie('Star Wars', 'George Lucas', 5)
    assert movie_repos.get_movie_by_title('Monkey') == None