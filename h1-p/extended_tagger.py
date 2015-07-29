import sys
from emission import compute_emission
from transition import compute_transition

def trigram_tagger(sentence, countsfile):
	n = len(sentence)
	dp = AutoVivification()
	bp = AutoVivification()
	dp["0"]["*"]["*"] = 1
	tags = dict()
	tags[False]=["*"]
	tags[True] = ["O", "I-GENE"]
	
	for k in range(1, n+1):
		for u in tags[(k-1)>0]:
			for v in tags[(k>0)]:
				best = -1
				arg = ""
				for w in tags[(k-2)>0]:
					current = dp[str(k-1)][w][u]*compute_transition(v, w, u, countsfile)*compute_emission(sentence[k-1], v, countsfile)
					if current > best:
						best = current
						arg = w
				dp[str(k)][u][v] = best
				bp[str(k)][u][v] = arg
				
	best = -1
	arg1 = ""
	arg2 = ""
	for u in tags[True]:
		for v in tags[True]:
			current = dp[str(n)][u][v]*compute_transition("STOP", u, v, countsfile)
			if current > best:
				best = current
				arg1 = u
				arg2 = v
	tag_seq = [""] * n
	tag_seq[n-2] = arg1
	tag_seq[n-1] = arg2
	for k in xrange(n-2, 0, -1):
		tag_seq[k-1] = bp[str(k+2)][tag_seq[k]][tag_seq[k+1]]

	return tag_seq






class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value




if __name__ == "__main__":
	countsfile = sys.argv[3]
	trained_words = set()

	with open(countsfile) as f1:
		for line in f1:
			line = line.rstrip('\n')
			sp = line.split()
			if len(sp)>3:
				trained_words.add(sp[3])


	f1 = open(sys.argv[1], "r")
	f2 = open(sys.argv[2], "w")
	
	sentence = []
	actual = []
	for line in f1:
		line = line.rstrip('\n')
		if line=="":
			tag_seq = trigram_tagger(sentence, countsfile)
			for k in range(0, len(actual)):
				f2.write(actual[k] + " " + tag_seq[k] + "\n")
			f2.write("\n")
			del sentence[:]
			del actual[:]
		else:
			if line in trained_words:
				sentence.append(line)
			else:
				if any(char.isdigit() for char in line):
					sentence.append("_NUMERIC_")
				elif line.isupper():
					sentence.append("_ALLCAPITALS_")
				elif line[-1].isupper():
					sentence.append("_LASTCAPITAL_")
				else:
					sentence.append("_RARE_")
			actual.append(line)
	f1.close()
	f2.close()

