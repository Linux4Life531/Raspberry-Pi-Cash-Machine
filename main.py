## Include files & libraries ##

import json
import os

## Basic Setup ##

from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

## LCD Setup ##

from RPLCD import CharLCD
global lcd
lcd = CharLCD(numbering_mode=GPIO.BCM, cols=16, rows=2, pin_rs=4, pin_e=17, pins_data=[27, 18, 23, 26])

## NFC Setup ##

from mfrc522 import SimpleMFRC522

global reader
reader = SimpleMFRC522()

## Keypad Setup ##

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

## Needed Functions ##

def writeToLCD(text):
    lcd.clear()
    lcd.write_string(text)

def readFromReader():
    id, text = reader.read()
    return id, text

def writeToReader(text):
    reader.write(text)

def readLine(lineNumber, line, characters):
    finalString = ""
    GPIO.output(line, GPIO.HIGH)
    if (GPIO.input(C1) == GPIO.HIGH):
        finalString = finalString + (characters[0])
    if (GPIO.input(C2) == GPIO.HIGH):
        finalString = finalString + (characters[1])
    if (GPIO.input(C3) == GPIO.HIGH):
        finalString = finalString + (characters[2])
    if (GPIO.input(C4) == GPIO.HIGH):
        finalString = finalString + (characters[3])
    GPIO.output(line, GPIO.LOW)
    return finalString

def readFromKeypad(length):
    outputtedString = ""
    stringFinished = False
    while (stringFinished!=True):
        outputtedString = outputtedString + readLine(1, L1, ["1","4","7","*"])
        outputtedString = outputtedString + readLine(2, L2, ["2","5","8","0"])
        outputtedString = outputtedString + readLine(3, L3, ["3","6","9","#"])
        outputtedString = outputtedString + readLine(4, L4, ["A","B","C","D"])
        sleep(0.3)
        if (len(outputtedString) == length):
            stringFinished = True
    return(outputtedString)

## Main Program ##

def main():
    
    try:

        ## Define the variables ##

        cardScanned = False
    
        ## Ask the user to scan ##

        writeToLCD("Scan your card")
    
        ## Get the data from the JSON scanner ##

        with open('data.json') as json_file:
            userData = json.load(json_file)

        names = []
        ids = []
        code = []
        money = []
            
        print(userData)

        ## Get the data from the scanner ##
        
        id, text = readFromReader()

        ## Use that data to get the user info ##

        if str(id) in userData:
            currentName = userData[str(id)]["Name"]
            currentPass = userData[str(id)]["PassCode"]
            currentMoney = userData[str(id)]["AmountOfMoney"]

        print(currentName)
        print(currentPass)
        print(currentMoney)

        ## Tell the user to enter the passcode ##

        writeToLCD("Hello " + currentName)
        sleep(1.5)
        writeToLCD("Enter your passcode")

        ## Read in the data ##

        inputedPass = readFromKeypad(4)

        ## Work out whether it works

        passCorrect = inputedPass == str(currentPass)
        print(str(passCorrect) + " = " + str(inputedPass) + " and " + str(currentPass))

        ## If it is, 

        if (passCorrect):
            lcd.clear()
            for i in (range(10)):
                writeToLCD("Hi " + str(currentName))
                sleep(2)
                writeToLCD("You have " + str(currentMoney) + " pounds")
                sleep(2)
            main()
        else:
            writeToLCD("Wrong Passcode")
            sleep(1)
            main()

    ## On KeyboardInterrupt  ##    
    
    except KeyboardInterrupt:
        writeToLCD("Goodbye!")
        sleep(0.8)
        lcd.clear()
        GPIO.cleanup()
        exit()

## Run the main function on run file ##

if __name__ == "__main__":
    main()