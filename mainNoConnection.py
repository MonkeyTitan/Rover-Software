#imports
import ServoCommands
import time

#Object creation
Servo = ServoCommands.Servo()

#Function execution
Servo.setConfig()
Servo.pwm.start(0)
time.sleep(2)
Servo.open()
time.sleep(5)
Servo.close()
Servo.pwm.stop()
time.sleep(2)