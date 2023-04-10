import json

from variables import *

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

def query(query):
    indice = dict()
    with open(INVERSE_INDEX_DB, encoding='utf-8') as file:
        indice = json.load(file)

    result = n_relevantes_query(query, indice, n=5)
    
    return result

#print(query('colher frutos'))