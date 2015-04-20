__author__ = 'dbailey6'

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

class Sonar:
    """Those should be a functional sonar function. For use with XL-MaxSonar-WR/WRC by MaxBotix Inc"""
    """ I'll be using it in Serial Mode Only"""
    #initializes the pins for the sonar
    def __init__(self, dataTypePin, pwmPin, analogPin, readTogglePin, rangeDataPin):
        self.pin1 = dataTypePin
        self.pin2 = pwmPin
        self.pin3 = analogPin
        self.RXpin4 = readTogglePin
        self.TXpin5 = rangeDataPin

        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.output(self.pin1, GPIO.HIGH)

        GPIO.setup(self.pin2, GPIO.IN)
        GPIO.output(self.pin2, GPIO.LOW)

        GPIO.setup(self.pin3, GPIO.IN)
        GPIO.output(self.pin3, GPIO.LOW)

        GPIO.setup(self.RXpin4, GPIO.OUT)
        GPIO.output(self.RXpin4, GPIO.LOW)

        GPIO.setup(self.TXpin5, GPIO.SERIAL)

    def startReading(self):
        GPIO.output(self.RXpin4, GPIO.HIGH)
        #the serial output needs to be handled here somehow

    def stopReading(self):
        GPIO.output(self.RXpin4, GPIO.LOW)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stopReading()