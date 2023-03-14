import os
import json
import requests
from dotenv import load_dotenv

from . import summoner

load_dotenv()
API_KEY = os.getenv('API_KEY')

base_url = 'https://br1.api.riotgames.com/' 
api_key_url = f'?api_key={API_KEY}'


def get_total_champion_mastery(summonerName: str) -> int:
    summonerId = summoner.get_summonerID_by_summonerName(summonerName)

    r = requests.get(base_url + f'lol/champion-mastery/v4/scores/by-summoner/{summonerId}' + api_key_url)
    data = r.json()

    return data

def get_top_n_champions_mastery(summonerName: str, n: int=3) -> int:
    summonerId = summoner.get_summonerID_by_summonerName(summonerName)

    url = base_url + f'lol/champion-mastery/v4/champion-masteries/by-summoner/{summonerId}/top?count={n}&' + api_key_url[1:]
    r = requests.get(url)
    data = r.json()

    return data

    