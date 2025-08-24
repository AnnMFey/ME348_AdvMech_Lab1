#based off of https://www.instructables.com/Raspberry-Pi-Tutorial-How-to-Blink-an-LED/
#we (and everyone else) will be using the Rpi.GPIO library written by Ben Crosten (documentation: https://pypi.org/project/RPi.GPIO/)
#Ben also runs a brewery where he uses Rpi to controll his process! (https://magpi.raspberrypi.com/articles/brewing-beer-raspberry-pi)

import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
while True:
   GPIO.output(18,GPIO.HIGH)
   print ("LED ON")
   sleep(1)
   GPIO.output(18,GPIO.LOW)
   print ("LED OFF")
   sleep(1)
