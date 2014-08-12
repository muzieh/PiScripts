import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

print "Start loop"
try:

	while True:
		print "Set Output False"
		GPIO.output(7, False)
		time.sleep(1)
		print "Set Output True"
		GPIO.output(7,True)
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
	print "cleanup"
