#import the class file
import PAMI.extras.dbStats.transactionalDatabaseStats as stats
    
class frequenciesOfItems:
    fileName: str = ''
    separator: str =''
    obj: any
    def __init__(self,fileName,separator):
        self.fileName = fileName
        self.separator = separator
        obj = stats.transactionalDatabaseStats(fileName,sep = separator)
        obj.run() 
        print(type(obj))
        
    def getFrequencies(self):
        return self.obj
itemsFrequencies = frequenciesOfItems('transactional database','\t')
itemsFreqDictionary = itemsFrequencies.getFrequencies()
