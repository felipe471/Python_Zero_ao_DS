import pandas as pd
from numpy import int64

data = pd.read_csv('datasets/kc_house_data.csv')
# print(data.dtypes)

# # ===========
# # Converter os tipos de variáveis
# # ===========
#
# # string ---> date
# data['date'] = pd.to_datetime(data['date'])
# print(data.dtypes)
#
# # int ---> float
# data['bedrooms'] = data['bedrooms'].astype(float)
# print(data.dtypes)
# print(data[['id', 'bedrooms']].head(3))
#
# # float ---> int
# data['bedrooms'] = data['bedrooms'].astype(int64)  # É mandatório ser int64
# print(data.dtypes)
#
# # int ---> string
# data['bedrooms'] = data['bedrooms'].astype(str)
# print(data.dtypes)
#
# # int ---> string
#
# data['bedrooms'] = data['bedrooms'].astype(int64)
# print(data.dtypes)
#
# # ===========
# # Manipulação de Dados
# # ===========
#
# # Criando novas variáveis
#
# data['nome'] = 'felipe'
# data['idade'] = 34
# data['aniversário'] = pd.to_datetime('1987-01-18')
# print(data[['id', 'nome', 'idade']].head(6))
# print(data.dtypes)
#
#
# # Deletar novas variáveis
# print(data.columns)
#
# #data = data.drop(['nome', 'idade', 'aniversário'], axis=1)
#
# # ou
#
# cols = ['nome', 'idade', 'aniversário']
# data = data.drop(cols, axis=1)
#
# print(data.columns)

# Seleção de Dados

# Forma 01: Direto pelo nome das colunas

# print(data['price'])
# print(data[['price', 'id', 'date']])

# Forma 02: Pelos índices das linhas e colunas

# print(data.iloc[0:10, 0:5])

# Forma 03: Pelos índices das linhas e nome das colunas

print(data.loc[0:10, 'price'])    # uma coluna só
print(data.loc[0:10, ['price', 'bedrooms']]) # mais colunas... daí usa colchete duplo pq agora vc tem que fazer uma lista

# Forma 04: Índices Booleanos

# print(data.columns)

# cols = [True, False, True, True, False, False, True, False, True, True, False, False, True, False, True, True, False, False, True, False, False]
#
# print(data.loc[0:10, cols])

# Respostas das perguntas de negócio

# Pergunta 1
# data['date'] = pd.to_datetime(data['date'])
# print('A data do imóvel mais antigo no portfólio é {}'.format(data['date'].sort_values()))

# print('A data do imóvel mais antigo no portfólio é: {}'.format(pd.to_datetime(data['date'].sort_values(ascending=True)).head(1)))

# Pergunta 2

# print(data.columns)
#
# n_floors = data['floors'].max()
# print(n_floors)
# print('Temos {} imóveis com 1 andar'.format(len(data.query('floors == 1'))))
# print('Temos {} imóveis com 2 andares'.format(len(data.query('floors == 2'))))
# print('Temos {} imóveis com 3 andares'.format(len(data.query('floors == 3'))))
# print('Temos {} imóveis com mais de 3 andares'.format(len(data.query('floors > 3'))))
# print(data[['id', 'floors']].query('floors > 3'))

# print(data['floors'].unique())
# print(data[data['floors'] == 3.5][['floors', 'id']])
# print(data[data['floors'] == 3.5].shape)

# Pergunta 3

# data['level'] = 'standard'
# # print(data['level'].head(6))
# data.loc[data['price'] > 540000, 'level'] = 'high level'
# print(data.head())
#
# data.loc[data['price'] < 540000, 'level'] = 'low level'
# print(data.head())

# Pergunta 4

report = data[['id', 'date', 'price', 'bedrooms', 'sqft_lot']].sort_values('price', ascending=False)
print(report.head(6))
report.to_csv('datasets/report_aula02.csv', index=False)

# Pergunta 5
import plotly.express as px
# # Plotly - Biblioteca que armazena uma função que desenha mapas
# # Scatter MapBox - Função que desenha um mapa

data_mapa = data[['id', 'lat', 'long', 'price']]
mapa = px.scatter_mapbox(data_mapa, lat='lat', lon='long', hover_name='id',
               hover_data=['price'],
               color_discrete_sequence=['fuchsia'],
               zoom=3,
               height=300 )

mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0})
mapa.show()

# import plotly.express as px

houses = data[['id', 'lat','long','price']]

fig = px.scatter_mapbox(houses,
                        lat = 'lat',
                        lon = 'long',
                        size = 'price',
                        color_continuous_scale = px.colors.cyclical.IceFire,
                        size_max=15,
                        zoom=10)

fig.update_layout(mapbox_style = 'open-steet-map')
fig.update_layout(height=600, margin={'r':0,'t':0,'l':0,'b':0,})
fig.show()