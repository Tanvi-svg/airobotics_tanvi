from time import sleep
import serial

a= serial.Serial("/dev/ttyACM0",9600)#getting data from arduino port

a.reset_input_buffer()#clear data in the serial buffer

try:
    while True:
        try:
            data= a.readline()#reads the data and gives it to raspberry pi and uses /n delimeter to divide data
            data=data.strip(b"\r\n")#strip away the byte (\r\n)
            data=float(data)#float value to make it not into a byte string
            print(data)
            sleep(0.05)
        except ValueError:
            a.reset_input_buffer()
except KeyboardInterrupt:
    print("exit")
    a.close()