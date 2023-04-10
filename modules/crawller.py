import csv
import requests
import numpy as np

from bs4 import BeautifulSoup
from langdetect import detect

from .variables import DATABASE_PATH, INVERSE_INDEX_DB
from .functions import create_inverse_index_dictionary

def add_to_csv(url, text):

    create_inverse_index_dictionary(url, text)

    with open(DATABASE_PATH, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([url, text.strip()])

def is_visited(url):
    with open(DATABASE_PATH, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if url == row[0]:
                return True
    return False

def crawl(url, n=20):
    links = [url]
    count = 0
    while count < 20:
        link = links.pop(0)
        
        if is_visited(link):
            if not links:
                return (count, 'is_visited')
            continue
        
        try:
            response = requests.get(link)
        except:
            if not links:
                return (count, 'get')
            continue

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            text = " ".join([para.get_text() for para in soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6"])])
            word_count = len(text.split())

            if word_count > 100:
                lang = detect(text)
                if lang != 'pt':
                    if not links:
                        return (count, 'lang')
                    continue

                add_to_csv(url, text)
                count += 1
                    
                links += [l.get('href') for l in soup.find_all('a') if l.get('href') is not None and l.get('href').startswith('http')]
                
            else:
                if not links:
                    return (count, 'word_count')
                continue
        else:
            if not links:
                return (count, 'status_code')
            continue
            

    return (count, 'ok')

# url = 'https://www.cnnbrasil.com.br/economia/alckmin-vai-presidir-conselhao-da-industria-para-impulsionar-setor/'
# print(crawl(url))