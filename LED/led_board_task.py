from gpiozero import LEDBoard
from time import sleep

graph= LEDBoard(12,1,7,8,25,24,23,18,15,14,pwm = True)

try:
    while True:
        a= input()
        b= a.split(",")#delimeters are used to seperate the numbers when we enter it in
        c=[float(i) for i in b]#list comprehension, so all the numbers that r entered is a float value
        graph.value= c

except:
    print("unexpected error")
    graph.close()
