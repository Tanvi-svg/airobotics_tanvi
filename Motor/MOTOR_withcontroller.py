from gpiozero import Motor
from time import sleep

m=Motor(23,24)

try:
    while True:
        m.forward()
        sleep(3)
        m.stop()
        sleep(2)
        m.backward()
        sleep(3)
        m.stop()
        sleep(2)
        
except KeyboardInterrupt:
    m.close()