import RPi.GPIO as GPIO
import time

def decimal_2_bunary(value):
    return [ int(element) for element in bin(value)[2:].zfill(8)]

def abc():
    signals = [0, 0, 0, 0, 0, 0, 0, 0]
    value = 0
    volt = 0
    for i in range(8):
        signals[i] = 1
        GPIO.output(dac, signals)
        time.sleep(0.0007)
        comp_v = GPIO.input(comp)
        if comp_v == 1:
            signals[i] = 0
        else:
            value += 2**(7-i)
    volt = value /256 * 3.3
    print("цифровое значение: ", value, signals, " напряжение: ", volt)
    return volt



dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
leds = leds[::-1]
comp = 14
troyka = 13 

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        time.sleep(0.007)
        GPIO.output(leds, 0)
        volt = abc()
        count_leds = int((volt*9)//3.3)
        print(count_leds)
        work_leds = leds[:count_leds]
        #GPIO.output(leds, 0)
        GPIO.output(work_leds, 1)
        




finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()