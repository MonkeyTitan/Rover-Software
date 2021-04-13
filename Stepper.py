#imports
import time
import Jetson.GPIO as GPIO

#Class creation
class Servo:
    def __init__(self):
        self.outputPin = 33

    def setConfig(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.outputPin, GPIO.OUT)
        self.pwm = GPIO.PWM(33, 333)

    def open(self):
        self.pwm.ChangeDutyCycle(5)

    def close(self):
        self.pwm.ChangeDutyCycle(0)