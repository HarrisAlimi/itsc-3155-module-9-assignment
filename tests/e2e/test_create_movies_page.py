# TODO: Feature 2

from flask.testing import FlaskClient

def test_create_movies_page(test_app: FlaskClient):
    response = test_app.get('/movies/new')
    response_data = response.data
    assert b'<h1 class="mb-5">Create Movie Rating</h1>' in response_data
    assert b'<p class="mb-3">Create a movie rating below</p>' in response_data

def test_create_movies_form(test_app: FlaskClient):
    response = test_app.post('/movies', data={
        "mname": "Star Wars",
        "dname": "George Lucas",
        "rating": 5},
        follow_redirects=True)

    response_data = response.data
    assert b'<th>George Lucas</th>' in response_data


def test_create_movies_bad(test_app:FlaskClient):
    response = test_app.post('/movies', data={
        "mname": None,
        "dname": "George Lucas",
        "rating": 5})
    assert response.status_code == 404

