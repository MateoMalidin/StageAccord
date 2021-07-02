import matplotlib.pyplot as plt

# lecture du corpus
def lecture(corpus, T):
    file = open(corpus, "r")
    lines = file.readlines()
    for line in lines:
        tab = line.split('\t')
        i = []
        for t in tab:
            if t != '\n':
                i.append(int(t))
        T.append(i)

# remplit le tableau des classes dans l'annotation
def C(T, c):
    for i in T:
        for j in i:
            if j not in c:
                c.append(j)
    c.sort()

# transpose la matrice des annotations
def transpose(T):
    t = [[0 for i in range(len(T))] for j in range(len(T[1]))]
    for i in range(len(T)):
        for j in range(len(T[i])):
            t[j][i] = T[i][j]
    return t

# nombre de fois où le i-ème item est classé dans la catégorie j
def nij(i, j, T):
    sum = 0.0
    for a in T:
        if a[i] == j:
            sum += 1
    return sum

# proportion des catégorisation dans la classe j
def pj(j, T):
    sum = 0.0
    for i in range(len(T[1])):
        sum += nij(i, j, T)
    return sum / (len(T[1])*len(T))

# accord entre annotateurs pour le i-ème item
def Pi(i, T, c):
    sum = 0.0
    for j in c:
        sum += nij(i, j, T)*(nij(i, j, T) - 1)
    return sum / (len(T)*(len(T) - 1))

# accord brut
def P(T, c):
    sum = 0.0
    for i in range(len(T[1])):
        sum += Pi(i, T, c)
    return sum / len(T[1])

# accord par chance
def Pe(T, c):
    sum = 0.0
    for j in c:
        sum += pj(j, T)**2
    return sum

# kappa de Fleiss
def kappa(T, c):
    p = P(T, c)
    pe = Pe(T, c)
    return (p - pe) / (1 - pe)

##### programme principal #####

corpus = ["annotation_typage_coreference.txt", "annotation_opinion.txt", "annotation_emotion.txt", "annotation_registre.txt"]

for f in corpus:
    T = []
    c = []
    lecture(f, T)
    if len(T) > len(T[1]):
        t = transpose(T)
        C(t, c)
        k = kappa(t, c)
    else:
        C(T, c)
        k = kappa(T, c)
    print(f, ' :')
    print(' k = ', round(k, 2))
    
    






