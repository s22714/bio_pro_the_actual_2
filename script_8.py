from Bio import Align
import numpy as np

seq_1 = "AAGAAATTCCAAGTCCAGGGATACACAAACAGGTGTACAGCAAATCATGTAGGTGGTACTTTTCCCCTAAGTTATAATTT\
AATCTATACCCTAGGAAAATGCCAAAGTCACAATTGGGTGGATTGGGTGATTTTCCAGTAGAAAGAAAATTCCATCCCAT\
CTTTGTTCTCAAAACGTTTTTTCTTTGCATATAGGTAAGGGTTTACAGATCAATAATCTTCTTGATTTCAGTATGAAATT\
ACTTTCTCTTTGCTTGAGTTACTCTGAGTTATGCAGAAGGCTCCCTGTTCTGAATCCACTAGTATTTCTTTTTTTCTGA\
GAATATTTCAGTGTATGTTGAAAACAAGGAACATTATGGAAACTTTCAGTCCTTAATTGTGTCAAGATATTAATGTTAGT\
GATATACAAATTAGATGGTGATGGGAAACTTGAGCCTGGCTTTATAGGAGGTAATTTTTTTTTCTTCCTTCCTTTTTTTG\
CAGGGGTGGGGGTTATGATACAGGGATACAGGTAAGATAGTCCTATAAACTCATCTGCTGATAGTTCATATGAAGGCTTT\
TGACTAGAAAACTTCCATTAATAGTGCTGAGATATAAACATATGGTAAAACTGCTTTCCATATTAAGATACCTTGCCAC\
CCACTCCTTTTCTTTGAGACAAGGTCTTGCTCTGTTAGCCAGGCTGGAGTGCAGTCATGTGATCTTGATGCACCGCAGCC\
TCCACCTCCCGGACTCAAGCGATCCTTCCGCCTCAGACCTCCAAATAGCTGGGACCACAGGCATGCACAGGGACCATACC\
TGGCTAATTTTTGTATTTTTTGTAGAGACGGGTTTTCACCATGTTGCCCAAGCTGGTTCAAACTCCTGAGCTCAAGCAA\
TCTGCCCACCTTGGTCTCCCAGAATGCTGGGATTACAGGCATGAGCCACCACCACGTCTGGCTTCCCCCTACTTGTTTTT"
seq_2 = "AAGAAATTCACAGTCCAGGGATACACAAACAGGTGTACAAAGCAAATCATGTAGGTGGTACTTTTCCCCTAAGTTATAATTT\
AATCTATACCCTAGGAAAATGCCAAAGTCGGAATTGGGTGATTGGGTGTTTCCAGTAGAAAGAAAATTCCATCCCAT\
CTTTGTTCTCAAAACGTTTTTTCTTTGCATATAGCTAAGGGTTTACAGATCAATAATCTCTTGATTTCAGTATGAAATT\
ACTTTCTCTTTGCTTGAGTTACTCTGAATTATGCAGAAGGCTCCCTGTTCTGAATCCACTTATGTATTTCTTTTTTTCTGA\
GAATATTTCAGTGTATGTTGAAAACAAGGAACATTATGGAAACTTTCAGTTCCTTAATTGTGTCAAATATTAATGTTAGT\
GATATACAAATTAGATGGTGATGGGAAACTTGAGCCTGGCTTTATAGGAGGTAATTTTTTTTTCTTCCTTCCTTTTTTTG\
CAGGGGTGGGGGTTATGATACAGGGATACAGGTAAGAGTCCTATAACTCATCTGCTGATAGTTCATATGAAGGCTTT\
TGACTAGAATAACTTCCATTAATAGTGCTGAAGATATAAACATATGGTAAAACTGCTTTCCATATTAAGATACCTTGCCAC\
CCACTCCTTTTCTTTGAGACAAGCCTTGCTCTGTATATAGCCAGGCTGGAGTGCAGTCATGTGATCTTGATGCACCGCAGCC\
TCCACCTCCCGGACTCAAGCGATCTTCCGCCTCAGACTCCAAATAGCTGGGACCACAGGCATGCACAGGGACCATACC\
TGGCTAATTTTTGTATTTTTTGTAGAGACGGCCCCTCCCATGTTGCCCAAGCTGGTCTCAAACTCCTGAGCTCAAGCAA\
TCTGCCCACCTTGGTCCCCATTTGCTGGGATTACAGCATGAGCGACCACCAGTCTGTTGCCCCCTACTTGTTTTT"

aligner = Align.PairwiseAligner()
alignments = aligner.align(seq_1, seq_2)

n = 3
alignment = alignments[n]

coord_matrix = np.zeros((2, len(alignment.coordinates[0])))

for i, (start, end) in enumerate(zip(*alignment.coordinates)):
    coord_matrix[0, i] = start
    coord_matrix[1, i] = end

with open('alignment_info.txt', 'w') as f:
    f.write(f"AlignmentCounts (gaps={alignment.counts().gaps}, identities={alignment.counts().identities}, mismatches={alignment.counts().mismatches})\n")
    f.write(str(coord_matrix))
    f.write(f"\n\n{str(alignment)}")

print(f"AlignmentCounts (gaps={alignment.counts().gaps}, identities={alignment.counts().identities}, mismatches={alignment.counts().mismatches})")
print(coord_matrix)
print(alignment)