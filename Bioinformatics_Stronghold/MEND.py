# MEND - http://rosalind.info/problems/mend/
from ete3 import Tree
import numpy as np

tree = Tree('datasets/rosalind_mend.txt')
#tree = Tree('datasets/test.txt')

def gmap(node):
    g_map = ['AA','Aa','aa']
    return g_map.index(node.name)


n = 0
for node in tree.traverse("postorder"):
    n+=1

node_pr = {}

s = set()

for node in tree.traverse("postorder"):
    #print(node)
    if node.is_leaf():
        index = gmap(node)
       # print(node.name, index)
        node_pr[node] = [0]*index + [1] + [0]*(2-index)
    else:
        parent1,parent2 = node.children
        p1 = node_pr[parent1]
        p2 = node_pr[parent2]
        #print(p1,p2)
        node_probas = [0,0,0]
        node_probas[0] = (p1[1]*p2[1]*0.25 + p1[0]*p2[1]*0.5 + p1[1]*p2[0]*0.5 + p1[0]*p2[0])
        node_probas[1] = (p1[0]*p2[1]*0.5 + p1[0]*p2[2] + p1[1]*p2[0]*0.5 + p1[1]*p2[1]*0.5 + p1[1]*p2[2]*0.5 + p1[2]*p2[0] + p1[2]*p2[1]*0.5)
        node_probas[2] = (p1[1]*p2[1]*0.25 + p1[1]*p2[2]*0.5 + p1[2]*p2[1]*0.5 + p1[2]*p2[2])
        node_pr[node] = node_probas
    #print(node_pr[node])
    #print(sum(node_pr[node]))
    #print('-'*50)
print(' '.join([str(i) for i in node_pr[tree]]))