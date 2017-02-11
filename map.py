import plotly.plotly as py
import pandas as pd
from atm import *

#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_us_cities.csv')
thinglist = main()
thingyList = {"name" : thinglist[0],
              "pop" : thinglist[1],
	       "lon" : thinglist[2],
                "lat" : thinglist[3]}
df = pd.DataFrame(thingyList) 
#print(type(df))
#print("\n")
#print(df)
df.head()

df['text'] = df['name'] + '<br>Population ' + (df['pop']).astype(str)+'hello world'
limits = [(0,100),(101,200),(201,300),(301,400),(401,1000)]
colors = ["rgb(0,116,217)","rgb(255,65,54)","rgb(133,20,75)","rgb(255,133,27)","lightgrey"]
cities = []
scale = 1000

for i in range(len(limits)):
    lim = limits[i]
    df_sub = df[lim[0]:lim[1]]
    city = dict(
        type = 'scattergeo',
        locationmode = 'USA-states',
        lon = df_sub['lon'],
        lat = df_sub['lat'],
        text = df_sub['text'],
        marker = dict(
            size = df_sub['pop']/scale,
            color = colors[i],
            line = dict(width=0.5, color='rgb(40,40,40)'),
            sizemode = 'area'
        ),
        name = '{0} - {1}'.format(lim[0],lim[1]) )
    print("!")
    cities.append(city)

layout = dict(
        title = 'Captial One Branch Locations<br>(Click legend to toggle traces)',
        showlegend = True,
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showland = True,
            landcolor = 'rgb(217, 217, 217)',
            subunitwidth=1,
            countrywidth=1,
            subunitcolor="rgb(255, 255, 255)",
            countrycolor="rgb(255, 255, 255)"
        ),
    )

fig = dict( data=cities, layout=layout )
py.iplot( fig, validate=False, filename='d3-bubble-map-populations' )

