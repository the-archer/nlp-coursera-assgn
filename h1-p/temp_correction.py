f1 = open("gene.dev", "r")

f2 = open("gene_dev.p2.out", "r")

f3 = open("gene_dev.p3.out", "w")

lines = f1.readlines()

i=0
for line in f2:
	if line!="\n":
		f3.write(lines[i].rstrip("\n")+" "+(line.split())[1]+"\n")
	else:
		f3.write("\n")
	i+=1

f1.close()
f2.close()
f3.close()