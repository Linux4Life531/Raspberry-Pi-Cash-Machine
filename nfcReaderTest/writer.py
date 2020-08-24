# Import the library
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

# Get the reader
reader = SimpleMFRC522()

def writeToReader(text):
        reader.write(text)

# Add the cards, and then exit properly
try:
        text = input('New data:')
        print("Now place your tag to write")
        writeToReader(text)
        print("Written")
finally:
        GPIO.cleanup()