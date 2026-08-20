import streamlit as st 
import pandas as pd
import requests
import plotly.express as px


st.title('Dashboard Vendas')

url = "https://labdados.com/produtos"
response = requests.get(url)
dados = pd.DataFrame.from_dict(response.json())

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.metric(
        'Receita',
        dados['Preço'].sum()
    )

with col2:
    
    st.metric(
        'Quantidade',
        dados.shape[0]
    )

st.divider()

st.dataframe(dados.head())