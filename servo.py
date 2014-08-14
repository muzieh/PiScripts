import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)


p = GPIO.PWM(7,50)
p.start(7.5)
time.sleep(2)
print "Start loop"
try:

	while True:
	       current = 2.5
	       
	       while current < 12.5:
		  p.ChangeDutyCycle(current)
		  time.sleep(0.003)
		  current += 0.1
	       current = 12.0
	       while current > 2.5:
		  p.ChangeDutyCycle(current)
		  time.sleep(0.003)
		  current -= 0.1

except KeyboardInterrupt:
     GPIO.cleanup()
     print "cleanup"
