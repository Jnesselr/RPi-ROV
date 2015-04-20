__author__ = 'dbailey6'

import Rpi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

class motor:
    """Hopefully a working motor class"""
# initializes the motor
    def __init__(self, pinDir, pinPWM):
        self.dirPin = pinDir
        self.pwmPin = pinPWM
        GPIO.setup(self.dirPin, GPIO.OUT)
        GPIO.output(self.dirPin, GPIO.LOW)
        GPIO.setup(self.pwmPin, GPIO.OUT)

        self.pwmControl = GPIO.PWM(self.pwmPin, 10000)
        self.pwmControl.start(0)

#controls motion forward at duty cycle set by speed
    def forward(self, speed):
        GPIO.output(self.dirPin, GPIO.LOW)
        self.pwmControl.ChangeDutyCycle(speed)
        print("Motor Forward at " + speed + "% duty cycle")

#controls motion reverse at duty cycle set by speed
    def reverse(self, speed):
        GPIO.output(self.dirPin, GPIO.HIGH)
        self.pwmControl.ChangeDutyCycle(speed)
        print("Motor Reverse at " + speed + "% duty cycle")
#stops motor
    def stop(self):
        self.pwmControl.ChangeDutyCycle(0)
        print("Motor is stopped")

    def __exit__(self):
        self.pwmControl.stop()