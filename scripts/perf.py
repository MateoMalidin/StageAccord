import numpy as np
import matplotlib.pyplot as plt

pas = 0.01

coref = open('kappaTV_coref.csv', 'r')
similarite = open('kappaTV_similarite.csv', 'r')
opinion = open('kappaTV_opinion.csv', 'r')
emotion = open('kappaTV_emotion.csv', 'r')
newsletter = open('kappaTV_newsletter.csv', 'r')

tc = coref.readlines()
ts = similarite.readlines()
to = opinion.readlines()
te = emotion.readlines()
tn = newsletter.readlines()

t = [tc, ts, to, te, tn]

coref.seek(0)
similarite.seek(0)
opinion.seek(0)
emotion.seek(0)
newsletter.seek(0)

l = len(tc) - 1

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

x = [cx, sx, ox, ex, nx]
y = [cy, sy, oy, ey, ny]

xe = [cxe, sxe, oxe, exe, nxe]
ye = [cye, sye, oye, eye, nye]

for i in range(len(t)):
    c = t[i]
    a = x[i]
    ae = xe[i]
    o = y[i]
    oe = ye[i]
    for j in range(1, len(tc)):
        v = c[j]
        tab = v.split(',')
        a[j-1] = round(float(tab[0]), 2)
        o[j-1] = round(float(tab[1]), 2)
    ae.append(a[0])
    oe.append(o[0])
    for k in range(len(a)-1):
        x1 = a[k]
        y1 = o[k]
        x2 = a[k+1]
        y2 = o[k+1]
        m = (y2 - y1) / (x2 - x1)
        p = y2 - m*x2
        it = x1 - pas
        while it > x2:
            ae.append(round(it, 2))
            oe.append(round(m*it + p, 2))
            it -= pas
        ae.append(x2)
        oe.append(y2)

ppc = 1
dgc = 0
for i in range(len(xe)):
    if xe[i][0] < ppc:
        ppc = xe[i][0]
    if xe[i][-1] > dgc:
        dgc = xe[i][-1]

print('ppc : ', ppc)
print('dgc : ', dgc)
print('nbIt : ', int((ppc-dgc)/pas))
print('lenxe : ', len(xe))

ecartmax = 0
point = 0
for i in range(len(xe)):
    for j in range(len(xe)):
        if i != j:
            x1 = 0
            x2 = 0
            print('ijk0 : ', i, ':', j, ':', x1)
            while xe[i][x1] > ppc:
                x1 += 1
                print('xei : ', xe[i][x1])
            while xe[j][x2] > ppc:
                x2 += 1
                print('xej : ', xe[j][x2])
            ecart = 0
            itmax1 = x1+int((ppc-dgc)/pas)
            itmax2 = x2+int((ppc-dgc)/pas)
            while x1 <= itmax1 and x2 <= itmax2:
                ecart = abs(ye[i][x1] - ye[j][x2])
                print('yei:yej : ', ye[i][x1], ':', ye[j][x2])
                print('ecart : ', ecart)
                if ecart > ecartmax:
                    ecartmax = ecart
                    point = x1
                x1 += 1
                x2 += 1

print('ecart max : ', ecartmax)
print('point : ', point)

for i in range(len(x)):
    plt.plot(xe[i], ye[i], marker='+')

plt.xlim([0.2, 0.9])
plt.ylim([0.0, 0.4])
plt.show()








