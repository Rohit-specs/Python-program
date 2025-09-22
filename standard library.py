import datetime
import calendar
import os
import sys
import time
import json
import shutil


mytime=datetime.datetime.now()
print(mytime)
after10days=mytime+datetime.timedelta(days=10)
print(after10days)
oneyearlater=mytime+datetime.timedelta(days=365)
print(oneyearlater)

print(os.getcwd())
os.mkdir("rohit")
os.rmdir("rohit")
os.path.exists("Problem")

for i in range (4):
    print(i)
    time.sleep(1.2)

print(calendar.calendar(2025))
print(calendar.month(2025,9))
print(calendar.isleap(2028))

dict={"id": 103,"name":"Rohit","address":"bageshwar"}
print(dict["id"])
data=json.dumps(dict,indent=2)
# print(data["id"])
print(data)
data=json.loads(data)
print(data["name"])

print(sys.path)

shutil.copy()
shutil.copy2()
shutil.move()