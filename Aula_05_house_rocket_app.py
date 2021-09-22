# Libraries
# ----------------------

import pandas as pd
import ipywidgets as widgets
import numpy as np
import datetime as dt
import plotly.express as px
import streamlit as st
from ipywidgets import fixed
from IPython.display import display
from matplotlib import gridspec
from matplotlib import pyplot as plt

# Streamlit Markdowns

st.title('House Rocket Company')

st.markdown('Welcome to House Rocket Data Analysis')

st.header('load data: kc_house_data.csv')

@st.cache(allow_output_mutation=True)

# ----------------------
# Functions
# Requisitos
# 1 - Nome: em relação a sua responsabilidade
# 2 - Input: Parâmetros de entrada
# 3 - Output: dados de saída ou dataframes de saída
# ----------------------

def data_head(data):
    print(data.head())
    return None

def collect_geodata(data):
    
    # creat empty
    
    data['place_id']     = 'NA'
    data['osm_type']     = 'NA'
    data['country']      = 'NA'
    data['country_code'] = 'NA'
    
    # Initialize API
    geolocator = Nominatim(user_agent="geoapi_exercise")

    # Make query

    for i in range(len(data)):
        query = str(data.loc[i, 'lat']) + ',' + str(data.loc[i, 'long'])

    # API Request

        response = geolocator.reverse(query)    

    # Populate Data

        if 'country_code' in response.raw['address']:
            data.loc[i, 'country_code'] = response.raw['address']['country_code']


        data.loc[i, 'place_id'] = response.raw['place_id']    


        data.loc[i, 'osm_type'] = response.raw['osm_type']  

        if 'country' in response.raw['address']:
            data.loc[i, 'country'] = response.raw['address']['country']  
            
    return data
    
    
def data_collect(path):
    
    # ----------------------
    # Extraction
    # ----------------------
    
    # Load dataset
    data = pd.read_csv(path)
   
    return data

def data_transform(data):
    
    # ----------------------
    # Transformation
    # ----------------------
    
    # Change date format
    
    data['year'] = pd.to_datetime(data['date']).dt.strftime('%Y')
    data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')
    data['year_week'] = pd.to_datetime(data['date']).dt.strftime('%Y-%U')
    
    # descriptive statistics
    num_attributes = data.select_dtypes(include = ['int64', 'float'])
   
   # central tendencies (mean, median)
    pd.set_option('display.float_format', lambda x: '%.3f' % x)
    media = pd.DataFrame(num_attributes.apply(np.mean, axis=0))
    mediana = pd.DataFrame(num_attributes.apply(np.median, axis=0))
    
    # dispersion (min, max, std)
    std = pd.DataFrame(num_attributes.apply(np.std, axis=0))
    min_ = pd.DataFrame(num_attributes.apply(np.min, axis=0))
    max_ = pd.DataFrame(num_attributes.apply(np.max, axis=0))
    
    df1 = pd.concat([max_, min_, media, mediana, std], axis = 1).reset_index()
    
    df1.columns = ['attributes', 'max', 'min', 'média', 'mediana', 'std']
    
    # show_dimensions_dataframe(data)
    
    data['level'] = 'NA'
    
    for i in range(len(data)):
        
        if (data.loc[i, 'price'] > 0) & (data.loc[i, 'price'] <= 321950):
            data.loc[i, 'level'] = 'Level 0'
            
        elif (data.loc[i, 'price'] > 321950) & (data.loc[i, 'price'] <= 450000):
             data.loc[i, 'level'] = 'Level 1'
                
        elif (data.loc[i, 'price'] > 450000) & (data.loc[i, 'price'] <= 645000):
             data.loc[i, 'level'] = 'Level 2'
                
        else:
            data.loc[i, 'level'] = 'Level 3'
            
    by_price = data[['price', 'level']].groupby('level').mean().reset_index()

    for i in range(len(data)):

        if data.loc[i, 'waterfront'] == 0:
            data.loc[i, 'waterfront'] = 'No'
        else:
            data.loc[i, 'waterfront'] = 'Yes'
    
    data['size_level'] = 'NA'
    
    for i in range(len(data)):
        if (data.loc[i, 'sqft_living'] >= 0) & (data.loc[i, 'sqft_living'] < 1427):
            data.loc[i, 'size_level'] = 'size 0'
            
        elif (data.loc[i, 'sqft_living'] >= 1427) & (data.loc[i, 'sqft_living'] < 1910):
            data.loc[i, 'size_level'] = 'size 1'    
    
        elif (data.loc[i, 'sqft_living'] >= 1910) & (data.loc[i, 'sqft_living'] < 2550):
            data.loc[i, 'size_level'] = 'size 2' 
            
        else:
            data.loc[i, 'size_level'] = 'size 3'
    
    by_size = data[['sqft_living', 'size_level']].groupby('size_level').mean().reset_index()
    
#    show_dimensions(df1)
    
    return data

