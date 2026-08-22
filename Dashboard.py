import streamlit as st
from utils.metricas import metricas 
from utils.tabelas import dataframe 
from database.import_requests import dados_requests 


st.set_page_config(
    page_icon="",
    page_title="Vendas",
    layout="wide"
)


st.title('Dashboard Vendas')

# Função de Métricas
metricas()    
# Função de Tabela > DataFrame    
#dataframe()

st.divider()
 
 