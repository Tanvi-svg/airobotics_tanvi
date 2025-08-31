from gpiozero import RGBLED
from time import sleep

rgb= RGBLED(16,20,21,pwm= True,active_high=False)

try:
    while True:
#         rgb.value=(1,0,0)
#         sleep(1)
#         rgb.value=(0,1,0)
#         sleep(1)
#         rgb.value=(0,0,1)
#         sleep(1) also anode is postive of rgb led and the pins are red,green,blue, and positive
                    #cathode is the vice versa of it

        rgb.red=0.9
        rgb.green=0.2
        rgb.blue=0.1
        
        
except:
    rgb.close()
