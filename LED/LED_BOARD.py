from gpiozero import LEDBoard
from time import sleep

board= LEDBoard(12,1,7,8,25,24,23,18,15,14,pwm= True)

try:
    while True:
#         board.value=(1,0,1,0,1,0,1,0,1,0)
        board.off()
        board.on(0,2,4,6,8)
        sleep(1.0)
#         board.value=(0,1,0,1,0,1,0,1,0,1)
        board.off()
        board.on(1,3,5,7,9)
        sleep(1)
except:
    board.close()