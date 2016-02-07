#import RPi.GPIO library as GPIO
import RPi.GPIO as GPIO
#Set GPIO numbering scheme to pinnumber
GPIO.setmode(GPIO.BOARD)
#setup pin 14 as an output
GPIO.setup(14,GPIO.OUT)
#lights off
GPIO.output(14,GPIO.HIGH)

#lights on
#GPIO.output(14,GPIO.LOW)

print GPIO.input(14)