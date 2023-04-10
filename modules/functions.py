import csv
import json

from sklearn.feature_extraction.text import TfidfVectorizer

from variables import *

def create_inverse_index_dictionary(url, text):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([text.strip()])
    
    indice = dict()
    with open(INVERSE_INDEX_DB, encoding='utf-8') as file:
        indice = json.load(file)
    
    for word, word_idx in vectorizer.vocabulary_.items():
        if word not in indice:
            indice[word] = {}

        indice[word][url] = tfidf[0, word_idx]

    with open(INVERSE_INDEX_DB, 'w', encoding='utf-8') as json_file:
        json.dump(indice, json_file, indent=4)
        
        