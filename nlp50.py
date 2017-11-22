import re
fname="nlp.txt"
def nlp50():
	with open(fname,"r",encoding="utf-8") as f:
		pattern=re.compile(r"(^.*?[\.|\;|\:|\?|\!])\s([A-Z].*)",re.MULTILINE+re.DOTALL)
		for line in f:
			line=line.strip()
			while len(line)>0:
				match=pattern.match(line)
				if match:
					yield match.group(1)
					line=match.group(2)
				else:
					yield line
					line=""

if __name__=="__main__":
	for i in nlp50():
		print(i)
