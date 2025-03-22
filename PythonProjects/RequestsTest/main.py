import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7d0a904c191f49c51acb9e449ab78931'
HEADER =  {'Content-Type':'application/json', 'trainer_token': TOKEN }
body_registration =  {
    "trainer_token": TOKEN,
    "email": "joniton_break@mail.ru",
    "password": "Dj4432"
}

body_confirmation = {
    "trainer_token": "abaef4dd01c0e49c51acb9e449ab78931"
}

body_create = {
    "name": "Бульба 2",
    "photo_id": 1
}

body_name = {
    "pokemon_id": "273311",
    "name": "Смена имени",
    "photo_id": -1
}

body_pokeball = {
    "pokemon_id": "273311",
}



'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''


'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation )
print(response_confirmation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)
message = response_create.json()['message']
print(message)

'''response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_name.text)
message = response_name.json()['message']
print(message)'''

'''response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)
message = response_pokeball.json()['message']
print(message)'''