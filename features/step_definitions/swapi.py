import requests

from pytest_bdd import scenarios, given, then, parsers, when

scenarios('')


@when('I am making request I am getting right name, birth_year and, and status_code')
def validate_people(_base_url, name, birth_year, url, status_code):
    r=requests.get(f"{_base_url}{url}")
    j=r.json()
    assert int(status_code) == r.status_code,\
        f'actual status code is {r.status_code} and expected is {status_code}'
    assert name == j["name"],\
        f'actual name is {j["name"]} and expected is {name}'
    assert birth_year == j["birth_year"],\
        f'actual birth_year is {j["birth_year"]} and expected is {birth_year}'


@when(parsers.parse('I request for planet number "{NUM}"'))
def get_planet_num(NUM):
    global num
    num=int(NUM)


@then(parsers.parse('I getting planet name "{NAME}"'))
def validate_planet_name(_base_url, NAME):
    r=requests.get(f"{_base_url}planets/{num}/")
    j=r.json()
    assert NAME == j["name"]
    f'actual name of planet is {j["name"]} and expected is {NAME}'
