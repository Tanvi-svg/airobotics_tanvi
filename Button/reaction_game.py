from gpiozero import LED,Button
from time import sleep
from random import uniform

b1= Button(14)
b2= Button(15)
l= LED(18)

try:
    while True:
        duration= uniform(5,10)#creates a random decimal number not an interger
        sleep(duration)
        
        l.on()
        while True:
            if b1.is_pressed:
                print("p1 wins")
                break
                
            elif b2.is_pressed:
                print("p2 wins")
                break
        l.off()
except KeyboardInterrupt:
    b1.close()
    b2.close()
    l.close()