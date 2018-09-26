# FIB - http://rosalind.info/problems/fib/

f = open('datasets/rosalind_fib.txt')
n, k = f.read().split()
n = int(n)
k = int(k)

assert n <= 40, 'n > 40'
assert k <= 5, 'k > 5'

dp_array = [0]*n
dp_array[0] = 1
dp_array[1] = 1

for i in range(2, n):
    dp_array[i] = dp_array[i-1] + k*dp_array[i-2]

print(dp_array[n-1])
