import requests

def test_base_url_returns_200(_base_url):
    r=requests.get(_base_url)
    assert 200 == r.status_code

def test_incorrect_base_url_return_error_404(_base_url):
    r = requests.get(f"{_base_url}wrong/url")
    assert 404 == r.status_code

def test_verify_all_available_resources_within_base_url(_base_url):
    r = requests.get(_base_url)
    dict={
    "films": f"{_base_url}films/",
    "people": f"{_base_url}people/",
    "planets": f"{_base_url}planets/",
    "species": f"{_base_url}species/",
    "starships": f"{_base_url}starships/",
    "vehicles": f"{_base_url}vehicles/"}
    assert dict==r.json()

