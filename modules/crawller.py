import csv
import requests
import numpy as np

from bs4 import BeautifulSoup
from langdetect import detect

from variables import *
from functions import create_inverse_index_dictionary

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

def crawl(url):
    if is_visited(url):
        return

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        text = " ".join([para.get_text() for para in soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6"])])
        word_count = len(text.split())

        if word_count > 100:

            lang = detect(text)
            if lang != 'pt':
                return

            add_to_csv(url, text)

            links = soup.find_all('a')
            for link in links:
                href = link.get('href')
                if href is not None and href.startswith('http'):
                    crawl(href)

            return links
        else:
            pass

#print(crawl('https://g1.globo.com/politica/noticia/2023/04/10/lula-100-dias-colunistas.ghtml'))