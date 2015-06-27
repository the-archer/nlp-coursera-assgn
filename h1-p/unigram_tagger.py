import emission



def unigram_tagger(countsfile, inputfile, outputfile):
	trained_words = set()

	with open(countsfile) as f1:
		for line in f1:
			line = line.rstrip('\n')
			sp = line.split()
			if len(sp)>3:
				trained_words.add(sp[3])
				
	

	f2 = open(outputfile, "w")
	with open(inputfile) as f1:
		for line in f1:
			line = line.rstrip('\n')
			if line!="":
				tags = ["O", "I-GENE"]
				best = -1
				assigned_tag = ""
				for y in tags:
					em = 0
					if line in trained_words:
						em = emission.compute_emission(line, y, countsfile)
					else:
						em = emission.compute_emission("_RARE_", y, countsfile)
					#print line
					#print y
					#print em
					#a = raw_input()
					if em > best:
						
						best = em
						assigned_tag = y

				f2.write(line+" "+assigned_tag+"\n")
			else:
				f2.write("\n")
	return 		