# IPRB - http://rosalind.info/problems/iprb/

# f = open('datasets/rosalind_iprb.txt')
# k,m,n = f.read().split()
# k = int(k)
# m = int(m)
# n = int(n)
k = 2
m = 2
n = 2

p = k + m + n

AA = k/p
Aa = m/p
aa = n/p

AA_AA = AA * (k-1) / (p-1)
AA_Aa = AA * (m-1) / (p-1)
AA_aa = AA * (n-1) / (p-1)
Aa_Aa = Aa * (m-1) / (p-1)
Aa_aa = Aa * (n-1) / (p-1)

total = AA_AA + 2*AA_Aa + 2*AA_aa + 0.75*Aa_Aa + 2*0.5*Aa_aa
print(total)
