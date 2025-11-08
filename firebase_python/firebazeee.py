import firebase_admin
from firebase_admin import db, credentials
from time import sleep
from datetime import datetime
from random import uniform

#authenticate firebase
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred,{"databaseURL": "https://raspberrrrrrypi-default-rtdb.asia-southeast1.firebasedatabase.app/"})


ref = db.reference("/")

#ref.set(({}))

while True:
    now = datetime.now()
    date_time = now.strftime("%d%m%Y%H%M%S")
    data = round(uniform(10,100),2)
    ref.push({"Timestamp":date_time, "Data":data})
    sleep(0.25)
    