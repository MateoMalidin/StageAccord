import numpy as np
import matplotlib.pyplot as plt

corpus = ["coref", "similarite", "opinion", "emotion", "newsletter"]
for c in corpus:
    file = open("kappaTV_" + c + ".csv", "r")
    lines = file.readlines()
    file.seek(0)

    x = (len(lines) - 1)*[0]
    y = (len(lines) - 1)*[0]


    for i in range(1, len(lines)):
        line = lines[i]
        tab = line.split(",")
        x[i - 1] = float(tab[0])
        y[i - 1] = float(tab[1])

    plt.plot(x, y, label = c)
    file.close()

plt.title("kappaTV -> taux -> 5 classes -> 5 annotateurs")
plt.xlabel("kappaTV")
plt.ylabel("taux")
plt.xlim([0.2, 0.9])
plt.ylim([0.0, 0.4])
plt.xticks([0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
plt.yticks([0.0, 0.1, 0.2, 0.3, 0.4])
plt.legend()
plt.savefig("kappaTV.png")
plt.show()

