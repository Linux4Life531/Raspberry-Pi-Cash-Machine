from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
reader = SimpleMFRC522()

def readFromReader():
    print("Hold a tag near the reader")
    id, text = reader.read()
    return id, text

try:
    while True:
        id, text = readFromReader()
        print("ID: %s\nText: %s" % (id,text))
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise