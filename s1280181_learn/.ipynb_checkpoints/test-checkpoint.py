from statistics import frequenciesOfItems as stats
from visualization import heatMapItemsFrequencies as mpx

itemsFrequencies = stats.frequenciesOfItems ('PM24HeavyPollutionRecordingSensors.csv','\t')
df = itemsFrequencies.getFrequencies()
HeatMap = mpx.heatMapItemsFrequencies(df)
HeatMap.HeatMap()
