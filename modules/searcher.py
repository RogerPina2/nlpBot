import json
import pandas as pd
from .variables import INVERSE_INDEX_DB, DATABASE_PATH

def buscar(palavras, indice):
    assert type(palavras)==list

    resultado = dict()
    for p in palavras:
        if p in indice.keys():
            for documento in indice[p].keys():
                if documento not in resultado.keys():
                    resultado[documento] = indice[p][documento]
                else:
                    resultado[documento] += indice[p][documento]
                    
    return resultado

# 2. Escreva uma função que ordena o resultado e retorna apenas N documentos mais relevantes para sua busca.
def n_relevantes(resultado, n):
    return sorted(resultado.items(), key=lambda x: x[1], reverse=True)[:n]

# 3. Incremente sua biblioteca de forma que ela passe a receber uma string como entrada (representando a query) e retorne 
# os N documentos mais relevantes (N pode ser definido arbitrariamente).
def n_relevantes_query(query, indice, n=2):
    palavras = query.split()
    busca = buscar(palavras, indice)
    rel = n_relevantes(busca, n)
    return rel

def query(query, th=0):

    indice = dict()
    with open(INVERSE_INDEX_DB, encoding='utf-8') as file:
        indice = json.load(file)

    result = n_relevantes_query(query, indice, n=5)
    
    res = sorted(result, key=lambda x: x[1], reverse=True)
    
    df = pd.read_csv('./data/database.csv')
    
    for r in res:
        _score = df[df['url'] == r[0]]['sentiment'].values[0]
        if _score >= th:
            return r

    return (False, False)

#print(query('junto'))
