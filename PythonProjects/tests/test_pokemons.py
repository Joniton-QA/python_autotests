import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7d0a904c191f49c51acb9e449ab78931'
HEADER =  {'Content-Type':'application/json', 'trainer_token': TOKEN }
TRAINER_ID = '24857'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID}) 
    assert response.status_code == 200
   
def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID}) 
    assert response_get.json()["data"][0]["name"] == 'Бульба 2'

@pytest.mark.parametrize('key, value', [('name', 'Бульба 2'), ('trainer_id', TRAINER_ID), ('id','273320')])
def test_parametrize(key,value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value




def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID}) 
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID}) 
    assert response_get.json()["data"][0]["trainer_name"] == 'Prime'