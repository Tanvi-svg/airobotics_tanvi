from gpiozero import Button,LED

button=Button(16)
led=LED(18)

try:
    while True:
#         button.when_pressed=led.toggle
        button.when_pressed=led.on
        button.when_released=led.off
except:
    led.close()
    button.close()