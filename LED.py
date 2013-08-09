import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

GPIO.output(5,GPIO.HIGH)
time.sleep(1)
GPIO.output(5,GPIO.LOW)
time.sleep(1)
GPIO.output(7,GPIO.HIGH)
time.sleep(1)
GPIO.output(7,GPIO.LOW)

GPIO.cleanup()
