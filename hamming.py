#!/usr/bin/env python
#sliding_window_fasta.py
import sys
def hamming(x,y):
    dist = 0
    for i in range(len(x)-1):
        if x[i] == y[i]:
            dist += 1
    return dist

if __name__ == "__main__":
    try:
        seq1 = sys.argv[1]
        seq2 = sys.argv[2]
        dist = hamming(seq1, seq2)
        print(f"{seq1}\t{seq2}\tDistance:{dist}")
    except IndexError:
        print('Both sequences need to be the same length')