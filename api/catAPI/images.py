import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

cat_base_url = 'https://api.thecatapi.com/v1/' 
dog_base_url = 'https://api.thedogapi.com/v1/' 
api_key_url = f'?api_key={api_key}'

def get_random_image(pet='cat'):

    if pet == 'cat':
        url = f'{cat_base_url}images/search{api_key_url}'
    elif pet == 'dog':
        url = f'{dog_base_url}images/search{api_key_url}'

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception('Failed to get')
