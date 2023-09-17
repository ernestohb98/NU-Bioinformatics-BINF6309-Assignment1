#!/usr/bin/env python
#sliding_window.py
import sys
def sliding_window(k,seq):
    seq = seq.upper()
    kmers = []
    for i in range(len(seq)-k+1):
        kmer = seq[i:i+k]
        kmers.append(kmer)
    return kmers
def gc_content(kmers):
    content = []
    for kmer in kmers:
        gc = 0
        for i in range(len(kmer)):
            if kmer[i] == "C" or kmer[i] == "G":
                gc += 1
        content.append(round(gc/len(kmer),2))
    return content

if __name__ == "__main__":
    arg_count = len(sys.argv) - 1
    if arg_count < 2:
        raise Exception("This script requires 2 arguments: a kmer size and then a sequence")

    k = int(sys.argv[1])
    seq = sys.argv[2]

    kmers = sliding_window(k, seq)
    gc = gc_content(kmers)
    for i in range(len(kmers)):
        print(f"{kmers[i]}\t{gc[i]}")