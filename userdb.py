import json
import meradb
import pickledb
from courses_data import inside

db = meradb.load("table.db")
db = pickledb.load("pickleDBdata.db")
y=inside["availableCourses"]
db.setData("courses",y)
db.getData("courses")
file_data=open("table.db","r")
load_data=json.load(file_data)
db.getAllKey(load_data)
db.totalKey(load_data)
db.rem(load_data)
db.exist("courses")
db.deleteAllKey(load_data)
db.randomIncertKeyValue(10)
db.dmerge()
db.dump()


