from mfrc522 import SimpleMFRC522 #writing data to the tag

r = SimpleMFRC522()

try:
    t = input('new data:')
    print("now place your tag to write")
    r.write(t)
    print("Written")
finally: #no matter whether error occurs or not it will execute the code wruitten under it.
    print("exit")
    