from Bio import Align

alignment = Align.parse("my_alignment.txt","sam")

al = Align.Alignment(alignment)

print(al)