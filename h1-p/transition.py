

def compute_transition(y3, y1, y2, countsfile):
	num = 0
	den = 0
	with open(countsfile) as f1:
		for line in f1:
			line = line.rstrip('\n')
			sp = line.split()
			if len(sp) > 4 and sp[1]=="3-GRAM" and sp[2]==y1 and sp[3]==y2 and sp[4]==y3:
				num = int(sp[0])

			if len(sp) > 3 and sp[1]=="2-GRAM" and sp[2]==y1 and sp[3]==y2:
				den = int(sp[0])
	if den!=0:
		return ((float(num))/den)
	else:
		print "Error"
		return 0


