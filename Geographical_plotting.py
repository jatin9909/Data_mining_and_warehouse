import pandas as pd
import chart_studio.plotly as py
import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, plot,iplot


pop = pd.read_csv("population_by_country_2020.csv")

data = dict(type='choropleth', locations=pop['Country'],
            z=pop['Population'],
            locationmode='country names', colorscale='Portland')

layout=dict(title='2020 Population', geo=dict(showframe=True, projection={'type':'mercator'}))

choromap = go.Figure(data=[data],layout=layout)
plot(choromap)
