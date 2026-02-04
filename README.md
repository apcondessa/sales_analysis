<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Sales CSV Analysis</title>
</head>

<body>

<h1>Sales Data Analysis</h1>

<p>
This project contains an exploratory analysis of a synthetic sales dataset stored in <strong>analise.csv</strong>.
The goal is to practice data cleaning, aggregation, and basic analytics using Python.
</p>

<hr>

<h2>Dataset Structure</h2>

<table border="1" cellpadding="6">
<tr>
<th>Column</th>
<th>Type</th>
<th>Description</th>
</tr>

<tr>
<td>dados</td>
<td>Date</td>
<td>Transaction date</td>
</tr>

<tr>
<td>produto</td>
<td>String</td>
<td>Product name</td>
</tr>

<tr>
<td>quantidade</td>
<td>Integer</td>
<td>Units sold</td>
</tr>

<tr>
<td>preço</td>
<td>Float</td>
<td>Unit price</td>
</tr>

</table>

<hr>

<h2>Analysis Objectives</h2>

<ul>
<li>Total revenue calculation</li>
<li>Top selling products</li>
<li>Daily sales volume</li>
<li>Average ticket size</li>
</ul>

<hr>

<h2>Technology Stack</h2>

<ul>
<li>Python 3</li>
<li>Pandas</li>
<li>Matplotlib (optional)</li>
<li>Jupyter Notebook or VS Code</li>
</ul>

<hr>

<h2>Load Dataset</h2>

<pre>
import pandas as pd
df = pd.read_csv("analise.csv")
df["dados"] = pd.to_datetime(df["dados"])
print(df.head())
</pre>

<hr>

<h2>Metrics</h2>

<ul>
<li>Revenue = quantity * price</li>
<li>Revenue per product</li>
<li>Sales per day</li>
<li>Average order value</li>
</ul>

<hr>

<h2>Aggregation Example</h2>

<pre>
df["revenue"] = df["quantidade"] * df["preço"]
revenue_by_product = df.groupby("produto")["revenue"].sum()
print(revenue_by_product)
</pre>

<hr>

<h2>Notes</h2>

<ul>
<li>Dataset is fully synthetic</li>
<li>No real business data</li>
<li>Educational purpose only</li>
<li>Focused on EDA fundamentals</li>
</ul>

<hr>

<h2>Next Steps</h2>

<ul>
<li>Add charts</li>
<li>Create dashboard</li>
<li>Time series analysis</li>
<li>Export KPIs</li>
</ul>

</body>
</html>

