<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Análise de Vendas — Dataset Sintético</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 900px;
            margin: auto;
            padding: 40px;
            line-height: 1.6;
            background-color: #fafafa;
        }

        h1, h2 {
            color: #333;
        }

        table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }

        th, td {
            border: 1px solid #ccc;
            padding: 10px;
            text-align: left;
        }

        th {
            background-color: #f0f0f0;
        }

        code {
            background: #eee;
            padding: 4px;
        }

        pre {
            background: #eee;
            padding: 15px;
            overflow-x: auto;
        }
    </style>
</head>

<body>

<h1>📊 Análise Técnica — Dataset Sintético de Vendas</h1>

<p>
Este projeto apresenta uma análise exploratória de um conjunto de dados sintéticos de vendas armazenado no arquivo <strong>analise.csv</strong>.
O objetivo é aplicar técnicas de manipulação, agregação e visualização de dados utilizando Python.
</p>

<hr>

<h2>📁 Estrutura do Dataset</h2>

<table>
<tr>
    <th>Coluna</th>
    <th>Tipo</th>
    <th>Descrição</th>
</tr>
<tr>
    <td>dados</td>
    <td>Date</td>
    <td>Data da transação</td>
</tr>
<tr>
    <td>produto</td>
    <td>String</td>
    <td>Nome do produto</td>
</tr>
<tr>
    <td>quantidade</td>
    <td>Integer</td>
    <td>Unidades vendidas</td>
</tr>
<tr>
    <td>preço</td>
    <td>Float</td>
    <td>Preço unitário</td>
</tr>
</table>

<hr>

<h2>🎯 Obje
