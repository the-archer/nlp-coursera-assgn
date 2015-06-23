
def mapping_infrequent_words(trainfile):
	counts = dict()
	with open(trainfile) as f1:
		for line in f1:
			sp = line.split()
			if len(sp) > 1:
				try:
					counts[sp[0]] += 1
				except:
					counts[sp[0]] = 1

	f2 = open("gene2.train", "w")
	with open(trainfile) as f1:
		for line in f1:
			sp = line.split()
			if len(sp) > 1:
				if counts[sp[0]]<5:
					sp[0] = "_RARE_"
				f2.write(sp[0])
				for i in range(1, len(sp)):
					f2.write(" " + sp[i])
				f2.write("\n")
			else:
				f2.write(line)

