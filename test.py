import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.output(18, GPIO.HIGH)
GPIO.input(18)  # returns 1

GPIO.output(18, GPIO.LOW)
GPIO.input(18)  # returns 0

###