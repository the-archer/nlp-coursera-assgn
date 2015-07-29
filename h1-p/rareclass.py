def mapping_infrequent_words_to_classes(trainfile):
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
	#print counts
	with open(trainfile) as f1:
		for line in f1:
			sp = line.split()
			if len(sp) > 1:
				if counts[sp[0]]<5:
					print sp[0]
					if any(char.isdigit() for char in sp[0]):
						print sp[0]
						sp[0] = "_NUMERIC_"
					elif sp[0].isupper():
						sp[0] = "_ALLCAPITALS_"
					elif sp[0][-1].isupper():
						sp[0] = "_LASTCAPITAL_"
					else:
						sp[0] = "_RARE_"

				f2.write(sp[0])
				for i in range(1, len(sp)):
					f2.write(" " + sp[i])
				f2.write("\n")
			else:
				f2.write(line)