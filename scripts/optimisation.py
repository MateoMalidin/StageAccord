import matplotlib.pyplot as plt
import math


# lecture du corpus
# parametres :
# - corpus : le tableau des chemins vers les corpus
# - T : un tableau vide
# action :
# - remplit le tableau T avec les donnees de l'annotation d'un fichier tabulaire
# - apres remplissage, les lignes du tableau T representent les annotations pour chaques annotateur et les colonnes representent les annotation pour chaque item

def lecture(corpus, T):
    file = open(corpus, "r") # fichier tabulaire contenant l'annotation
    lines = file.readlines() # tableau contenant les lignes du fichier file
    for line in lines: # parcours des lignes du fichier file
        tab = line.split('\t') # tableau contenant les elements de la ligne courante
        i = [] # tableau des elements de la ligne courante nettoyes
        for t in tab:
            if t != '\n':
                i.append(int(t))
        T.append(i)


# remplit le tableau des classes utilisees dans l'annotation
# parametres :
# - T : tableau contenant l'annotation
# - C : un tableau vide
# action :
# - remplit le tableau C avec l'ensemble des classes rencontrees dans l'annotation
# - une fois remplit, le tableau C contient l'ensemble (non redondant) des classes apparaissant dans l'annotation

def Cl(T, c):
    for i in T: # parcours des lignes
        for j in i: # parcours des colonnes
            if j not in c: # si la classe attribue a l'item j par l'annotateur i n'est pas encore dans c
                c.append(j)
    c.sort()


# transpose la matrice des annotations
# parametre :
# - T : le tableau d'annotation (lignes = items, colonnes = annotateurs)
# sortie :
# - t : le tableau d'annotation (lignes = annotateurs, colonnes = items)

def transpose(T):
    t = [[0 for i in range(len(T))] for j in range(len(T[1]))] # le tableau qui contiendra la transpose de l'annotation
    for i in range(len(T)):
        for j in range(len(T[i])):
            t[j][i] = T[i][j] # transposition
    return t


##### Accord inter-annotateur #####
##### Davies et Fleiss, 1982 #####


# Xijc
# parametres :
# - T : la matrice d'annotation
# - I : le nombre d'items
# - J : le nombre d'annotateurs
# - item : l'indice de l'item
# - annot : l'indice de l'annotateur
# - c : la classe d'annotation
# sortie :
# - 1 si le j-eme annotateur a attribue la classe c au i-eme item
# - 0 sinon

def Xijc(T, I, J, item, annot, c):
    for j in range(J): # parcours des annotateurs
        for i in range(I): # parcours des items
            if j == annot and i == item:
                if T[j][i] == c:
                    return 1
                else:
                    return 0


# Yic
# parametres :
# - T : la matrice d'annotation
# - I : le nombre d'items
# - J : le nombre d'annotateurs
# - i : l'indice de l'item
# - c : la classe d'annotation
# sortie :
# - le nombre d'annotateurs ayant attribue la classe c au i-eme item

def Yic(T, I, J, item, c):
    sum = 0.0
    for j in range(J): # parcours des annotateurs
        sum += Xijc(T, I, J, item, j, c)
    return sum


# Po
# parametres :
# - T : la matrice d'annotation
# - I : le nombre d'items
# - J : le nombre d'annotateurs
# - C : l'ensemble des classes
# sortie :
# - l'accord inter-annotateur brut

def Po(T, I, J, C):
    sum = 0.0
    for i in range(I): # parcours des items
        for c in C: # parcours des classes
            yic = Yic(T, I, J, i, c)
            sum += yic * (yic - 1)
    return (1.0/(I*J * (J - 1))) * sum


# Pjc
# parametres :
# - T : la matrice d'annotation
# - I : le nombre d'items
# - J : le nombre d'annotateurs
# - j : l'indice de l'annotateur
# - c : la classe d'annotation
# sortie :
# - la proportion d'items associes a la classe c par le j-eme annotateur

def Pjc(T, I, J, j, c):
    sum = 0.0
    for i in range(I): # parcours des items
        sum += Xijc(T, I, J, i, j, c)
    return (1.0/I) * sum

# Pe
# parametres :
# - T : la matrice d'annotation
# - I : le nombre d'items
# - J : le nombre d'annotateurs
# - C : l'ensemble des classes
# sortie :
# - l'accord par chance (Davies et Fleiss, 1982)

def Pe(T, I, J, C):
    sum = 0.0
    # parcours des paires d'annotateurs
    for j1 in range(J - 1): # annotateur 1
        for j2 in range(j1 + 1, J): # annotateur 2
            for c in C: # parcours des classes
                sum += Pjc(T, I, J, j1, c) * Pjc(T, I, J, j2, c)
    return (2.0/(J*(J - 1))) * sum


