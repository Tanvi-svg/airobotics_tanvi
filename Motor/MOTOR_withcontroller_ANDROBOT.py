from gpiozero import Motor,Robot
from time import sleep

r= Robot(Motor(23,24),Motor(5,6))

try:
    while True:
        r.forward()
        sleep(3)
        r.stop()
        sleep(2)
        r.backward()
        sleep(3)
        r.stop()
        sleep(2)
        r.left()
        sleep(3)
        r.stop()
        sleep(2)
        r.right()
        sleep(3)
        r.stop()
        sleep(2)
        
except KeyboardInterrupt:
    r.close()
