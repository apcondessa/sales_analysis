<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Sales CSV Analysis</title>
</head>

<body>

<h1>Sales Data Analysis</h1>

<p>
This project analyzes a synthetic sales dataset stored in analise.csv.
The purpose is to practice data loading, cleaning, aggregation, and basic exploratory data analysis using Python.
</p>

<hr>

<h2>Dataset Columns</h2>

<ul>
<li>dados: transaction date</li>
<li>produto: product name</li>
<li>quantidade: units sold</li>
<li>preço: unit price</li>
</ul>

<hr>

<h2>Objectives</h2>

<ul>
<li>Calculate total revenue</li>
<li>Identify top selling products</li>
<li>Analyze sales over time</li>
<li>Compute average ticket value</li>
</ul>

<hr>

<h2>Tech Stack</h2>

<ul>
<li>Python</li>
<li>Pandas</li>
<li>Matplotlib (optional)</li>
<li>Jupyter Notebook or VS Code</li>
</ul>

<hr>

<h2>Load the CSV</h2>

<pre>
import pandas as pd

df = pd.read_csv("analise.csv")
df["dados"] = pd.to_datetime(df["dados"])

print(df.head())
</pre>

<hr>

<h2>Key Metrics</h2>

<ul>
<li>Revenue = quantity * price</li>
<li>Revenue by product</li>
<li>Daily sales volume</li>
<li>Average order value</li>
</ul>

<hr>

<h2>Example Aggregation</h2>

<pre>
df["revenue"] = df["quantidade"] * df["preço"]

result = df.groupby("produto")["revenue"].sum()

print(result)
</pre>

<hr>

<h2>Notes</h2>

<ul>
<li>Dataset is synthetic</li>
<li>No real business data</li>
<li>Educational project</li>
<li>Focused on EDA fundamentals</li>
</ul>

<hr>

<h2>Next Steps</h2>

<ul>
<li>Add visualizations</li>
<li>Create dashboards</li>
<li>Perform time series analysis</li>
<li>Export KPIs</li>
</ul>

</body>
</html>


