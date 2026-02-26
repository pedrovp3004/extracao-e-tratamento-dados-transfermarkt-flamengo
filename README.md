📊 Extração e Tratamento de Dados – Transfermarkt (Flamengo 2025)
📌 Sobre o Projeto

Este projeto realiza a extração, limpeza e transformação de dados do elenco do CR Flamengo (temporada 2025) a partir do site Transfermarkt.

A partir de uma página HTML não estruturada, os dados são coletados via Web Scraping com Python, tratados e estruturados em um DataFrame limpo e organizado, pronto para análise exploratória ou integração com ferramentas de Business Intelligence (como Power BI).

O projeto segue a lógica de um pipeline ETL (Extract → Transform → Load).

🎯 Objetivo Técnico

Extrair dados diretamente do HTML da página

Estruturar informações em formato tabular

Tratar e converter dados textuais em dados estruturados

Padronizar nomes de colunas

Gerar um dataset pronto para análise

🚀 Tecnologias Utilizadas

Python 3.13.2

Requests – Requisições HTTP

BeautifulSoup (lxml parser) – Parsing de HTML

Pandas – Manipulação e transformação de dados

Regex (re) – Extração de padrões textuais

🔎 Pipeline do Projeto

1️⃣ Requisição HTTP com headers personalizados
2️⃣ Parsing do HTML com BeautifulSoup
3️⃣ Extração da tabela principal do elenco
4️⃣ Separação de campos combinados
5️⃣ Limpeza e conversão de dados
6️⃣ Padronização dos nomes das colunas
7️⃣ Estruturação final em DataFrame

🧹 Limpeza e Tratamento dos Dados (Transform)

Durante a extração, algumas colunas vieram com dados combinados ou em formato textual que exigiram tratamento:

🔹 Coluna "Jogadores"

Original: Nome + Posição no mesmo bloco HTML

Tratamento:

Extração do Nome

Criação da coluna Posição

Ajuste da coluna original para conter apenas o nome

🔹 Coluna "Nasc./Idade"

Original: DD/MM/AAAA (idade)

Tratamento:

Extração da idade (valor entre parênteses)

Criação da coluna Idade

Ajuste da coluna original para manter apenas a data de nascimento

🔹 Coluna "Altura"

Original: 1,93m

Tratamento:

Remoção do sufixo m

Conversão para valor numérico (1.93)

Preparação para cálculos futuros

🔹 Padronização de Nomes de Colunas
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
📊 Estrutura Final do Dataset
Coluna	Tipo	Descrição
Número	Int	Número da camisa
Nome	String	Nome do jogador
Posição	String	Posição em campo
Idade	Int	Idade atual
Data de Nasc.	Date	Data de nascimento
Nacionalidade	String	País
Altura	Float	Altura em metros
Pé Dominante	String	Pé preferido
No Time Desde	Date	Data de chegada
Clube Anterior	String	Último clube
Contrato Até	Date	Data de término
Valor Mercado(Euro)	String	Valor estimado
📷 Exemplo de Saída do DataFrame

Abaixo está um recorte do dataset final após o processo de limpeza e transformação:

O dataset final apresenta os dados já tratados, com separação adequada de campos, padronização de colunas e conversão de tipos numéricos, tornando-o pronto para análise exploratória ou integração com ferramentas de BI.

📦 Estrutura do Projeto
extracao-e-tratamento-dados-transfermarkt-flamengo/
│
├── src/
│   └── main.py
│
├── docs/
│   └── preview.png
│
├── outputs/
│
├── requirements.txt
├── .gitignore
└── README.md
📦 Como Executar o Projeto
# Clone o repositório
git clone https://github.com/SEUUSUARIO/extracao-e-tratamento-dados-transfermarkt-flamengo.git

# Acesse a pasta
cd extracao-e-tratamento-dados-transfermarkt-flamengo

# Instale as dependências
pip install -r requirements.txt

# Execute o script
python src/main.py
📈 Possíveis Expansões Futuras

Conversão do valor de mercado para tipo numérico

Exportação automática para CSV/Excel

Criação de dashboard no Power BI

Automatização para múltiplos clubes

Aplicação de Análise Exploratória de Dados (EDA)

👨‍💻 Autor

Pedro Vasconcelos de Pinho
Estudante de Ciência da Computação
Foco em Análise de Dados e Ciência de Dados
