import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from minio import Minio
from io import BytesIO

minio_client = Minio(
    "localhost:9001",  # Endereço do seu MinIO (por exemplo, 'localhost:9000')
    access_key="minioadmin",    # Sua chave de acesso
    secret_key="minioadmin",    # Sua chave secreta
    secure=False                    # Se estiver usando HTTPS, coloque como True
)

# Nome do bucket e do arquivo CSV
bucket_name = "microdados-silver"
csv_file_name = "microdados_ENEM"

# Função para obter o arquivo CSV do MinIO
def get_csv_from_minio(bucket_name, file_name):
    # Baixar o arquivo diretamente para um buffer em memória
    data = minio_client.get_object(bucket_name, file_name)
    file_data = BytesIO(data.read())
    
    # Ler o CSV diretamente no pandas
    df = pd.read_csv(file_data)
    return df

# Carregar o CSV do MinIO
df = get_csv_from_minio(bucket_name, csv_file_name)

# Mostrar os dados no Streamlit
st.write(df.head())

st.title("Dashboard ENEM")

