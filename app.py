# app.py (VERSÃO MAIS ROBUSTA)

import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Dashboard de Produção de Petróleo | RJ", page_icon="🇧🇷", layout="wide")

DATA_PATH = os.path.join("data", "producao_rio_de_janeiro.parquet")

@st.cache_data
def carregar_dados():
    if os.path.exists(DATA_PATH):
        return pd.read_parquet(DATA_PATH)
    return None

df = carregar_dados()

st.title("🇧🇷 Dashboard da Produção de Petróleo no Rio de Janeiro")

# --- INÍCIO DA CORREÇÃO ---
# Verifica se o dataframe está vazio ANTES de tentar criar os filtros
if df is None or df.empty:
    st.error("Nenhum dado encontrado para exibir.")
    st.warning("Por favor, execute o script 'data_processing.py' e verifique se ele encontrou dados para o Rio de Janeiro.")
# --- FIM DA CORREÇÃO ---
else:
    st.markdown("##### Análise da produção de petróleo (em m³) de 1997 a 2025.")
    st.markdown("---")

    st.sidebar.header("Filtros")
    
    anos = sorted(df['ano'].unique())
    ano_selecionado = st.sidebar.slider(
        "Selecione o Ano:",
        min_value=min(anos),
        max_value=max(anos),
        value=(min(anos), max(anos))
    )

    localizacoes = df['localizacao'].unique()
    localizacao_selecionada = st.sidebar.multiselect(
        "Selecione a Localização:",
        options=localizacoes,
        default=localizacoes
    )
    
    df_filtrado = df[
        (df['ano'] >= ano_selecionado[0]) & 
        (df['ano'] <= ano_selecionado[1]) &
        (df['localizacao'].isin(localizacao_selecionada))
    ]

    # Verifica se o dataframe FILTRADO está vazio
    if df_filtrado.empty:
        st.warning("Nenhum dado encontrado para os filtros selecionados.")
    else:
        st.header("Métricas Gerais do Período Selecionado")
        col1, col2, col3 = st.columns(3)
        
        producao_total = df_filtrado['producao_m3'].sum()
        col1.metric("Produção Total (m³)", f"{producao_total:,.0f}")

        media_mensal = df_filtrado.groupby(pd.Grouper(key='data', freq='M'))['producao_m3'].sum().mean()
        col2.metric("Média Mensal (m³)", f"{media_mensal:,.0f}")
        
        pico_producao = df_filtrado.groupby(pd.Grouper(key='data', freq='M'))['producao_m3'].sum().max()
        col3.metric("Pico Mensal (m³)", f"{pico_producao:,.0f}")
        
        st.markdown("---")

        st.header("Visualizações")
        
        st.subheader("Evolução Mensal da Produção de Petróleo (m³)")
        df_temporal = df_filtrado.groupby('data')['producao_m3'].sum().reset_index()
        fig_temporal = px.line(df_temporal, x='data', y='producao_m3', title="Produção Mensal", labels={'data': 'Data', 'producao_m3': 'Produção (m³)'})
        st.plotly_chart(fig_temporal, use_container_width=True)

        col_graf1, col_graf2 = st.columns(2)
        with col_graf1:
            st.subheader("Produção Total por Ano")
            df_anual = df_filtrado.groupby('ano')['producao_m3'].sum().reset_index()
            fig_anual = px.bar(df_anual, x='ano', y='producao_m3', title="Produção Anual Acumulada", labels={'ano': 'Ano', 'producao_m3': 'Produção Total (m³)'})
            st.plotly_chart(fig_anual, use_container_width=True)
        with col_graf2:
            st.subheader("Produção por Localização")
            df_localizacao = df_filtrado.groupby('localizacao')['producao_m3'].sum().reset_index()
            fig_localizacao = px.pie(df_localizacao, names='localizacao', values='producao_m3', title="Distribuição da Produção (Mar vs. Terra)", hole=.3)
            st.plotly_chart(fig_localizacao, use_container_width=True)

        st.header("Dados Detalhados")
        st.dataframe(df_filtrado)