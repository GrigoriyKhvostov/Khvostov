import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
leds=[2, 3, 4, 17, 27, 22, 10, 9]
comp=14
troyka=13
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial =1)
GPIO.setup(comp, GPIO.IN)
def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
def les   ():
    brevno=[0,0,0,0,0,0,0,0]
    for k in range (8):
        
        brevno[k]=1
        GPIO.output(dac,brevno)
        time.sleep(0.01)
        if(1==GPIO.input(comp)):
            brevno[k]=0
    return(brevno)
def ckamen():
    derevo=0
    vetcka= 128
    brevno=les()
    for d in range (0, 8, 1):
        derevo = derevo + brevno[d]*vetcka
        vetcka = vetcka//2
    return (derevo)

try:
    while(0<6):
        a=ckamen()
       
        print(a, " ",  a*3.3/256)
        GPIO.output(leds,les())
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()