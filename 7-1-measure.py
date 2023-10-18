import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

dac=[8, 11, 7, 1, 0, 5, 12, 6]
leds=[2, 3, 4, 17, 27, 22, 10, 9]
comp =14
troyka = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial =1)

def decimal_2_binary(value):
    signals = [int(element) for element in bin(value)[2:].zfill(8)]
    GPIO.output(leds, signals)

def value_troyka():
    signals =[0, 0, 0, 0, 0, 0, 0, 0]
    value = 0
    volt = 0
    for i in range(8):
        signals[i] = 1
        GPIO.output(dac, signals)
        time.sleep(0.005)
        comp_v=GPIO.input(comp)
        if comp_v==1:
            signals[i]=0
        else:
            value+=2**(7-i)
    volt = value/256*3.3
    decimal_2_binary(value)
    return volt

try:
    old_dimension=[]
    new_dimension = []
    times=[]
    time_start=time.time()
    cur_volt = value_troyka()
    times.append(0.0)
    old_dimension.append(int(cur_volt*256/3.3))
    new_dimension.append(cur_volt)
    max_Voltage = 0

    while time.time()-time_start<15.00:
        cur_volt = value_troyka()
        max_Voltage = max(max_Voltage, cur_volt)
        new_dimension.append(cur_volt)
        old_dimension.append(int(cur_volt*256/3.3))
        times.append(time.time()-time_start)
        print(cur_volt)

    GPIO.output(troyka, 0)

    while time.time() - time_start < 25.00:
        cur_volt = value_troyka()
        max_Voltage = max(max_Voltage, cur_volt)
        times.append(time.time()-time_start)
        new_dimension.append(cur_volt)
        old_dimension.append(int(cur_volt*256/3.3))
        print(cur_volt)

    time_of_experiment = time.time()-time_start

    quant = 3.3/256
    discret = len(new_dimension)/time_of_experiment

    with open("settings.txt", 'w') as f2:
        f2.write("средняя частота дискретизации:" +str(discret)+'\n')
        f2.write("шаг квантования АЦП:" +str(quant) + '\n')

    print("общая продожительность:", time_of_experiment)
    print("период одного измерения:", time_of_experiment/len(new_dimension))
    print("средняя частота дискретизации:", discret)
    print("частота квантования:", quant)
    old_dimension_str=[str(item) for item in old_dimension]
    with open("data.txt", "w")as outfile:
        outfile.write("\n".join(old_dimension_str))
    plt.title('capacitor voltage versus time')
    plt.xlabel('time', fontsize=16)
    plt.ylabel('capacitor voltage', fontsize = 16)
    plt.grid(which='major')
    plt.plot( new_dimension)
    plt.show()

finally:
    GPIO.setup(dac, 0)
    GPIO.cleanup()



