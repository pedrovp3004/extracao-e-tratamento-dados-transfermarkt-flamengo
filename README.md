# 📊 Extração e Tratamento de Dados – Transfermarkt (Flamengo 2025)

## 📌 Sobre o Projeto

Este projeto realiza a extração, limpeza e manipulação de dados do elenco do Flamengo (temporada 2025) a partir do site Transfermarkt.

Os dados são obtidos via web scraping utilizando Python, processados com BeautifulSoup e estruturados em um DataFrame com Pandas para posterior análise e integração com ferramentas de Business Intelligence (como Power BI).

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Requests
- BeautifulSoup (lxml parser)
- Pandas
- Regex (re)

---

## 🔎 O que o projeto faz

✔️ Realiza requisição HTTP com headers personalizados  
✔️ Interpreta o HTML da página  
✔️ Extrai informações estruturadas da tabela do elenco  
✔️ Trata dados textuais (regex para idade e data)  
✔️ Converte tipos numéricos (altura)  
✔️ Renomeia e reorganiza colunas  
✔️ Gera um DataFrame pronto para análise  

---

## 📁 Estrutura Final dos Dados

| Coluna | Descrição |
|--------|-----------|
| Número | Número da camisa |
| Nome | Nome do jogador |
| Posição | Posição em campo |
| Idade | Idade atual |
| Data de Nasc. | Data de nascimento |
| Nacionalidade | País |
| Altura | Altura em metros |
| Pé Dominante | Pé preferido |
| No Time Desde | Data de chegada |
| Clube Anterior | Último clube |
| Contrato Até | Data de término do contrato |
| Valor Mercado(Euro) | Valor estimado de mercado |

---

## 📦 Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/seuusuario/extracao-e-tratamento-dados-transfermarkt-flamengo.git
