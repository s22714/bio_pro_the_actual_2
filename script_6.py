from Bio import Align

seq_a = "AACCTTGGAA"
seq_b = "AAACCCTGG"

aligner = Align.PairwiseAligner()

alignments = aligner.align(seq_a,seq_b)

for a in alignments:
    if a.counts().mismatches > 0:
        print(a)