import plotly.plotly as py
import plotly.graph_objs as graph_objs
import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('PythonAPI','ubpiol2cve')

mapbox_access_token = 'pk.eyJ1IjoiZGluZ3VzYWdhciIsImEiOiJjanM3MzBqbnEwc3AwNGFtczdkdHp4eHRsIn0.Sd1fkVZwvKIrx6B7_ScujA'

data = graph_objs.Data([
    graph_objs.Scattermapbox(
        lat=['45.5017'],
        lon=['-73.5673'],
        mode='markers',
    )
])
layout = graph_objs.Layout(
    height=600,
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        layers=[
            dict(
                sourcetype = 'geojson',
                source = 'Chennai-Wards-2011.geojson',
                type = 'fill',
                color = 'rgba(163,22,19,0.8)'
            ),
        ],
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=27.8,
            lon=-83
        ),
        pitch=0,
        zoom=5.2,
        style='light'
    ),
)

fig = dict(data=data, layout=layout)
py.iplot(fig)