import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.transfermarkt.com.br/cr-flamengo/kader/verein/614/saison_id/2025/plus/1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

html = requests.get(url, headers = headers).text

soup = BeautifulSoup(html, 'lxml')

tabela = soup.find("table", class_="items")
"""thead = tabela.find("thead")

ths = thead.find_all("th")

titulos = [th.get_text(strip=True) 
           for th in ths]
"""

ths = tabela.find("thead").find_all("th")

titulos = [
    th.get_text("", strip=True) 
    for th in ths
]


trs = tabela.find('tbody').find_all("tr", recursive=False)

dados = []
nomes = []
posicoes = []

for tr in trs:
    tds = tr.find_all("td", recursive=False)

    #Para pegar o texto "limpo" de cada coluna

    linha = [
        td.get_text(" ", strip=True) 
        for td in tds
    ]

    dados.append(linha)

    #Extraindo nome e Posição da coluna Jogadores 

    nome_posicao = tds[1] #Colunas Jogadores

    nome_tag = nome_posicao.select_one("td.hauptlink a")
    nome = nome_tag.get_text(strip=True) if nome_tag else None
    
    linhas_inline = nome_posicao.select("table.inline-table tr")
    posicao = linhas_inline[1].get_text(" ",strip=True) if len(linhas_inline) > 1 else None

    nomes.append(nome)
    posicoes.append(posicao)
    

df = pd.DataFrame(dados, columns=titulos)

df["Idade"] = df["Nasc./Idade"].str.extract(r"\((\d+)\)").astype(int)
df["Nome"] = nomes
df["Posição"] = posicoes

df["Altura"] = (

    df["Altura"].str.replace("m", "", regex=False)
    .str.replace(",",".",regex=False)    
)

df["Altura"] = pd.to_numeric(df["Altura"], errors="coerce")


df["Nasc./Idade"] = df["Nasc./Idade"].str.extract(r"(\d{2}/\d{2}/\d{4})")

df = df.rename(columns={
    "#": "Número",
    "Nasc./Idade": "Data de Nasc.",
    "Nac.": "Nacionalidade",
    "Pé": "Pé Dominante",
    "No time desde": "No Time Desde",
    "Anterior": "Clube Anterior",
    "Contrato": "Contrato Até",
    "Valor de mercado": "Valor Mercado(Euro)"
})


ordem = ["Número", "Nome", "Posição", "Idade", "Data de Nasc.", "Nacionalidade", "Altura", "Pé Dominante",
         "No Time Desde", "Clube Anterior", "Contrato Até", "Valor Mercado(Euro)"]

df = df[ordem]


print(df.head())
