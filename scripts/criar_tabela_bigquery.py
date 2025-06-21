from google.cloud import bigquery
import os

def criar_tabela_no_bigquery(tabela_id, caminho_credencial):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = caminho_credencial

    client = bigquery.Client()

    schema = [
        bigquery.SchemaField("data", "TIMESTAMP"),
        bigquery.SchemaField("usd_brl", "FLOAT"),
        bigquery.SchemaField("eur_brl", "FLOAT"),
    ]

    table = bigquery.Table(tabela_id, schema=schema)

    try:
        table = client.create_table(table)  # Tenta criar
        print(f"✅ Tabela criada: {table.full_table_id}")
    except Exception as e:
        print(f"⚠️ Erro ao criar tabela (talvez já exista): {e}")
