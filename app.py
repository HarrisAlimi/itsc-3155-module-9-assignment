from flask import Flask, redirect, render_template, request

from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

app = Flask(__name__)

movie_repository = get_movie_repository()

ratings = []

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', ratings=ratings, list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    print(ratings)
    return render_template('create_movies_form.html', create_rating_active=True)

#@app.post('/movies')
@app.post('/result')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    mname = request.form.get('name', type = str)
    dname = request.form.get('dname', type = str)
    rating = request.form.get('select', type = str)
    
    movie = Movie(mname, dname, rating)
    ratings.append(movie)
    
    return render_template('list_all_movies.html', ratings = ratings)


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    for movie in ratings:
        if movie.title == 'A':
            print(movie)
        
    return render_template('search_movies.html', search_active=True)
