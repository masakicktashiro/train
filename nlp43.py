import nlp41true
import re
fname_parsed="neko.txt.cabocha"
def src_dst_func():
	chunks_by_bun=nlp41true.neko_lines()
	src_dst=[]
	for chunks in chunks_by_bun:
		for i,chunk in enumerate(chunks):
			meishi_flag=None
			meishi_doushi_flag=None
			for word in chunk.morphs:
				if word.pos=="名詞":
					meishi_flag=1
				else:
					continue
			if meishi_flag is not None:
				for from_meishi in chunks[chunk.dst].morphs:
					if from_meishi.pos=="動詞":
						meishi_doushi_flag=1
			if meishi_doushi_flag is not None:
				src_dst.append([("".join([i.surface if i.pos!="記号" else "" \
				for i in chunk.morphs]),"".join([i.surface \
				if i.pos!="記号" else "" for i in chunks[chunk.dst].morphs]))])
	
	return src_dst


if __name__=="__main__":
	src_dst=src_dst_func()
	for i in src_dst:
		print(i[0][0],"->",i[0][1])
