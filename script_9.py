from Bio import Align, SeqIO
from Bio.Seq import Seq
from Bio.SeqUtils import MeltingTemp


def check_Tm(primer):
    return MeltingTemp.Tm_NN(Seq(primer))


def check_homodimer(primer):

    return MeltingTemp.Tm_Wallace(primer,primer)


def check_hairpin(primer):
    return MeltingTemp.Tm_GC(primer)


with open("primers.txt", 'r') as file:
    primers = [line.strip() for line in file]

print(f"{'Primer':<25}{'Tm':<10}{'Homodimer':<15}{'Hairpin':<10}")

for primer in primers:
    print(f""
          f"{primer:<25} "
          f"{check_Tm(primer):<10.2f}"
          f"{'Yes' if check_homodimer(primer) > check_Tm(primer) else 'No':<15}"
          f"{'Yes' if check_hairpin(primer) > check_Tm(primer) else 'No':<10}")