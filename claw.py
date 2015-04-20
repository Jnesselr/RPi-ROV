__author__ = 'dbailey6'

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

class Claw:
    """Hopefully a working claw class"""
    # initializes the claw
    def __init__(self, pinDir, pinPower):
        self.dirPin = pinDir
        self.pwrPin = pinPower
        GPIO.setup(self.dirPin, GPIO.OUT)
        GPIO.output(self.dirPin, GPIO.LOW)
        GPIO.setup(self.pwrPin, GPIO.OUT)
        GPIO.output(self.pwrPin, GPIO.LOW)

    def open(self):
        GPIO.output(self.dirPin, GPIO.LOW)
        GPIO.output(self.pwrPin, GPIO.HIGH)
        print("Claw is opening")

    def close(self):
        GPIO.output(self.dirPin, GPIO.HIGH)
        GPIO.output(self.pwrPin, GPIO.HIGH)
        print("Claw is closing")

    def stop(self):
        GPIO.output(self.pwrPin, GPIO.LOW)
        print("Claw has stopped")

    def __exit__(self):
        self.stop()