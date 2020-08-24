from RPLCD import CharLCD
from time import sleep
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
lcd = CharLCD(numbering_mode=GPIO.BCM, cols=16, rows=2, pin_rs=4, pin_e=17, pins_data=[27, 18, 23, 26])

def writeToLCD(text):
    lcd.clear()
    lcd.write_string(text)

try:
    while True:
        writeToLCD("Testing")
        sleep(1)
        lcd.clear()
except KeyboardInterrupt:
    GPIO.cleanup()
