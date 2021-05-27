import pandas as pd
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.express as px
from plotly.offline import download_plotlyjs, plot,iplot

df = pd.read_csv("infant_mortality_2020.csv");

data = dict(type='choropleth',locations=df['Country or Area'],
            z=df['Value'],locationmode='country names',
            colorscale='portland',
            colorbar={'title':'Deaths/1,000 live births'})

layout = dict(title='Infant Mortality, 2020',
              geo=dict(showframe=True, showlakes=True,lakecolor='rgb(85,173,240)',
                       projection={'type':'equirectangular'}))

choromap = go.Figure(data=[data], layout=layout)
choromap.update_layout(title={'xanchor':'center','yanchor':'top','y':0.9,'x':0.5},
                       font=dict(size=20))

plot(choromap)