def data_load(data):
    
    # ----------------------
    # Load
    # ----------------------
       
    # Define Map
    
    def updateMap(data, limit1, limit2, limit3, limit4, condition, construction):
    
        houses = data[(data['sqft_living'] >= limit1) & 
                      (data['bathrooms'] >= limit2) & 
                      (data['price'] <= limit3) & 
                      (data['sqft_basement'] <= limit4) & 
                      (data['condition'] >= condition) & 
                      (data['yr_built'] <= construction)][['id', 'lat', 'long', 'sqft_living', 
                                                           'bathrooms', 'price', 'sqft_basement', 'condition', 'yr_built']]
    
    # plot map
    st.title('House Rocket Map')
    is_check = st.checkbox('Display Map')


    living_room_min = int(data['sqft_living'].min())
    living_room_max = int(data['sqft_living'].max())
    bedroom_min = int(data['bedrooms'].min())
    bedroom_max = int(data['bathrooms'].max())
    price_min = int(data['price'].min())
    price_max = int(data['price'].max())
    basement_size_min = int(data['sqft_basement'].min())
    basement_size_max = int(data['sqft_basement'].max())
    house_condition_min = int(data['condition'].min())
    house_condition_max = int(data['condition'].max())
    year_built_min = int(data['yr_built'].min())
    year_built_max = int(data['yr_built'].max())
    # waterview = str(data['waterfront'])


    living_room = st.slider('Living room size',
                            min_value=living_room_min,
                            max_value=living_room_max,
                            value=6000,
                            step=100)
    bedroom = st.slider('Number of bedrooms',
                            min_value=bedroom_min,
                            max_value=bedroom_max,
                            value=3,
                            step=1)
    price = st.slider('House price',
                            min_value=price_min,
                            max_value=price_max,
                            value=1000000,
                            step=5000)
    basement_size = st.slider('Basement size',
                            min_value=basement_size_min,
                            max_value=basement_size_max,
                            value=1000,
                            step=10)
    house_condition = st.slider('House condition',
                            min_value=house_condition_min,
                            max_value=house_condition_max,
                            value=3,
                            step=1)

    year_built = st.slider('Year built',
                            min_value=year_built_min,
                            max_value=year_built_max,
                            value=2000,
                            step=1)

    waterview = st.selectbox('Water View',
                            options = ['Yes', 'No'],
                            index = 0)

    if is_check:
        # select rows
        houses = data[(data['sqft_living'] < living_room) &
                      (data['bedrooms'] < bedroom) &
                      (data['price'] < price) &
                      (data['sqft_basement'] < basement_size) &
                      (data['condition'] <= house_condition) &
                      (data['yr_built'] <= year_built) &
                      (data['waterfront'] == waterview)][['id', 'lat', 'long','price']]
        # st.dataframe(houses)
        fig = px.scatter_mapbox(houses,
                                lat = 'lat',
                                lon = 'long',
                                # color = 'bathrooms',
                                size = 'price',
                                color_continuous_scale = px.colors.cyclical.IceFire,
                                size_max=15,
                                zoom=10)
    
        fig.update_layout(mapbox_style = 'open-street-map')
        fig.update_layout(height=600, margin={'r':0,'t':0,'l':0,'b':0,})
        st.plotly_chart(fig)

    # ##### DASHBOARD
    #
    # data['year'] = pd.to_datetime(data['date']).dt.strftime('%Y')
    # data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')
    # data['year_week'] = pd.to_datetime(data['date']).dt.strftime('%Y-%U')
    #
    # date_limit = widgets.SelectionSlider(options=data['date'].sort_values().unique().tolist(),
    #                                      value='2014-12-01',
    #                                      description='Disponível',
    #                                      continuous_update=False,
    #                                      orientation='horizontal',
    #                                      readout=True)
    #
    # # Widgets to control year renovated
    #
    # renovated_yr = widgets.BoundedIntText(
    #     value=2010,
    #     min=1930,
    #     max=2015,
    #     step=1,
    #     description='Ano de Renovação',
    #     disabled=False)
    #
    # # Widgets to control waterfront
    #
    # data['is_waterfront'] = data['waterfront'].apply(lambda x: 'yes' if x == 1 else 'no')
    #
    # water_view = widgets.Dropdown(
    #     options=data['is_waterfront'].unique().tolist(),
    #     value='yes',
    #     description='Waterview',
    #     disabled=False)
    #
    # st.sidebar.checkbox("Show Dashboard", True, key=1)
    # # if st.sidebar.checkbox("Show Dashboard", True, key=2):
    #
    # def update_map(data, limit, option, year):
    #
    #
    #     # Widgets to control data
    #
    #
    #     # Filter data
    #
    #     data = data[data['date']>= limit].copy()
    #
    #     fig = plt.figure(figsize=(20,12)) # Configura o tamanho da figura na tela do dashboard
    #     specs = gridspec.GridSpec(ncols=2, nrows=2,figure=fig) # Define como o dashboard será divido na tela
    #
    #     ax1 = fig.add_subplot(specs[0,:])  # First Row
    #     ax2 = fig.add_subplot(specs[1, 0])  # First Row - First Column
    #     ax3 = fig.add_subplot(specs[1, 1])  # Second Row - Second Column
    #
    #     # First Graph
    #
    #     by_year = data[['id', 'year']].groupby('year').sum().reset_index()
    #     ax1.bar(by_year['year'], by_year['id'])
    #
    #     # Second Graph
    #
    #     by_day = data[['id', 'date']].groupby('date').mean().reset_index()
    #     ax2.plot(by_day['date'], by_day['id'], 'go--', linewidth=1, markersize=6)
    #     ax2.set_title('title: Avg price by day')
    #
    #     # Third Graph
    #
    #     by_week_of_year = data[['id', 'year_week']].groupby('year_week').mean().reset_index()
    #     ax3.bar(by_week_of_year['year_week'], by_week_of_year['id'])
    #     ax3.set_title('title: Avg price by week of year')
    #     plt.xticks(rotation = 60);
    #
    # b = widgets.interactive(update_map, data = fixed(data), limit=date_limit, option=water_view, year=renovated_yr )
    # st.plotly_chart(b)


    
if __name__ == '__main__':
    # ETL
    
    # Collect
    
    data_raw = data_collect('datasets/kc_house_data.csv')
    
    # Transformation
    
    data_processing = data_transform(data_raw)
    
    # Load
    
    data_load(data_processing)



