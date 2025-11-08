from time import sleep
from gpiozero import Robot,Motor,PWMOutputDevice
from bluedot import BlueDot
from signal import pause

blue= BlueDot()

pwm_a= PWMOutputDevice(13)

pwm_b= PWMOutputDevice(12)

robot = Robot(Motor(5,6),Motor(24,23))

pwm_a.value = 1
pwm_b.value = 1

def run(pos):
    if pos.top:
        robot.forward(pos.distance)
    elif pos.bottom:
        robot.backward(pos.distance)
    elif pos.left:
        robot.left(pos.distance)
    elif pos.right:
        robot.right(pos.distance)

try:
    blue.when_pressed= run
    blue.when_moved= run
    blue.when_released= robot.stop
    
    pause()
    
finally:
    robot.close()
    pwm_a.close()
    pwm_b.close()