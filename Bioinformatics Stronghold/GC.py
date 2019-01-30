# GC - http://rosalind.info/problems/gc/

f = open('datasets/rosalind_gc.txt')

class Seq():
    def __init__(self, label, string):
        self.label = label
        self.string = string
    
    def calc_gc(self):
        n = len(self.string)
        gc = 0
        for i in range(len(self.string)):
            if self.string[i] == 'G' or self.string[i] == 'C':
                gc += 1
        self.gc = float(gc)*100/n

    def __repr__(self):
        return f'<Seq {self.label}>'

seqs = []
partial_string = []

for line in f:
    if line.startswith('>'):
        if len(partial_string) != 0:
            seqs.append(Seq(label, ''.join(partial_string)))
            partial_string = []
        label = line.strip().split('>')[1]
    else:
        partial_string.append(line.strip())
seqs.append(Seq(label, ''.join(partial_string)))

for s in seqs:
    s.calc_gc()

best = max(seqs, key=lambda x: x.gc)
print(best.label)
print(best.gc)
