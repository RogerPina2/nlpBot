import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

base_url = 'https://br1.api.riotgames.com/' 
api_key_url = f'?api_key={API_KEY}'

from . import summoner
from . import champion_mastery