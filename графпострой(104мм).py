from matplotlib import pyplot as plt
import numpy as np
import math
from textwrap import wrap

data = []
height = []
time = []
#adc = open('value_104.txt', 'r')
with open('value_104.txt', 'r') as file:
    for line in file:
        cur_data = float(line)
        data.append(cur_data)

size = len(data)

for i in range(0, size):
    y = data[i]
    cur_h = -1.03051956*0.00001*y**3 + 1.35238127*0.01*y**2-4.43828980*y + 4.31300364*100
    height.append(cur_h)
    x = i
    cur_time = x*15/size
    time.append(cur_time)


plt.plot(time[1::], height[1::], '-', c ='red')
plt.grid(which='major', color = 'gray', linewidth = 0.5)
plt.minorticks_on()
plt.grid(which='minor', color = 'dimgray', linestyle = ':')

plt.title("\n".join(wrap('График зависимости уровня воды от времени (h0=80мм)', 35)), loc = 'center', fontsize = 10)
plt.ylabel("Уровень воды, мм", fontsize = 10)
plt.xlabel("Время,с", fontsize = 10)
plt.scatter (x , y, c = 'cornflowerblue', label = 'Измерения')


plt.xlim(xmin=0, xmax=15)
plt.ylim(ymin = 0, ymax = 120)


plt.show()