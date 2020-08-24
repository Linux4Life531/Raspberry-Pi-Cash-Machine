import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

MATRIX = [
    [1, 2, 3, "A"],
    [4, 5, 6, "B"],
    [7, 8, 9, "C"],
    ["*", 0, "#", "D"] ]

ROW = [5, 6, 13, 19]
COL = [12, 16, 20, 21]

for j in range(4):
    GPIO.setup(COL[j], GPIO.OUT)
    GPIO.output(COL[j], 1)

for i in range(4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
    while True:
        for j in range(4):
            GPIO.output(COL[j], GPIO.LOW)

            for i in (range(4)):
                if GPIO.input(ROW[i]) == 1:
                    print(str(MATRIX[i][j]))
                    while(GPIO.input(ROW[j]) == 1):
                        pass
            GPIO.output(COL[j], GPIO.HIGH)

except KeyboardInterrupt:
    GPIO.cleanup()