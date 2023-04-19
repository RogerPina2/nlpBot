import json

from nltk.corpus import wordnet

from .variables import *

def wn_search(query_word):
    indice = dict()
    with open(INVERSE_INDEX_DB, encoding='utf-8') as file:
        indice = json.load(file)

    synsets = wordnet.synsets(query_word, lang='por')
    if not synsets:
        return None, None

    query_synset = synsets[0]

    max_similarity = 0
    best_match = None
    for word in indice:
        word_synsets = wordnet.synsets(word, lang='por')
        if not word_synsets:
            continue
        
        for word_syn in word_synsets:
            word_syn_similarity = query_synset.wup_similarity(word_syn)
            if word_syn_similarity > max_similarity:
                max_similarity = word_syn_similarity
                best_match = word

    if not best_match:
        return None, None

    return best_match, sorted(indice[best_match], key=lambda x: indice[best_match][x], reverse=True)[0]

#print(wn_search('junto'))