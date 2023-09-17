#!/usr/bin/env python
#sliding_window_fasta.py
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
    fasta = sys.argv[2]
    seq = ""
    with open(fasta) as file:
        for line in file:
            if line.startswith(">"):
                name = line
        seq = seq + line.rstrip()
    kmers = sliding_window(k, seq)
    gc = gc_content(kmers)
    print(name.rstrip())
    for i in range(len(kmers)):
        print(f"{kmers[i]}\t{gc[i]}")