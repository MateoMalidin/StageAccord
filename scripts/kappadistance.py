# programme de visualisation des resultats simules (kappaTV)
import numpy as np
import matplotlib.pyplot as plt

# tableau des noms des corpus
corpus = ["coref", "similarite", "opinion", "emotion", "newsletter"]

for c in corpus: # pour chaque corpus
    file = open("kappaTV_" + c + ".csv", "r") # ouverture du fichier de resultats
    lines = file.readlines() # lecture du ficnier
    file.seek(0) # reinitialisation du pointeur de caracteres

    x = (len(lines) - 1)*[0] # tableau des abcisses
    y = (len(lines) - 1)*[0] # tableau des ordonnes

    for i in range(1, len(lines)): # pour chaque ligne de donnees
        line = lines[i] # ligne de donnees
        tab = line.split(",") # tableau de donnees
        x[i - 1] = float(tab[0]) # stockage de l'abcisse
        y[i - 1] = float(tab[1]) # stockage de l'ordonne

    plt.plot(x, y, label = c) # tracage de la courbe
    file.close() # fermeture du fichier courant

# mise en forme du graphique
plt.title("kappaTV -> taux -> 5 classes -> 5 annotateurs")
plt.xlabel("kappaTV")
plt.ylabel("taux")
plt.xlim([0.2, 0.9])
plt.ylim([0.0, 0.4])
plt.xticks([0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
plt.yticks([0.0, 0.1, 0.2, 0.3, 0.4])
plt.legend()
# sauvegarde du graphique
plt.savefig("kappaTV.png")
# affichage du graphique
plt.show()
