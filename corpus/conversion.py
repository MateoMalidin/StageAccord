input = open('annotation_registre.txt', 'r')
output = open('annotation_registre2.txt', 'w')

lines = input.readlines()
input.seek(0)

for line in lines:
    tab = line.split('\t')
    if tab[0] != '\n':
        output.write(str(int(tab[0])))
        output.write('\t')

output.write('\n')

for line in lines:
    tab = line.split('\t')
    if tab[0] != '\n':
        output.write(str(int(tab[1])))
        output.write('\t')

output.write('\n')

for line in lines:
    tab = line.split('\t')
    if tab[0] != '\n':
        output.write(str(int(tab[2])))
        output.write('\t')

input.close()
output.close()
