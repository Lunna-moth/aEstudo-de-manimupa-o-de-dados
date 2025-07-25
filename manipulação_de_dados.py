# -*- coding: utf-8 -*-
"""Manipulação de dados.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XhEZYIgHc0W0ajdb5J73RTr5bBwFEB8d
"""

import pandas as pd

dados = pd.read_json('/content/dados_hospedagem.json')

dados.head(5)

dados = pd.json_normalize(dados['info_moveis'])
dados

colunas = list(dados.columns)
colunas

dados = dados.explode(colunas[3 :])
dados

dados.reset_index(inplace=True, drop=True)
dados

dados.info()

import numpy as np

dados['max_hospedes'] = dados['max_hospedes'].astype(np.int64)

dados.info()

col_numericas = ['quantidade_banheiros','quantidade_quartos','quantidade_camas']

dados[col_numericas] = dados[col_numericas].astype(np.int64)

dados.info()

dados['avaliacao_geral'] = dados['avaliacao_geral'].astype(np.float64)

dados.info()



from os import replace

dados['preco'] = dados['preco'].apply(lambda x: x.replace('$','').replace(',', '').strip())

dados['preco'] = dados['preco'].astype(np.float64)

dados.info()

dados[['taxa_deposito','taxa_limpeza']]

dados[['taxa_deposito','taxa_limpeza']].applymap(lambda x: float(x.replace('$', '').replace(',','').strip()))

dados[['taxa_deposito','taxa_limpeza']] = dados[['taxa_deposito','taxa_limpeza']].applymap(lambda x: x.replace('$', '').replace(',','').strip())

dados[['taxa_deposito','taxa_limpeza']] = dados[['taxa_deposito','taxa_limpeza']].astype(np.float64)

dados.info()

dados['descricao_local']

dados['descricao_local'].str.lower()

dados['descricao_local'] = dados['descricao_local'].str.lower()

dados['descricao_local'].str.replace('[^a-zA-Z0-9\-\']', ' ', regex=True)

dados['descricao_local'] = dados['descricao_local'].str.replace('[^a-zA-Z0-9\-\']', ' ', regex=True)

dados['descricao_local'] = dados['descricao_local'].str.replace('(?<!\w)-(?!\w)', '', regex=True)

dados['descricao_local'] = dados['descricao_local'].str.split()
dados.head()

dados['comodidades'].str.replace('\{|}|\"','',regex=True)

dados['comodidades'] = dados['comodidades'].str.replace('\{|}|\"','',regex=True)

dados['comodidades'] = dados['comodidades'].str.split(',')
dados.head()

dt_data = pd.read_json('/content/moveis_disponiveis.json')
dt_data.head()

dt_data.info()

dt_data['data'] = pd.to_datetime(dt_data['data'])

dt_data.info()

dt_data.head()

dt_data['data'].dt.strftime('%Y-%m')

subset = dt_data.groupby(dt_data['data'].dt.strftime('%Y-%m'))['vaga_disponivel'].sum()
subset

