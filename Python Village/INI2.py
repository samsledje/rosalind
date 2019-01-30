# INI2 - http://rosalind.info/problems/ini2/

f = open('datasets/rosalind_ini2.txt')

a, b = map(int, f.readline().strip().split())
print(a ** 2 + b ** 2)

f.close()