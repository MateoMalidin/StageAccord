# programme d'interpolation et de calcul de l'ecart maximal entre les courbes
import numpy as np
import matplotlib.pyplot as plt

pas = 0.01 # intervalle entre les points interpoles

# ouverture des fichiers
coref = open('kappaTV_coref.csv', 'r')
similarite = open('kappaTV_similarite.csv', 'r')
opinion = open('kappaTV_opinion.csv', 'r')
emotion = open('kappaTV_emotion.csv', 'r')
newsletter = open('kappaTV_newsletter.csv', 'r')

# lecture des fichiers
tc = coref.readlines()
ts = similarite.readlines()
to = opinion.readlines()
te = emotion.readlines()
tn = newsletter.readlines()

# tableau les donnees des fichiers
t = [tc, ts, to, te, tn]

# reinitialisation du pointeur de caractere
coref.seek(0)
similarite.seek(0)
opinion.seek(0)
emotion.seek(0)
newsletter.seek(0)

l = len(tc) - 1 # nombre de valeurs dans un fichier

# creation des tableaux d'abcisses et d'ordonnes de chaque corpus
cx = l*[0]
cy = l*[0]
sx = l*[0]
sy = l*[0]
ox = l*[0]
oy = l*[0]
ex = l*[0]
ey = l*[0]
nx = l*[0]
ny = l*[0]

# creation des tableaux d'abcisses et d'ordonnes avec contenant les points interpoles
cxe = []
cye = []
sxe = []
sye = []
oxe = []
oye = []
exe = []
eye = []
nxe = []
nye = []

# tableaux contenant les abcisses et ordonnes de tous les corpus
x = [cx, sx, ox, ex, nx]
y = [cy, sy, oy, ey, ny]

# tableaux contenant les abcisses et ordonnes interpoles de tous les corpus
xe = [cxe, sxe, oxe, exe, nxe]
ye = [cye, sye, oye, eye, nye]

# replissages des tableaux
for i in range(len(t)): # pour chaque corpus
    c = t[i] # donnees de l'annotation
    a = x[i] # tableau d'abcisses de l'annotation
    ae = xe[i] # tableau d'abcisses avec interpolation
    o = y[i] # tableau d'ordonnes de l'annotation
    oe = ye[i] # tableau d'ordonnes avec interpolation
    for j in range(1, len(tc)): # pour chaque ligne de donnees
        v = c[j] # ligne de donnees (string)
        tab = v.split(',') # ligne de donnees (list)
        a[j-1] = round(float(tab[0]), 2) # stockage de l'abcisse arrondie aux centiemes
        o[j-1] = round(float(tab[1]), 2) # stockage de l'ordonne arrondie aux centiemes
    ae.append(a[0]) # ajout de l'abcisse au tableau d'interpolation des abcisses
    oe.append(o[0]) # ajout de l'ordonne au tableau d'interpolation des ordonnes
    for k in range(len(a)-1): # interpolation entre deux points
        x1 = a[k] # abcisse 1
        y1 = o[k] # ordonne 1
        x2 = a[k+1] # abcisse 2
        y2 = o[k+1] # ordonne 2
        m = (y2 - y1) / (x2 - x1) # coefficient directeur de l'interpolation lineaire
        p = y2 - m*x2 # ordonne a l'origine de l'interpolation lineaire
        it = x1 - pas # premiere iteration
        while it > x2: # inerpolation des points
            ae.append(round(it, 2)) # ajout de l'abcisse interpolee
            oe.append(round(m*it + p, 2)) # ajout de l'ordonne interpole
            it -= pas # decrementation du pas
        ae.append(x2) # ajout du dernier point
        oe.append(y2) # ajout du dernier point

# determination de l'espace communs a toutes les courbes
ppc = 1 # plus petit premier point commun
dgc = 0 # plus grand dernier points commun
for i in range(len(xe)): # parcours des corpus
    if xe[i][0] < ppc: # parcours des abcisses
        ppc = xe[i][0]
    if xe[i][-1] > dgc:
        dgc = xe[i][-1]

print('ppc : ', ppc)
print('dgc : ', dgc)
print('nbIt : ', int((ppc-dgc)/pas))
print('lenxe : ', len(xe))

# calcul de l'ecart maximal entre les courbes
ecartmax = 0 # ecart maximal
point = 0 # indice du point ou l'ecar est maximal
# pour toutes les combinaisons de courbes
for i in range(len(xe)): # courbe 1
    for j in range(len(xe)): # courbe 2
        if i != j:
            x1 = 0 # abcisse 1
            x2 = 0 # abcisse 2
            print('ijk0 : ', i, ':', j, ':', x1)
            # tant que les abcisses n'appartiennent pas a l'espace commun a toutes les coubes
            while xe[i][x1] > ppc:
                x1 += 1
                print('xei : ', xe[i][x1])
            while xe[j][x2] > ppc:
                x2 += 1
                print('xej : ', xe[j][x2])
            ecart = 0 # ecart entre les courbes
            # plage de valeurs a comparer
            itmax1 = x1+int((ppc-dgc)/pas)
            itmax2 = x2+int((ppc-dgc)/pas)
            # parcours des abcisses
            while x1 <= itmax1 and x2 <= itmax2:
                ecart = abs(ye[i][x1] - ye[j][x2]) # calcul de l'ecart entre les courbes
                print('yei:yej : ', ye[i][x1], ':', ye[j][x2])
                print('ecart : ', ecart)
                if ecart > ecartmax: # mise a jour de l'ecart maximal
                    ecartmax = ecart
                    point = x1
                x1 += 1 # deplacement du point 1
                x2 += 1 # deplacement du point 2

print('ecart max : ', ecartmax)
print('point : ', point)

# tracage des courbes interpoles
for i in range(len(x)):
    plt.plot(xe[i], ye[i], marker='+')

# mise en forme du graphique
plt.xlim([0.2, 0.9])
plt.ylim([0.0, 0.4])
# affichage du graphique
plt.show()
