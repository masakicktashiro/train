import re
import nlp40
fname_parsed="neko.txt.cabocha"

class Chunk:
	def __init__(self):
		self.morphs=[]
		self.dst=-1
		self.srcs=[]
	
	def __str__(self):
		surface=""
		for morph in self.morphs:
			surface+=morph.surface
		return "{}\tsrcs{}\tdst{}".format(surface,self.srcs,self.dst)

def neko_lines():
	with open(fname_parsed,"r",encoding="utf-8") as f:
		chunks=dict()
		idx=-1
		pattern=re.compile(r"([0-9]+?)D")
		for line in f:
			if line.startswith("EOS"):
				if len(chunks)>0:
					for i,p in enumerate(chunks):
						if int(chunks[i].dst)>-1:
							chunks[chunks[i].dst].srcs.append(i)
					sorted_chunks=sorted(chunks.items(),key=lambda x:x[0])
					yield list(zip(*sorted_chunks))[1]
					chunks=dict()
					idx=0
					chunks[idx]=Chunk()
				else:
					yield []
			elif line.startswith("*"):
				idx=int(line.split(" ")[1])
				chunks[idx]=Chunk()
				chunks[idx].dst=int(pattern.sub(r"\1",line.split(" ")[2]))
			else:
				information=line.split("\t")[1].split(",")
				chunks[idx].morphs.append\
				(nlp40.Morph(line.split("\t")[0],information[6],\
				information[0],information[1]))
		raise StopIteration

if __name__=="__main__":
	for i,p in enumerate(neko_lines(),1):
		if i==8:
			for t1,t2 in enumerate(p):
				print("[{}]{}".format(t1,t2))
			break
