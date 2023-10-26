import wiringpi
import time
import sys
from wiringpi import GPIO

wiringpi.wiringPiSetup()

NUM = 2

wiringpi.pinMode(NUM, GPIO.OUTPUT)
wiringpi.digitalWrite(NUM, GPIO.LOW)
