from gpiozero import Button
from picamera2 import Picamera2,Preview


picam2=Picamera2()
picam2.start_preview(Preview.QTGL)
picam2.start()


try:
    while True:
      picam=picam2.start()

except:
    button.close()
    picam2.stop_preview()
    picam2.stop()