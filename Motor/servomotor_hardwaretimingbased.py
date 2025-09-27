from gpiozero import AngularServo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory #to reduce jittering

f= PiGPIOFactory()
s= AngularServo(15,pin_factory=f)#directly controlling the pin with hardware pwm

try:
    while True:
        a= int(input("Please enter number"))#-90 to 90 degrees
        s.angle= a
        
except KeyboardInterrupt:
    s.close()
    