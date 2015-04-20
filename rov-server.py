__author__ = 'dbailey6'

import RPi.GPIO as GPIO
import time
import network
import motor

SWITCH = 10
GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH, GPIO.IN)

def heard(phrase):
	print "heard:" + phrase
	for a in phrase:
		if a == "\r" or a == "\n":
			pass # strip it
		else:
			if GPIO.input(SWITCH):
				network.say("1")
			else:
				network.say("0")

while True:
	print "waiting for connection"
	network.wait(whenHearCall=heard)
	print "connected"

	while network.isconnected():
		print "server is running"
		time.sleep(1)
	
	print "connection closed"

frontRight = motor(1, 2)
