import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

base_url = 'https://api.thecatapi.com/v1/' 
api_key_url = f'?api_key={api_key}'

# from . import summoner
# from . import champion_mastery