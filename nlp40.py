import CaboCha
import os
fname="neko.txt"
fname_parsed="neko.txt.cabocha"

def parse_cabocha():
	with open(fname,"r",encoding="utf-8") as f,open(fname_parsed,"w",encoding="utf-8") as i:
		cabocha=CaboCha.Parser()
		for line in f:
			i.write(cabocha.parse(line).toString(CaboCha.FORMAT_LATTICE))

class Morph:
	def __init__(self,surface,base,pos,pos1):
		self.surface=surface
		self.base=base
		self.pos=pos
		self.pos1=pos1

	def __str__(self):
		return "surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]".format(self.surface,self.base,self.pos,self.pos1)

def return_morph():
	with open(fname_parsed,"r",encoding="utf-8") as f:
		morph_ls=[]
		for i in f:
			if i=="EOS\n":
				yield morph_ls
				morph_ls=[]
			else:
				if i[0]=="*":
					continue
				splited=i.split("\t")
				information=splited[1].split(",")
				morph_ls.append(Morph(surface=splited[0],base=information[6],pos=information[0],pos1=information[1]))
		raise StopIteration
if __name__=="__main__":
	if not os.path.exists(fname_parsed):
		parse_cabocha()
	for i,p in enumerate(return_morph(),1):
		if i==3:
			for morph in p:
				print(morph)
			break	
