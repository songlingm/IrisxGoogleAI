
import wiringpi
import time
import sys
from wiringpi import GPIO

wiringpi.wiringPiSetup()

NUM = 2

wiringpi.pinMode(NUM, GPIO.OUTPUT)

while True:
    try:
        wiringpi.digitalWrite(NUM, GPIO.HIGH)
        time.sleep(0.125)
        wiringpi.digitalWrite(NUM, GPIO.LOW)
        time.sleep(0.125)
    except KeyboardInterrupt:
        print("\nexit")
        sys.exit(0)
