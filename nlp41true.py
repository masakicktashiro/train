import re
import nlp40
fname_parsed="neko.txt.cabocha"

class Chunk:
	def __init__(self,morphs,dst,srcs):
		self.morphs=[]
		self.dst=[]
		self.srcs=[]
	
	def __str__(self):
		surface=""
		for morph in self.morphs:
			surface+=morph.surface
		return "{}\tsrcs{}\tdst{}".format(surface,self.srcs,self.dst)

def neko_lines():
	with open(fname_parsed,"r",encoding="utf-8") as f:
		chunks=[]
		idx=-1
		dsts=[]
		srcs=[]
		morphs=[]
		word=""
		words=[]
		pattern=re.compile(r"([0-9]+?)D")
		for line in f:
			if line.startswith("EOS"):
				if len(dsts)>0:
					words.append(word)
					for i in range(len(dsts)):
						srcs.append([])
					for i,p in enumerate(dsts):
						if int(p)>-1:
							srcs[int(p)].append(i)
					chunks.append([words,morphs,srcs,dsts])
					yield chunks
					chunks=[]
					dsts=[]
					srcs=[]
					word=""
					words=[]
					morphs=[]
				else:
					yield []
			elif line.startswith("*"):
				dsts.append(pattern.sub(r"\1",line.split(" ")[2]))
				idx=int(line.split(" ")[1])
				if word!="":
					words.append(word)
					word=""
			else:
				information=line.split("\t")[1].split(",")
				word+=line.split("\t")[0]
				if len(morphs)<idx+1:
					morphs.append([nlp40.Morph(line.split("\t")[0],\
					information[6],information[0],information[1])])
				else:
					morphs[idx].append(nlp40.Morph(line.split("\t")[0],\
					information[6],information[0],information[1]))
		raise StopIteration

if __name__=="__main__":
	for i,p in enumerate(neko_lines(),1):
		if i==8:
			print(p)
			for t1,t2,t3,t4 in zip(p[0][0],p[0][1],p[0][2],p[0][3]):
				print(t1,t3,t4)
				print([i.pos for i in t2])
			break
