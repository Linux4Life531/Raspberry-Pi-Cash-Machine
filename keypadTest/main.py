import RPi.GPIO as GPIO
# from EmulatorGUI import GPIO
import time

L1 = 5
L2 = 6
L3 = 13
L4 = 19

C1 = 12
C2 = 16
C3 = 20
C4 = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def readLine(lineNumber, line, characters):
    GPIO.output(line, GPIO.HIGH)
    if (GPIO.input(C1) == GPIO.HIGH):
        print(characters[0])
    if (GPIO.input(C2) == GPIO.HIGH):
        print(characters[1])
    if (GPIO.input(C3) == GPIO.HIGH):
        print(characters[2])
    if (GPIO.input(C4) == GPIO.HIGH):
        print(characters[3])
    GPIO.output(line, GPIO.LOW)

try:
    while True:
        readLine(1, L1, ["1","4","7","*"])
        readLine(2, L2, ["2","5","8","0"])
        readLine(3, L3, ["3","6","9","#"])
        readLine(4, L4, ["A","B","C","D"])
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nApplication stopped!")