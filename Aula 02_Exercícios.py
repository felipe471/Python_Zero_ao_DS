import pandas as pd
import plotly.express as px
from numpy import int64
from datetime import datetime

data = pd.read_csv('datasets/kc_house_data.csv')

# Pergunta 1

data['date'] = pd.to_datetime(data['date'])  # convertendo str to datetime
# print(data.dtypes)
data['house_age'] = 'age'  # criando nova coluna house_age
# print(data[['date', 'house_age']].sort_values('date').head(3))  # imprimindo e ordenando em função da data

print(data.columns)  # 'imprimindo o nome das colunas'
data.loc[data['date'] > '2014-01-01', 'house_age'] = 'new_house'
print(data[['id', 'date', 'house_age']].sort_values('date'))

# Pergunta 2

data['dormitory_type'] = 'type'

data.loc[data['bedrooms'] == 1, 'dormitory_type'] = 'studio'
data.loc[data['bedrooms'] == 2, 'dormitory_type'] = 'apartment'
data.loc[data['bedrooms'] > 2, 'dormitory_type'] = 'house'

print(data[['id', 'bedrooms', 'dormitory_type']])

# Pergunta 3

data['condition_type'] = 'estado do imóvel'

data.loc[data['condition'] <= 2, 'condition_type'] = 'bad'
data.loc[data['condition'] == 3, 'condition_type'] = 'regular'
data.loc[data['condition'] == 4, 'condition_type'] = 'regular'
data.loc[data['condition'] == 5, 'condition_type'] = 'good'

print(data[['id', 'condition', 'condition_type']])

# Pergunta 4

data['condition'] = data['condition'].astype(str)

print(data.dtypes)

# Pergunta 5

data = data.drop(['sqft_living15', 'sqft_lot15'], axis=1)
var = data.columns

# Pergunta 6

data["yr_built"] = pd.to_datetime(data['yr_built'])
print(data.dtypes)

# Pergunta 7

data['yr_renovated'] = pd.to_datetime(data['yr_renovated'])
print(data.dtypes)

# Pergunta 8

# print(data[['id', 'yr_built']].sort_values('yr_built', ascending=True).head(2))
#
# Pergunta 9

# print(data[['id', 'yr_renovated']].sort_values('yr_renovated', ascending=True))
# print(data[data['yr_renovated'] > 0][['id', 'yr_renovated']].sort_values('yr_renovated', ascending=True))

# Pergunta 10

print(len(data.query('floors == 2')))

# Pergunta 11

print(len(data[data['condition_type'] == 'regular']))

# Pergunta 12

bad_houses = data[data['condition_type'] == 'bad']
print(len(bad_houses[bad_houses['waterfront'] == 1]))

print(data[(data['condition_type'] == 'bad') & (data['waterfront'] == 1)])

# Pergunta 13

print(data[(data['condition_type'] == 'good') & (data['house_age'] == 'new_house')].count)

# Pergunta 14

# Qual o valor do imóvel mais caro do tipo studio?

tipo_st = data[data['dormitory_type'] == 'studio']
print(tipo_st[['price','dormitory_type']].sort_values('price', ascending=False).head(1))
print(data[data['dormitory_type'] == 'studio'].sort_values('price', ascending=False).head(1))

# Pergunta 15

# Quantos imóveis do tipo apartement foram renovados em 2015?

print(data[(data['dormitory_type'] == 'apartment') & (data['yr_renovated'] == 2015)].shape)

# Pergunta 16

# Qual o maior número de quartos que um imóvel do tipo house possui?

print(data[data['dormitory_type'] == 'house'].sort_values('bedrooms', ascending=False))
# print(data.iloc[:,3])

# Pergunta 18

# Selecione as colunas id, date, price, floors, zipcode

print(data[['id', 'date', 'price', 'floors', 'zipcode']])
print(data.columns)

print(data.iloc[:,[1,2,3,7,16]])

print(data.loc[:,['id', 'date', 'price', 'floors', 'zipcode']])

print(data.loc[:,[True, True, True, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False]])

# Pergunta 19

data_save = data.iloc[:, 10:17]
print(data_save)

data_save.to_csv('datasets/E9_A2.csv')

# Pergunta 20

data_mapa = data[['id', 'lat', 'long', 'price']]
mapa = px.scatter_mapbox(data_mapa, lat='lat', lon='long', hover_name='id',
               hover_data=['price'],
               color_discrete_sequence=['darkgreen'],
               zoom=8,
               height=300 )

mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0})
mapa.show()

