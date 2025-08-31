from gpiozero import DistanceSensor
from time import sleep

sense=DistanceSensor(16,20)

try:
    while True:
        print(round(sense.distance*100,2))
        sleep(0.1)
        
except:
    sense.close()