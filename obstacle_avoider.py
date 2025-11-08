from time import sleep
from gpiozero import DigitalOutputDevice,PWMOutputDevice,DigitalInputDevice

pwm_b= PWMOutputDevice(13)
pwm_a= PWMOutputDevice(12)

bin1= DigitalOutputDevice(5)
bin2= DigitalOutputDevice(6)

ain1= DigitalOutputDevice(24)
ain2= DigitalOutputDevice(23)

pwm_a.value= 0.5
pwm_b.value= 0.5

ls= DigitalInputDevice(22)
ms= DigitalInputDevice(27)
rs= DigitalInputDevice(17)

def forward():
    bin1.value= 1
    bin2.value= 0
    ain1.value=1
    ain2.value=0
    

def backward():
    bin1.value= 0
    bin2.value= 1
    ain1.value=0
    ain2.value=1
    

def left():
    bin1.value= 0
    bin2.value= 1
    ain1.value=1
    ain2.value=0
    

def right():
    bin1.value= 1
    bin2.value= 0
    ain1.value=0
    ain2.value=1
    

def stop():
    bin1.value= 1
    bin2.value= 1
    ain1.value=1
    ain2.value=1
    
try:
    while True:
        lv= ls.value
        mv= ms.value
        rv= rs.value
        
        if lv and mv and rv: #all values are 1(no obstacle detected
            forward()
            
        elif lv and mv and not rv:
            backward()
            sleep(0.5)
            left()
            sleep(0.5)
            
        elif lv and not mv and rv:
            backward()
            sleep(0.5)
            left()
            sleep(0.5)
            
        elif lv and not mv and not rv:
            backward()
            sleep(0.5)
            left()
            sleep(0.5)
            
        elif not lv and mv and rv:
            backward()
            sleep(0.5)
            right()
            sleep(0.5)
            
        elif not lv and mv and not rv:
            backward()
            sleep(0.5)
            right()
            sleep(0.5)
            
        elif not lv and not mv and rv:
            backward()
            sleep(0.5)
            right()
            sleep(0.5)
        
        elif not lv and not mv and not rv:
            backward()
            sleep(0.5)
            right()
            sleep(0.5)
            
finally:
    pwm_a.close()
    pwm_b.close()
    ain1.close()
    ain2.close()
    bin1.close()
    bin2.close()
    ls.close()
    ms.close()
    rs.close()
    