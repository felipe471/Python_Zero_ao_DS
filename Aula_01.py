# Carregue o conjunto de dados chamado kc_house_data.csv

# funcao - read_csv()

# biblioteca Pandas

import pandas as pd

data = pd.read_csv('datasets/kc_house_data.csv')

# Mostra na tela as 6 primeiras linhas do conjunto de dados

print(data.head())

# Mostre o número de colunas e o número de linhas do conjunto de dados

print(data.shape)

# Mostre na tela o nome das colunas dos conjuntos de dados

print(data.columns)

# Mostre na tela o cojunto de dados ordenados pela coluna price

print(data.sort_values('price'))

# Para ver o id e o preço basta adcionar colchetes duplo depois de data e antes do .

print(data[['price', 'id']].sort_values('price'))

# # Mostre na tela o cojunto de dados ordenados pela coluna price do maior para o menor

print(data[['price', 'id']].sort_values('price', ascending=False))

print(data[['bedrooms', 'id']].sort_values('bedrooms', ascending=False))

print(data['bedrooms'].sum())

print((data['bathrooms'] == 2).sum())

print(len(data.query('bathrooms==2')))

print(data['price'].mean())

dois_banheiros = data.query('bathrooms==2')
print('o preço médio de todas as casas com 2 banheiros é $ {:.2f}'.format(dois_banheiros['price'].mean()))

tres_quartos = data.query('bedrooms==3')
print('O preço mínimo das casas com 3 quartos é $ {:.2f}'.format(data['price'].min()))

print('{} casas possume mais de 300m² de sala de estar.'.format(len(data.query('sqft_living > 3229.17'))))

dois_andares = print('{} casas possuem mais de 2 anadares'.format(len(data.query('floors == 2'))))

vista_mar = print('{} casas tem vista para o mar'.format(len(data.query('view == 1'))))

vista_mar_1 = data.query('view == 1')
print('Das casas com vista para o mar, {} tem 3 quartos'.format(len(vista_mar_1.query('bedrooms == 3'))))

casas_300m = data.query('sqft_living > 3229.17')
a = print('Das casas com mais de 300 m² de sala de estar, {} tem 3 banheiros'.format(len(casas_300m.query('bathrooms==3'))))
