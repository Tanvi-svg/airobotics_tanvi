from time import sleep
import busio
import board
import adafruit_vl53l0x

i2c=busio.I2C(board.SCL,board.SDA)#make an i2c bus instance for the data we r getting from the gpio pins 2 and 3
vl53= adafruit_vl53l0x.VL53L0X(i2c)

try:
    while True:
        print(f"Distance: {vl53.range}mm")
        sleep(0.2)
except KeyboardInterrupt:
    print("exit")