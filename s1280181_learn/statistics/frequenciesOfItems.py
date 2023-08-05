#import the class file
import PAMI.extras.dbStats.transactionalDatabaseStats as stats
    
class frequenciesOfItem:
    fileName:str
    separator:str
    obj:any
    def __init__(self,fileName,separator):
        self.fileName = fileName
        self.separator = separator
        obj = stats.transactionalDatabaseStats(fileName,sep = separator)
        obj.run() 
    
    def getFrequencies(self):
        return self.obj
