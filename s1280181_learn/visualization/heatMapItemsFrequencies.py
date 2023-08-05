import plotly.express as px
import pandas as pd
    

class heatMapItemsFrequencies :
    df: object
    def __init__(self,df):
        self.df = df
    def HeatMap(self):
        fig = px.density_mapbox(self.df, lat='lat', lon='lon', z='frequency', radius=8,
                        center={'lat':34.686567, 'lon':135.52000}, zoom=5,height = 600,width=800,
                        mapbox_style='open-street-map')
        fig.show()
