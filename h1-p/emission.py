

def compute_emission(x, y, countsfile):
	num = 0
	den = 0
	

	with open(countsfile) as f1:
		for line in f1:
			line = line.rstrip('\n')
			sp = line.split()
			if len(sp)>3 and sp[1]=="WORDTAG" and sp[2]==y and sp[3]==x:
				num = int(sp[0])
			if len(sp)>2 and sp[1]=="1-GRAM" and sp[2]==y:
				den = int(sp[0])
	if den!=0:
		return ((float(num))/den)
	else:
		print "Error"
		return 0