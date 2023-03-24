import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

base_url = 'https://br1.api.riotgames.com/' 
api_key_url = f'?api_key={API_KEY}'

def get_summoner_by_summonerName(summonerName: str) -> json:
    r = requests.get(base_url + f'lol/summoner/v4/summoners/by-name/{summonerName}' + api_key_url)
    data = r.json()
    
    return data

def get_summonerID_by_summonerName(summonerName: str) -> int:
    data = get_summoner_by_summonerName(summonerName)

    return data['id']

def get_summoner_level(summonerName: str) -> int:
    data = get_summoner_by_summonerName(summonerName)

    return data['summonerLevel']