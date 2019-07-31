import json
import os.path
import random


def load(fileName='hello.db'):
    
    meraDB = MeraDB(fileName)
    meraDB.load_file()
    return meraDB

def load_demerge(file_name="some_other.db"):

    dmergeDB=MeraDB(file_name)
    dmergeDB.dmerge()
    return dmergeDB

class MeraDB():
    def __init__(self, fileName):
       
        self.fileName = fileName

    def load_file(self):
        jObject = {}
        fileName = ""
        if os.path.exists(self.fileName):
            print "Loading Database from ", self.fileName, " !"
            content = open(self.fileName).read()
            self.jObject = json.loads(content)
            print "DB loaded successfully!"
        else:
            myFile=open(self.fileName,"w")
            string_data=json.dumps(jObject) 
            myFile.write(string_data)
            myFile.close()
            return self.jObject
    def dump(self):
        
        print "Dumping database to ", self.fileName, " !"
        
        open(self.fileName, 'w').write(json.dumps(self.jObject))
        file_handler = open(self.fileName, 'w')
        json_dump = json.dumps(self.jObject)
        file_handler.write(json_dump)
        file_handler.close()

        print "DB dumped successfully!"
        return "OK"

    def setData(self,key,value):
        self.jObject[key]=value
        open(self.fileName, 'w').write(json.dumps(self.jObject))
        file_handler = open(self.fileName, 'w')
        json_dump = json.dumps(self.jObject)
        file_handler.write(json_dump)
        file_handler.close()
        return True

    def getData(self,key):
        self.jObject[key]
        open(self.fileName, 'w').write(json.dumps(self.jObject))
        file_handler = open(self.fileName, 'w')
        json_dump = json.dumps(self.jObject)
        file_handler.write(json_dump)
        file_handler.close()
        return True
    
    def getAllKey(self,dict_data):
        for key in dict_data:
            print "key:  ", key
    
    def rem(self,myDict):
        del myDict["courses"]
        return myDict

    def exist(self,key):
        if key in self.jObject:
            return True
        else:
            return False

    def totalKey(self,dict_data):
        count=0
        for key in dict_data:
            count=count+1
        return count

    def deleteAllKey(self,dict_data):
        dict_data.clear()
        return dict_data

    def randomIncertKeyValue(self,num):
        for i in range (num):
            key=random.randint(1,100)
            value=random.randint(1,100)
            self.jObject[key]=value

    def dmerge(self):
        myFile=open("some_other.db","w")
        string_data=json.dumps(self.jObject) 
        myFile.write(string_data)
        myFile.close()
        return self.jObject