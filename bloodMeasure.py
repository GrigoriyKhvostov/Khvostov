import bloodFunctions as b
import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
b.initSpiAdc()

try:
    old_dimension=[]
    time_start=time.time()
    
    while time.time()-time_start<60.00:
        cur_volt = b.getAdc()
        
        old_dimension.append(cur_volt)
    old_dimension_str=[str(item) for item in old_dimension]
    
    with open("data_nagruz.txt", "w")as outfile:
        outfile.write("\n".join(old_dimension_str))
    plt.plot(old_dimension)
    plt.show()
finally:
    b.deinitSpiAdc()
   
    GPIO.cleanup()