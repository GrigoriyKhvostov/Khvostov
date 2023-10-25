import numpy as np 
import matplotlib.pyplot as plt


#with open("data.txt", "r") as data:
 #  voltage=[float(i) for i in data.read().split("\n")]
#voltage*3.3/256
data_array = np.loadtxt("data.txt", dtype=int)
hren=np.loadtxt("settings.txt", dtype=float)
data_array=data_array*hren[1]
time=np.linspace(0, 25.038, 606)

fig, ax = plt.subplots(figsize=(16, 10), dpi=400)
plt.title('Процесс зарядки и разрядки конденсатора')
plt.xlabel("Время, с")
plt.ylabel("Напряжение, В")
plt.legend("V(t)")
plt.minorticks_on()
plt.grid(which="major", color = "#444", linewidth=1)
plt.grid(which="minor", color = "#aaa", ls=":")
plt.figtext(0.3, 0.4, "Время зарядки = 11.29 с; Время разрядки = 13.75 с", fontsize=20, bbox={"boxstyle":"square", 'facecolor': "#AAAAFF"})
ax.set_xlim(0, 25)

plt.plot(time, data_array, lw =3, marker='o', mfc='blue', markersize=5, mec = "blue", color="red", linestyle="-",markevery=20)
fig.savefig("graph.svg")
plt.show()