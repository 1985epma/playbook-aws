import requests

# Moedas e ativos que queremos verificar
moedas = ['dolar', 'euro', 'libra']
ativos = ['ouro', 'eth', 'btc']

# Fazer uma busca no Google para cada moeda e ativo
for moeda in moedas:
    url = f'https://www.google.com/search?q={moeda}'
    res = requests.get(url)
    if res.status_code == 200:
        start = res.text.find('1 ' + moeda.upper()) + 4
        end = res.text.find(' ', start)
        valor = res.text[start:end]
        print(f'1 {moeda.upper()} = {valor} BRL')

for ativo in ativos:
    url = f'https://www.google.com/search?q={ativo}'
    res = requests.get(url)
    if res.status_code == 200:
        start = res.text.find('1 ' + ativo.upper()) + 4
        end = res.text.find(' ', start)
        valor = res.text[start:end]
        print(f'1 {ativo.upper()} = {valor} USD')

