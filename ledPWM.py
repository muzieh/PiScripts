import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

p = GPIO.PWM(7,50)
p.start(0.0)

print "Start loop"
try:

   while True:
      bri = 0.0
      while bri < 100.0:
	 p.ChangeDutyCycle(bri)
	 time.sleep(0.0001)
	 bri += 0.01

except KeyboardInterrupt:
   GPIO.cleanup()
   print "cleanup"
