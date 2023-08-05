import plotly.express as px
import pandas as pd
    
df = pd.read_csv('/Users/s1280181/python/s1280181_learn/s1280181_learn/statistics/itemFrequency.csv',sep='\t')
df.iloc[:,0] = df.iloc[:,0].replace(',{2,}','', regex=True)
df = df[~df.iloc[:, 0].str.contains(',')]
# DataFrameをcsvファイルに書き出し
# タブ区切りであることを指定
# 行番号や列名が出力されないように指定
df.columns = ['Point', 'frequency']
# Point列をカンマで分割して、緯度と経度の列を作る
df[['lon', 'lat']] = df['Point'].str.strip('[]').str.split(' ', expand=True)
# 緯度と経度の列を数値に変換する
df['lon'] = df['lon'].apply(lambda x: pd.to_numeric(x.strip("'Point("),errors='coerce'))
df['lat'] = df['lat'].apply(lambda x: pd.to_numeric(x.strip(")'"),errors='coerce'))
df = df.dropna(axis=0, how='any')
print(df)
# ヒートマップを作る
fig = px.density_mapbox(df, lat='lat', lon='lon', z='frequency', radius=8,
                        center={'lat':34.686567, 'lon':135.52000}, zoom=5,height = 600,width=800,
                        mapbox_style='open-street-map')
fig.show()

class heatMapItemsFrequencies :
    def __init__(self,obj)
    {
        
    }