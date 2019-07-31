import requests
import random
import os.path
import json

course_id_list=[]
def get_course(api1):
    if os.path.exists("coursesData.json"):
        myFile=open("coursesData.json","r")
        data1=myFile.read()
        dictData=json.loads(data1)
        courses=dictData["availableCourses"]
        count = 0
        for index in courses:
            print count,index["name"],index["id"]
            course_id_list.append(index["id"])
            count=count+1
    else:
        resp = requests.get(api1)
        jsonObject = resp.json()
        courseJsonFile=open("coursesData.json","w")
        stringData=json.dumps(jsonObject)
        courseJsonFile.write(stringData)
url1 = 'http://saral.navgurukul.org/api/courses'
get_course(url1)

random_course_id = random.choice(course_id_list)
print random_course_id

def get_excersice(api2):
    myfilename="files/excersice"+str(random_course_id)+".json"
    if os.path.exists(myfilename):
        excersiceJsonFile=open(myfilename,"r")
        data1=excersiceJsonFile.read()
        dictData=json.loads(data1)
        exercises=dictData["data"]
        count=0
        for index in exercises:
            print count,index["name"],index["id"]
            childExcersiceData=index["childExercises"]
            count1=0
            for index1 in childExcersiceData:
                print "       ",count1,index1["name"],index1["id"]
                count1=count1+1
            count=count+1
    else:
        resp=requests.get(api2)
        jsonObject=resp.json()
        exerciseJsonFile=open(myfilename,"w")
        stringData=json.dumps(jsonObject)
        exerciseJsonFile.write(stringData)

url2 = 'http://saral.navgurukul.org/api/courses/'+str(random_course_id)+'/exercises'
get_excersice(url2)
