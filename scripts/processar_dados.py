import pandas as pd

def carregar_dados(caminho_arquivo):
    df = pd.read_csv(caminho_arquivo)
    df['data'] = pd.to_datetime(df['data'])
    return df

def calcular_media_diaria(df):
    df['data_dia'] = df['data'].dt.date
    media_usd = df.groupby('data_dia')['usd_brl'].mean()
    media_eur = df.groupby('data_dia')['eur_brl'].mean()
    return media_usd, media_eur
