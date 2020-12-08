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
# SO
from os.path import dirname, join
# Data manipulation
import pandas as pd
import numpy as np
# Bokeh libraries
from bokeh.io import curdoc  #output_file #, output_notebook, curdoc
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Div, Select, Slider, TextInput
from bokeh.layouts import row, column, gridplot, layout
from bokeh.models.widgets import Tabs, Panel
#from bokeh.io import output_file

## ==== ##
## DATA ##
## ==== ##
#data = pd.read_csv("~/home/deimos/Documents/Data-Visualizations/NY_AirBB_Bokeh/AB_NYC_2019.csv")
data = pd.read_csv("NY_AirBB_Bokeh/AB_NYC_2019.csv")

# Eliminate nans and incomplete rows for simplicity
data = data.dropna()
print(data.shape)
data = data.iloc[0:1000]
print(data.shape)

# Make sure that the data is the right type
data["price"] = pd.to_numeric(data["price"])
data["reviews_per_month"] = pd.to_numeric(data["reviews_per_month"])
data["availability_365"] = pd.to_numeric(data["availability_365"])

#print(data[data["price"] > 30]["host_id"])
#print(data["price"].describe())

# Adding new information for improving the plot
data['room_type_color'] = np.where(data['room_type'] == 'Entire home/apt', 'blue', 'green')
'''
data[data['room_type'] == 'Shared room'] = 'red'
'''
data['alpha'] = np.where(data['room_type'] == 'Entire home/apt', 0.4, 0.3)
#data[data['room_type'] == 'Shared room'] = 0.75


## ========== ##
## BOKEH_PLOT ##
## ========== ##

# Bring extra info from an external html file
desc = Div(text=open(join(dirname(__file__), "description.html")).read(), sizing_mode="stretch_width")

# Define posible axis and tooltips
axis_map = {
        "Longitude": "longitude",
        "Latitude": "latitude",
        "Price": "price",
        "Reviews per month": "reviews_per_month",
        "Days available": "availability_365"
}

TOOLTIPS = [
        ("Availability", "@availability_365"),
        ("Price", "@price"),
        ("Room type", "@room_type"),
        ("Number of reviews", "@number_of_revies"),
]

# Create input controls
#latitude_slider = Slider(title="Latitude", ) # completar
#longitude_slider = Slider(title="Longitude", ) # Completar
prices_slider = Slider(title="Price per night >=",
                       value=80, #np.nanmean(data["price"].values()),
                       start=0, #min(data["price"].values()),
                       end=500, #max(data["price"].values()),
                       step=10)
reviews_slider = Slider(title="Number of reviews per month",
                        value=5, #np.nanmean(data["reviews_per_month"].values()),
                        start=0, #min(data["reviews_per_month"].values()),
                        end=100, #max(data["reviews_per_month"].values()),
                        step=5)
avaiability_slider = Slider(title="Number of days available per year",
                        value=180,
                        start=0,
                        end=365,
                        step=10)
x_axis = Select(title="X Axis",
                options=sorted(axis_map.keys()),
                value="Longitude")
y_axis = Select(title="Y Axis",
                options=sorted(axis_map.keys()),
                value="Latitude")

# Create column data source
source = ColumnDataSource(data=dict(x=[],
                                    y=[],
                                    room_type_color=[],
                                    alpha=[]))  # continuar anadiendo mas informacion

# Init the figure
fig = figure(plot_height=600,
             plot_width=600,
             toolbar_location=None, # None, "above", "below", "left", "right"
             tooltips=TOOLTIPS)

fig.circle(x='x',
           y='y',
           source=source, #data,
           color='room_type_color',
           line_color=None,
           fill_alpha="alpha")

def selectFlats():
    """Select info to be displayed."""
    data["price"] = pd.to_numeric(data["price"])
    
    '''
    selected = data[
        (data["price"] >= float(prices_slider.value)) &
        (data["reviews_per_month"] >= float(reviews_slider.value)) #&
        #(data["avaiability_365"] >= int(avaiability_slider))
    ]
    '''
    mask = (data["price"] > prices_slider.value)
    selected = data[mask]
    #print("  --> ", len(selected))
    print(prices_slider.value, type(prices_slider.value))
    print(reviews_slider.value, type(reviews_slider.value))
    print(avaiability_slider.value, type(avaiability_slider.value))
    #print("0000", selected.head())
    return selected

def update():
    """Update the plot."""
    df = selectFlats()

    x_name = axis_map[x_axis.value]
    y_name = axis_map[y_axis.value]

    fig.xaxis.axis_label = x_axis.value
    fig.yaxis.axis_label = y_axis.value

    fig.title.text = str(len(df)) + " flats selected"
    source.data = dict(
            x=df[x_name],
            y=df[y_name],
            room_type_color=df["room_type_color"],
            alpha=df["alpha"]
    )

controls = [prices_slider, reviews_slider, avaiability_slider, x_axis, y_axis]
# Add controls
for control in controls:
    control.on_change('value', lambda attr, old, new: update())

inputs = column(*controls, width=320, height=100)
inputs.sizing_mode = "fixed"
l = layout([ [desc], [inputs, fig], ], sizing_mode="scale_both")

update()

curdoc().add_root(l)
curdoc.title="Movies"

# Output file
#output_file("NY_AirBnB_2019.html", title="NY AirBnB 2019")

# Show
show(l)
