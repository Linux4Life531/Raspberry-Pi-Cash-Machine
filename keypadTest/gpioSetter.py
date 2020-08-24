import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

while True:
    pin = int(input("ENTER PIN NUMBER: "))
    value = int(input("ENTER PIN VALUE (1 OR 0): "))
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, value)