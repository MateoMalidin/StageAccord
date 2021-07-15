import matplotlib.pyplot as plt
import numpy as np

# tableau des noms des corpus
corpus = ['coref', 'similarite', 'opinion', 'emotion', 'newsletter']

# tableau des abcisses
X = []
# tableau des ordonnes
Y = []

# pour chaque corpus
for c in corpus:
    file = open(c + '_res_brute.csv', 'r') # ouverture du fichier
    line = file.read() # données du fichier
    tab = line.split(',') # tableau des données
    x = round(float(tab[0]), 2) # abcisse
    y = round(float(tab[1]), 2) # ordonne
    X.append(x)
    Y.append(y)
    plt.plot(x, y, marker='o', label = c) # tracage de la courbe

# moyenne des x et moyenne des y
moyx = 0
moyy = 0
for i in range(len(X)):
    moyx += X[i]
    moyy += Y[i]
moyx = moyx / len(X)
moyy = moyy / len(Y)

# calcul de la droite des moindres carres

# calcul du coefficient a

num = 0
for i in range(len(X)):
    num += (X[i] - moyx)*(Y[i] - moyy)

denom = 0
for i in range(len(X)):
    denom += (X[i] - moyx)**2

a = num / denom

# calcul du coefficient b

b = moyy - a*moyx

# equation de la droite des moindres carres

def f(x):
    return a*x + b

# tracage de la droite des moindres carres

abcisse = [0.0, 0.9]
ordonne = [f(0.0), f(0.9)]

plt.plot(abcisse, ordonne)

# mise en forme du graphique
plt.title('kappa / taux de variation de la reference (1000 groupes)')
plt.legend() 
plt.xlabel("kappa")
plt.xlim(0.0, 0.9)
plt.ylabel("taux")
plt.ylim(0.0, 0.5)

# affichage du graphique
plt.show()
