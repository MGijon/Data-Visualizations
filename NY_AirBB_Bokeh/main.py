""" Bokeh interactive visualization of the dataset 'NY Airbnb 2019'

'id': id of the element 
'name': name of the element
'host_id': id of the host
'host_name': name of the host
'neighbourhood_group': neighbourhood group identifier
'neighbourhood': neighbourhood identifier 
'latitude': latitude (coordinates, flat location)
'longitude': longitude (coordinates, flat location)
'room_type': type of room (3 types considered: Entire home/apt, Private room, Shared room)
'price': price per night
'minimum_nights': minimun number of nights
'number_of_reviews': number or reviews
'last_review': last review 
'reviews_per_month': number of reviews per month
'calculated_host_listings_count':
'availability_365': days available per year
"""
# Data manipulation
import pandas as pd
import numpy as np
# Bokeh libraries
from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Div, Select, Slider, TextInput
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel
from bokeh.io import output_file

## ==== ##
## DATA ##
## ==== ##
data = pd.read_csv("AB_NYC_2019.csv")
#print(data.columns)
#data = data.dropna()

#print(data['room_type'].value_counts())
#data['room_type_color'] = ['green' for _ in range(data.shape[0])]
#data['room_type_color'] = np.where(data['room_type'] == 'Entire home/apt', 'blue', 'green')
#data['room_type_color'] = np.where((data['room_type'] == 'Private room') & (data['room_type'] != 'Entire home/apt'),       'yellow', 'blue'
data['room_type_color'] = np.where(data['room_type'] == 'Entire home/apt', 'blue', 'green')
#data[data['room_type'] == 'Private room']['room_type_color'] = 'yellow'

#Entire home/apt    2540
#Private room       22326
#Shared room
#print(data.head(20))

print(data['room_type_color'].value_counts())
#print(data['calculated_host_listings_count'].value_counts())

## ========== ##
## BOKEH_PLOT ##
## ========== ##

# Define posible axis and tooltips
axis_map = {
        
}

TOOLTIPS = [
        ("Availability", "@availability_365"),
        ("Price", "@price"),
        ("Room type", "@room_type"),
        ("Number of reviews", "@number_of_revies"),
]

# Init the figure
fig = figure(plot_height=600,
             plot_width=600, 
             toolbar_location="above", # None, above, below, left, right
             tooltips=TOOLTIPS)

fig.circle(x='latitude',
           y='longitude', 
           source=data, 
           color='room_type_color')


# Output file
output_file("NY_AirBnB_2019.html", title="NY AirBnB 2019")

# Show the figure
show(fig)