# kappa de Fleiss
# parametres :
# - T : la matrice d'annotation
# - C : l'ensemble des classes
# sortie :
# - le kappa de Fleiss

def kappa(T, C):
    I = len(T[0]) # nombre d'items
    J = len(T) # nombre d'annotateurs
    po = Po(T, I, J, C) # accord brut
    pe = Pe(T, I, J, C) # accord par chance
    return (po - pe)/(1.0 - pe)


##### Variation de la reference #####
##### Bregeon et al., 2019 #####


# definition de la reference
# parametres :
# - T : la matrice d'annotation
# - C : l'ensemble des classes
# - R : un tableau vide
# action :
# - remplit le tableau R avec la reference obtenue par vote majoritaire

def Ref(T, C, R):
    I = len(T[0]) # nombre d'items
    J = len(T) # nombre d'annotateurs
    for i in range(I): # parcours des items
        max = 0 # nombre maximal de categorisation du i-eme item dans une meme classe
        cmaj = 0 # classe majoritaire pour le i-eme item
        for c in C: # parcours des classes
            cpt = 0 # nombre de categorisation du i-eme item dans la classe c
            for j in range(J): # parcours des annotateurs
                if T[j][i] == c:
                    cpt += 1
            if cpt > max:
                max = cpt
                cmaj = c
        R.append(cmaj) # reference pour le i-eme item


# simulation des groupes de 5 annotateurs
# parametres :
# - T : la matrice d'annotation
# - C : l'ensemble des classes
# - Ri : un tableau vide
# action :
# - définit l'ensembles des references des groupes simules

def Refi(T, C, Ri):
    I = len(T[0]) # nombre d'items
    J = len(T) # nombre d'annotateurs
    # pour toutes les combinaisons de 5 annotateurs
    for j1 in range(J-4): # annotateur 1
        for j2 in range(j1 + 1, J-3): # annotateur 2
            for j3 in range(j2 + 1, J-2): # annotateur 3
                for j4 in range(j3 + 1, J-1): # annotateur 4
                    for j5 in range(j4 + 1, J): # annotateur 5
                        annot = [] # annotation du groupe
                        for i in range(I): # parcours des items
                            annotitem = [T[j1][i], T[j2][i], T[j3][i], T[j4][i], T[j5][i]] # annotation du groupe courant pour le i-eme item
                            annot.append(annotitem) # ajout a l'annotation du groupe
                        Tannot = transpose(annot) # tansposee de l'annotation
                        ri = [] # annotation de reference produite par le groupe courant
                        Ref(Tannot, C, ri) # definition de la reference du groupe
                        Ri.append(ri)


# taux de variation de la reference
# parametres :
# - Ri : l'ensembles des references produitent par les groupes simules
# sortie :
# - le taux de variation moyen de la reference

def taux(Ri):
    nbG = len(Ri) # nombre de groupes
    nbP = math.factorial(nbG) / (math.factorial(2) * math.factorial(nbG - 2))
    sum = 0.0
    # pour toutes les paires de references
    for r1 in range(nbG - 1): # reference 1
        for r2 in range(r1 + 1, nbG): # reference 2
            for i in range(len(Ri[r1])): # parcours des items
                if Ri[r1][i] != Ri[r2][i]:
                    sum += 1.0
    return sum / nbP


##### programme principal #####


# tableau contenant les chemins vers les fichiers
corpus = ["annotation_typage_coreference.txt", "annotation_opinion.txt", "annotation_emotion.txt", "annotation_registre.txt"]

for f in corpus: # parcours des fichiers
    T = [] # matrice d'annotation
    c = [] # ensemble des classes
    R = [] # annotation de reference
    Ri = [] # ensemble des references des groupes simules
    lecture(f, T) # lecture du corpus
    if len(T) > len(T[0]): # si la matrice d'annotation n'est pas dans le bon format
        t = transpose(T) # transposition de la matrice d'annotation
        Cl(t, c) # generation de l'ensemble des classes
        k = kappa(t, c) # calcul du kappa de Fleiss sur le fichier courant
        Refi(t, c, Ri) # definition de l'ensemble des references des groupes simules
    else: # si la matrice d'annotation est dans le bon format
        Cl(T, c) # generation de l'ensemble des classes
        k = kappa(T, c) # calcul du kappa de Fleiss sur le fichier courant
        Refi(T, c, Ri) # definition de l'ensemble des references des groupes simules
    print(f, ' :')
    print(' k = ', round(k, 2))
    v = taux(Ri)
    print(' taux = ', round(v, 2))
