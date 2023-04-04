import requests
import csv
from bs4 import BeautifulSoup

# Função para adicionar as informações da página ao CSV
def add_to_csv(url, soup):
    try:
        title = soup.find("title").get_text().strip()
        description = soup.find("meta", {"name": "description"})
        if description:
            description = description.get("content").strip()
        else:
            description = ""
        with open("./data/database.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([url, title, description])
    except:
        pass

# Função para verificar se a URL já foi visitada
def is_visited(url):
    with open("./data/database.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if url == row[0]:
                return True
    return False

# Função para fazer o crawling a partir de uma URL
def crawl(url):
    # Verifica se a URL já foi visitada
    if is_visited(url):
        return
    # Faz a requisição HTTP
    response = requests.get(url)
    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Faz o parsing do conteúdo HTML com BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        # Adiciona as informações ao banco de dados em formato CSV
        add_to_csv(url, soup)
        # Busca por links na página e continua o crawling a partir deles
        links = soup.find_all("a")
        for link in links:
            href = link.get("href")
            if href is not None and href.startswith("http"):
                crawl(href)

# Exemplo de uso
crawl("https://www.linkedin.com/")
