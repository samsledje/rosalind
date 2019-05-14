import numpy as np

def PWM(infile, l):
    seqs = []
    motifs = []
    n_lines = 0
    pwm = np.zeros((4,l))

    nucleotides={
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3
    }

    with open(infile, 'r') as f:
        for line in f:
            n_lines += 1
            seqs.append(line.strip())

    for seq in seqs:
        new_motif = [c for c in seq if c.isupper()]
        assert(len(new_motif) == l)
        motifs.append(''.join(new_motif))

    assert(len(motifs) == n_lines)

    for pos in range(l):
        for mot in motifs:
            pwm[nucleotides[mot[pos]], pos] += 1

    return(pwm / pwm.sum(axis=0))

def consensus(PWM):
    maps = {
        0: 'A',
        1: 'C',
        2: 'G',
        3: 'T'
    }

    seq = [maps[np.argmax(PWM[:,i])] for i in range(PWM.shape[1])]
    return(''.join(seq))
    

if __name__ == "__main__":
    print(PWM('input.txt', 8))
    print(consensus(PWM('input.txt', 8)))