import pandas as pd
from numpy import int64

data = pd.read_csv('datasets/data_lp.csv')
print(data.dtypes)

import plotly.express as px
# Plotly - Biblioteca que armazena uma função que desenha mapas
# Scatter MapBox - Função que desenha um mapa

data_mapa = data[['id', 'lat', 'long', 'price']]
mapa = px.scatter_mapbox(data_mapa, lat='lat', lon='long', hover_name='id',
               hover_data=['price'],
               color_discrete_sequence=['blue'],
               zoom=3,
               height=300 )

mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0})
mapa.show()