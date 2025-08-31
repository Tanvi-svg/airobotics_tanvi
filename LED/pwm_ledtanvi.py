from gpiozero import PWMLED

led=PWMLED(18)

try:
    while True:
        brightness=float(input())
        led.value=brightness

except:
    led.close()