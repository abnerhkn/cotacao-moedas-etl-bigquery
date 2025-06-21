from google.cloud import bigquery
import os

def enviar_para_bigquery(df, tabela_id, caminho_credencial):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = caminho_credencial

    client = bigquery.Client()

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_APPEND",   
        autodetect=True,
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
    )

    # Salva o DataFrame como CSV temporário
    temp_file = "temp.csv"
    df.to_csv(temp_file, index=False)

    # Envia o CSV para o BigQuery
    with open(temp_file, "rb") as source_file:
        load_job = client.load_table_from_file(
            source_file,
            tabela_id,
            job_config=job_config
        )
        load_job.result()  # Aguarda a conclusão do job

    print(f"✅ Dados enviados com sucesso para {tabela_id}")
    os.remove(temp_file)