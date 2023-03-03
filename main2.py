import codecs
import re
path = "C:/Users/bilge.adam/Downloads/tr.txt/small.txt"
f = codecs.open(path, encoding='utf-8')

cooc = {}
freq = {}


for line in f:
	line = line.strip()
	line = re.sub(r"[^a-zA-ZİŞÜĞÇÖüğçöışâ]", " ", line)
	line = line.split( " " )
	for i in range(len(line) - 1):
		if line[i] not in freq:
			freq[ line[i] ] = 0

		freq[ line[i] ] += 1
		k = line[i] + "-" + line[i+1]
		if k not in cooc:
			cooc[k] = 0
		cooc[k] += 1



for k in cooc:
	parts = k.split("-")
	if k in cooc and parts[0] in freq and parts[1] in freq:
		anb = cooc[k]
		aub = freq[parts[0]] + freq[parts[1]]
		jaccard = anb / aub
		if jaccard > 0.10 and freq[parts[0]] > 100:
			print(k, jaccard)
