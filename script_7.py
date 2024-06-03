from Bio import Align

al = Align.parse("my_alignment.txt","sam")


a = next(al)
l = [i[1]-i[0] for i in a.aligned[0]]
print("Maksymalna dlugosc dopasowania: ", max(l))
print("Maksymalna pozycja dopasowania: ", a.aligned[0][l.index(max(l))][0])