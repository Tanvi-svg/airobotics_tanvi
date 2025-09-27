from mfrc522 import SimpleMFRC522 # reading data from tag

r = SimpleMFRC522()

try:
    uid,data=r.read() #unique id and data
    print(f"ID: {uid}   Data: {data}")#formatted string

finally:
    print("EXIT")