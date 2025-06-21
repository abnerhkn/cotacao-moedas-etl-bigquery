

from scripts.coletar_dados import coletar_dados_de_janeiro_ate_hoje
from scripts.criar_tabela_bigquery import criar_tabela_no_bigquery
from scripts.enviar_bigquery import enviar_para_bigquery
from scripts.processar_dados import calcular_media_diaria
from scripts.visualizar_dados import plotar_cotacoes

tabela_id = "local-cedar-463615-g2.cotacoes_moedas.historico"
caminho_credencial = "chave.json"


criar_tabela_no_bigquery(tabela_id, caminho_credencial)

def main():
    df = coletar_dados_de_janeiro_ate_hoje()
    df.to_csv('data/cotacoes.csv', index=False)

    
    enviar_para_bigquery(df, tabela_id, caminho_credencial)

    
    media_usd, media_eur = calcular_media_diaria(df)
    plotar_cotacoes(media_usd, media_eur)

if __name__ == '__main__':
    main()
