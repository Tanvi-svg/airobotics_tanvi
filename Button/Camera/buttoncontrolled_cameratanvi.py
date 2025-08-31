from gpiozero import Button
from picamera2 import Picamera2,Preview
from time import time,sleep

button=Button(16)

picam2=Picamera2()
picam2.start_preview(Preview.QTGL)
picam2.start()

def capture():
    picam2.capture_file(f"myface_{time()}.jpg")
    sleep(0.1)

try:
    while True:
        button.when_pressed=capture

except:
    button.close()
    picam2.stop_preview()
    picam2.stop()