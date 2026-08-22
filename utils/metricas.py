import streamlit as st
import pandas as pd
from formacao.formata_numeros import formatar_valor
from formacao.formata_numeros import formatar_quantidade
from database.import_requests import dados_requests


# Variável Global > Dados Requests

dados = dados_requests()


def metricas():
    
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
    return metricas     





# with col3:

#     card_kpi(
#         titulo="Faturamento",
#         valor="R$ 125.430,50",
#         delta="▲ 12,5% vs mês anterior",
#         icone="💰",
#         positivo=True
#     )   