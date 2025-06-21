import requests
import pandas as pd
from datetime import datetime

def coletar_historico(moeda, dias=150):
    url = f"https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/{dias}"
    response = requests.get(url)
    data = response.json()

    cotacoes = []
    for item in data:
        data_convertida = datetime.fromtimestamp(int(item['timestamp']))
        cotacoes.append({
            'data': data_convertida,
            f'{moeda.lower()}_brl': float(item['bid'])
        })

    return pd.DataFrame(cotacoes)

def coletar_dados_de_janeiro_ate_hoje():
    df_usd = coletar_historico('USD', 150)
    df_eur = coletar_historico('EUR', 150)

    df = pd.merge(df_usd, df_eur, on='data', how='outer').sort_values('data')

    
    df = df[df['data'] >= datetime(2025, 1, 1)]

    return df
