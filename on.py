import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(14,GPIO.OUT)
#GPIO.output(14,1) #off
GPIO.output(14,0) #on
print GPIO.input(14)