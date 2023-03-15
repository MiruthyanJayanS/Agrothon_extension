import streamlit as st
import pandas as pd
import numpy as np
from trends import *
arhar = Commodity(commodity_dict["arhar"])
commodity_list.append(arhar)
bajra = Commodity(commodity_dict["bajra"])
commodity_list.append(bajra)
barley = Commodity(commodity_dict["barley"])
commodity_list.append(barley)
copra = Commodity(commodity_dict["copra"])
commodity_list.append(copra)
cotton = Commodity(commodity_dict["cotton"])
commodity_list.append(cotton)
sesamum = Commodity(commodity_dict["sesamum"])
commodity_list.append(sesamum)
gram = Commodity(commodity_dict["gram"])
commodity_list.append(gram)
groundnut = Commodity(commodity_dict["groundnut"])
commodity_list.append(groundnut)
jowar = Commodity(commodity_dict["jowar"])
commodity_list.append(jowar)
maize = Commodity(commodity_dict["maize"])
commodity_list.append(maize)
masoor = Commodity(commodity_dict["masoor"])
commodity_list.append(masoor)
moong = Commodity(commodity_dict["moong"])
commodity_list.append(moong)
niger = Commodity(commodity_dict["niger"])
commodity_list.append(niger)
paddy = Commodity(commodity_dict["paddy"])
commodity_list.append(paddy)
ragi = Commodity(commodity_dict["ragi"])
commodity_list.append(ragi)
rape = Commodity(commodity_dict["rape"])
commodity_list.append(rape)
jute = Commodity(commodity_dict["jute"])
commodity_list.append(jute)
safflower = Commodity(commodity_dict["safflower"])
commodity_list.append(safflower)
soyabean = Commodity(commodity_dict["soyabean"])
commodity_list.append(soyabean)
sugarcane = Commodity(commodity_dict["sugarcane"])
commodity_list.append(sugarcane)
sunflower = Commodity(commodity_dict["sunflower"])
commodity_list.append(sunflower)
urad = Commodity(commodity_dict["urad"])
commodity_list.append(urad)
wheat = Commodity(commodity_dict["wheat"])
commodity_list.append(wheat)

import streamlit as st
import pandas as pd
import plotly.express as px

# Define the data
data = TwelveMonthsForecast('safflower')[2]

# Convert the data to a Pandas DataFrame
df = pd.DataFrame(data, columns=['Month', 'Price', 'Change'])

# Create the chart using Plotly
fig = px.line(df, x='Month', y='Price', title='Price of a product over time')
fig.update_traces(mode='markers+lines', marker=dict(size=8, symbol='circle', color='blue'), line=dict(width=2))

# Add the percentage change as a secondary y-axis
fig.add_scatter(x=df['Month'], y=df['Change'], name='Percentage Change', mode='lines', yaxis='y2', line=dict(width=2, color='red'))

# Set the layout of the chart
fig.update_layout(
    yaxis=dict(title='Price'),
    yaxis2=dict(title='Percentage Change', overlaying='y', side='right', showgrid=False),
    xaxis=dict(tickangle=45),
    title=dict(x=0.5, y=0.9, xanchor='center', yanchor='top')
)

# Display the chart in Streamlit
st.plotly_chart(fig)
