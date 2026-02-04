import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
from datetime import datetime


# Lê o arquivo de vendas. Ajuste o nome das colunas ou o caminho se necessário.
df = pd.read_csv("../vendas.csv", parse_dates=["dados"])

# Análises iniciais do DataFrame
buffer_info = StringIO()
df.info(buf=buffer_info)
info_text = buffer_info.getvalue()

head_text = df.head().to_string()
describe_text = df.describe().to_string()
nulls_text = df.isnull().sum().to_string()
columns_text = df.columns.to_list()
shape_text = str(df.shape)

print(head_text)
print(info_text)
print(describe_text)
print(nulls_text)
print(columns_text)
print(shape_text)

# Cria a coluna de mês a partir da coluna de data
df["mes"] = df["dados"].dt.to_period("M")

# Vendas (quantidade) por mês
vendas_por_mes = df.groupby("mes")["quantidade"].sum()
print("Vendas por mês (unidades):")
print(vendas_por_mes)

# Calcula a receita (quantidade * preço)
df["receita"] = df["quantidade"] * df["preço"]

# Vendas agregadas por produto
vendas_prod = df.groupby("produto").agg(
    quantidade_total=("quantidade", "sum"),
    receita_total=("receita", "sum"),
)

# Produto mais vendido em unidades
mais_vendido = vendas_prod["quantidade_total"].idxmax()

# Produto com maior receita
mais_receita = vendas_prod["receita_total"].idxmax()

texto_mais_vendido = (
    f"Produto mais vendido em unidades: {mais_vendido} "
    f"(total: {vendas_prod.loc[mais_vendido, 'quantidade_total']})"
)
texto_mais_receita = (
    f"Produto com maior receita: {mais_receita} "
    f"(total: {vendas_prod.loc[mais_receita, 'receita_total']:.2f} €)"
)

print(texto_mais_vendido)
print(texto_mais_receita)

# ----- Gráficos -----
vendas_por_mes.index = vendas_por_mes.index.astype(str)

plt.figure(figsize=(6, 4))
vendas_por_mes.plot(kind="bar")
plt.title("Vendas por mês (unidades)")
plt.xlabel("Mês")
plt.ylabel("Vendas (unidades)")
plt.tight_layout()
plt.savefig("vendas_por_mes.png")
plt.close()

top5 = vendas_prod.nlargest(5, "receita_total")

plt.figure(figsize=(6, 4))
plt.bar(top5.index, top5["receita_total"])
plt.title("Top 5 produtos por receita")
plt.ylabel("Receita (€)")
plt.xlabel("Produto")
plt.tight_layout()
plt.savefig("top5_produtos.png")
plt.close()

# ----- Relatórios em TXT e HTML -----
agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

relatorio_txt = f"""
RELATÓRIO DE VENDAS
Gerado em: {agora}

=== Informações gerais do DataFrame ===
Colunas: {columns_text}
Dimensões (linhas, colunas): {shape_text}

=== Primeiras linhas ===
{head_text}

=== Info ===
{info_text}

=== Estatísticas descritivas ===
{describe_text}

=== Valores nulos por coluna ===
{nulls_text}

=== Vendas por mês (unidades) ===
{vendas_por_mes.to_string()}

=== Vendas por produto ===
{vendas_prod.to_string()}

{texto_mais_vendido}
{texto_mais_receita}
"""

with open("relatorio_vendas.txt", "w", encoding="utf-8") as f:
    f.write(relatorio_txt)
