from gpiozero import LEDBarGraph
from time import sleep

graph= LEDBarGraph(12,1,7,8,25,24,23,18,15,14,pwm = True)

try:
    while True:
        board= float(input())
        graph.value=board

except:
    print("unexpected error")
    graph.close()