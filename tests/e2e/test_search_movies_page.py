# TODO: Feature 3
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie
from app import movie_repository

def test_create_search_movies_page(test_app: FlaskClient):
    response = test_app.get('/movies/search')
    response_data = response.data
    assert b'<h1 class="mb-5">Search Movie Ratings</h1>' in response_data
    assert b'<p class="mb-3">Search for a movie rating below</p>' in response_data
    
def test_search_movie(test_app: FlaskClient):
    movie_repository.create_movie('Star Wars', 'George Lucas', 1)
    
    response = test_app.get('/movies/search', data={
        "moviesearch": "Star Wars"})
    response_data = response.data
    
    assert b'<p>1/5 for movie Star Wars</p>' in response_data
    
def test_search_movie_fail(test_app: FlaskClient):
    movie_repository.create_movie('Star Wars', 'George Lucas', 1)
    
    response = test_app.get('/movies/search', data={
        "moviesearch": ""})
    response_data = response.data
    
    assert b'<div class="text-bg-danger p-3">Wrong input provided.</div>' in response_data