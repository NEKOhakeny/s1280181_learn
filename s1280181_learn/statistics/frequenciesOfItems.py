#import the class file
import PAMI.extras.dbStats.transactionalDatabaseStats as stats
import pandas as pd


class frequenciesOfItems:
    fileName: str
    separator: str
    obj: object
    def __init__(self,fileName,separator):
        self.fileName = fileName
        self.separator = separator
        self.obj = stats.transactionalDatabaseStats(fileName,sep = separator)
        self.obj.run() 
        self.obj.save(self.obj.getSortedListOfItemFrequencies(),'test.csv')
    def getFrequencies(self):
        df = pd.read_csv('test.csv',sep= self.separator)
        df.iloc[:,0] = df.iloc[:,0].replace(',{2,}','', regex=True)
        df = df[~df.iloc[:, 0].str.contains(',')]
        df.columns = ['Point', 'frequency']
        df[['lon', 'lat']] = df['Point'].str.strip('[]').str.split(' ', expand=True)
# 緯度と経度の列を数値に変換する
        df['lon'] = df['lon'].apply(lambda x: pd.to_numeric(x.strip("'Point("),errors='coerce'))
        df['lat'] = df['lat'].apply(lambda x: pd.to_numeric(x.strip(")'"),errors='coerce'))
        df = df.dropna(axis=0, how='any')
        print(df)
        return df
