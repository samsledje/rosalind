# RNA - http://rosalind.info/problems/prot/

f = open('datasets/rosalind_prot.txt')
s = f.readline().strip()

codon_table = { "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
                "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
                "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
                "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
                "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
                "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
                "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
                "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
                "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
                "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
                "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
                "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
                "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
                "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
                "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
                "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
}

assert len(s) % 3 == 0, "Sequence length must be a multiple of 3"
n = len(s)
l = []

for i in range(0,n,3):
    codon = s[i:i+3]
    amino_acid = codon_table[codon]
    if amino_acid == "Stop":
        break
    else:
        l.append(amino_acid)

print(''.join(l))
