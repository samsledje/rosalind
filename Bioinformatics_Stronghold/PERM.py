# PERM - http://rosalind.info/problems/perm/
import math, sys

f = open('datasets/rosalind_perm.txt')
i = int(f.readline().strip())

out = open('perm_results.txt', 'w+')
out.write(str(math.factorial(i)))
out.write('\n')
numbers = [j+1 for j in range(i)]

def permute(n, l, nums):
    if n == 0:
        out.write(' '.join(l))
        out.write('\n')
        return
    for j in nums:
        new_l = list(l)
        new_nums = list(nums)
        new_nums.remove(j)
        new_l.append(str(j))
        permute(n-1, new_l, new_nums)

permute(i, [], numbers)
out.close()

f.close()

    