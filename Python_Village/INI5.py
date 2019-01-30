# INI5 - http://rosalind.info/problems/ini5/

f = open('datasets/rosalind_ini5.txt')
#f = open('datasets/test.txt')

lines = f.readlines()
for i in range(0, len(lines)):
    if (i+1) % 2 == 0:
        print(lines[i].strip())

f.close()