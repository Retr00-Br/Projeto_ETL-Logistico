import requests
from bs4 import BeautifulSoup

def extrair_origens():
    url = "https://pt.wikipedia.org/wiki/Lista_de_portos_do_Brasil"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        cidades = []
        for linha in soup.find_all('tr'):
            colunas = linha.find_all('td')
            if colunas:
                nome_porto = colunas[0].get_text(strip=True)
                if len(nome_porto) > 3:
                    cidades.append(nome_porto)
        return list(set(cidades))
    except Exception as e:
        print(f"Erro na extração: {e}")
        return []

if __name__ == "__main__":
    lista = extrair_origens()
    print(f"Extraídas {len(lista)} origens logísticas!")
    print(lista[:5])
