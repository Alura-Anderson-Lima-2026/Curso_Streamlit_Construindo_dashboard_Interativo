import streamlit as st 
import pandas as pd
import requests
import plotly.express as px


st.title('Dashboard Vendas')

url = "https://labdados.com/produtos"
response = requests.get(url)
dados = pd.DataFrame.from_dict(response.json())


dadoss = pd.read_csv("dados.csv") 


st.dataframe(dadoss)