import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
from datetime import datetime

st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

st.title("📊 Dashboard de Vendas")

# Upload do CSV
arquivo = st.file_uploader("Envie o arquivo vendas.csv", type="csv")

if arquivo:

    df = pd.read_csv(arquivo, parse_dates=["dados"])

    st.subheader("📄 Prévia dos dados")
    st.dataframe(df.head())

    # Info dataframe
    buffer_info = StringIO()
    df.info(buf=buffer_info)
    info_text = buffer_info.getvalue()

    st.subheader("ℹ️ Informações gerais")
    st.text(info_text)

    st.subheader("📈 Estatísticas descritivas")
    st.dataframe(df.describe())

    st.subheader("❗ Valores nulos")
    st.write(df.isnull().sum())

    # Cria coluna mês
    df["mes"] = df["dados"].dt.to_period("M")

    # Receita
    df["receita"] = df["quantidade"] * df["preço"]

    # Vendas por mês
    vendas_por_mes = df.groupby("mes")["quantidade"].sum()
    vendas_por_mes.index = vendas_por_mes.index.astype(str)

    # Vendas por produto
    vendas_prod = df.groupby("produto").agg(
        quantidade_total=("quantidade", "sum"),
        receita_total=("receita", "sum"),
    )

    # KPIs
    mais_vendido = vendas_prod["quantidade_total"].idxmax()
    mais_receita = vendas_prod["receita_total"].idxmax()

    col1, col2 = st.columns(2)

    col1.metric(
        "🏆 Produto mais vendido",
        mais_vendido,
        f"{vendas_prod.loc[mais_vendido, 'quantidade_total']} unidades"
    )

    col2.metric(
        "💰 Maior receita",
        mais_receita,
        f"€ {vendas_prod.loc[mais_receita, 'receita_total']:.2f}"
    )

    # ----- GRÁFICO 1 -----
    st.subheader("📊 Vendas por mês")

    fig1 = plt.figure()
    vendas_por_mes.plot(kind="bar")
    plt.xlabel("Mês")
    plt.ylabel("Unidades")
    plt.tight_layout()

    st.pyplot(fig1)

    # ----- GRÁFICO 2 -----
    st.subhead


