# importando as bibliotecas pandas e streamlit

import pandas as pd
import streamlit as st
from statistics import mean


# Adicionando alguns elementos de texto.

st.title('Dashboard - Dados da Agricultura nos EUA')
st.header('_Gráficos_ :chart: : ')
st.subheader(':green[Os 5 Produtos com os maiores valores de fazenda]')

# Trazendo a base de dados e ordenando pela data mais atual.

tabela = pd.read_csv('ProductPriceIndex.csv')
tabela = tabela.sort_values(by=['date'], ascending=False)

# Escrevendo as datas apenas com o ano (YYYY).

for i, data in enumerate(tabela['date']):
    tabela.iloc[i, 1] = data[0: 4]


# Criando uma tabela apenas com os resultados de 2019.
tabela_2019 = tabela.loc[lambda tabela: tabela['date'] == '2019']

# Ordenando os valores de fazenda do mais caro para o mais barato 
tabela_2019 = tabela_2019.sort_values(by=['farmprice'], ascending=False)

# Eliminando as itens duplicados por nome de produto.
tabela_2019 = tabela_2019.drop_duplicates(subset=['productname'])

# Derando o df com apenas os 5 primeiros itens da tabela_2019
tabela_2019.columns = ['Produto', 'Ano', 'Valor de Fazenda', 'Atlanta', 'Chicago', 'Los Angeles', 'New York', 'Media']
tabela_mais_caros = tabela_2019.iloc[0: 5]


# Transformando os valores em float.
for i, data in enumerate(tabela_mais_caros['Valor de Fazenda']):
    tabela_mais_caros.iloc[i, 2] = data.replace('$', '')
    tabela_mais_caros.iloc[i, 2] = float(tabela_mais_caros.iloc[i, 2])


# Plotando um gráfico de barra do valor de fazenda x nome do produto.
st.bar_chart(tabela_mais_caros, x='Produto', y='Valor de Fazenda', color=['#32CD32'])

st.subheader('Escolha o produto e veja a média de custo: ')
st.text('OBS -> Considerando: Atlanta, Chicago, Los Angeles e Nova York')

# Criando função para mostrar a média de custo dos produtos mais caros, considerando 
def mostra_locais(produto: str):
    tabela_produto = tabela_mais_caros.loc[lambda tabela_2019: tabela_2019['Produto'] == f'{produto}'].drop(['Valor de Fazenda', 'Produto', 'Ano', 'Media'], axis=1)
    valores = [float(x[1:]) for x in tabela_produto.iloc[0]]
    return f'A média de valor do {produto} é de $ {mean(valores):.2f}'


# Loopin para seleção do produto e aplicação da função mostra_locais
while True:

    produto = st.selectbox(
        'Escolha o produto: ',
        ('Couve-flor', 'Salsão', 'Morango','Espargos', 'Batata'))

    if produto == 'Couve-flor':
        st.subheader(mostra_locais('Cauliflower'))
        break

    elif produto == 'Salsão':
        st.subheader(mostra_locais('Celery'))
        break

    elif produto == 'Morango':
        st.subheader(mostra_locais('Strawberries'))
        break

    elif produto == 'Espargos':
        st.subheader(mostra_locais('Asparagus'))
        break

    elif produto == 'Batata':
        st.subheader(mostra_locais("Potatoes"))
        break





