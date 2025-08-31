from gpiozero import LED
from time import sleep
from bluedot import BlueDot

v= LED(14)
b= BlueDot()

try:
    while True:
        b.when_pressed=v.on
        b.when_released=v.off

except:
    v.close()
    