import BlynkLib
from gpiozero import LED
from BlynkTimer import BlynkTimer

BLYNK_AUTH_TOKEN = 'ntMGqXKboNOEglmYw47XpSsDjXcfEKgH'

led = LED(18)

blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)


@blynk.on("V0")#some event will happen
def v0_write_handler(value):
    led.value = float(value[0])
    
@blynk.on("connected")
def blynk_connected():
    
    print("Raspberry pi connected to new Blynk")
    
while True:
    blynk.run()