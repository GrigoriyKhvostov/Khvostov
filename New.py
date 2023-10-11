import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
DAC = 21
led = 27
GPIO.setup(DAC,GPIO.OUT)
GPIO.setup(led,GPIO.OUT)
GPIO.output(DAC,0)

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]
val =0
T=3
step=1
pwm0=GPIO.PWM(DAC,1000)
pwm1=GPIO.PWM(led,1000)
pwm0.start(0)
pwm1.start(0)
try:
    while(True):
        val = int(input())
        # val+=step
        # if val==100 or val ==0:
        #     step = -step
        pwm0.ChangeDutyCycle(val)
        pwm1.ChangeDutyCycle(val)

        print("{:.4f} V".format(val/100*3.3))
        # time.sleep(0.2)
finally:
    GPIO.output(DAC,0)
    GPIO.cleanup()