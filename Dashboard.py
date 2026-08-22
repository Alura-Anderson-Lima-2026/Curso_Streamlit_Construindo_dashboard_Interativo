import streamlit as st 
import pandas as pd
import requests
import plotly.express as px
from formacao.formata_numeros import formatar_valor
from formacao.formata_numeros import formatar_quantidade

st.set_page_config(
    page_icon="",
    page_title="Vendas",
    layout="wide"
)


st.title('Dashboard Vendas')

url = "https://labdados.com/produtos"
response = requests.get(url)
dados = pd.DataFrame.from_dict(response.json())

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.metric(
        'Receita',
        formatar_valor(dados['Preço'].sum())
    )

with col2:
    
    st.metric(
        'Quantidade',
        formatar_quantidade(dados.shape[0])
    )
    


st.divider()

st.dataframe(dados.head())