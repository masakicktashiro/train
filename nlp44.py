import re
import CaboCha
import pydot_ng as pydot
import nlp40
import nlp41true
fname_parsed="neko.txt.cabocha"
def mk_sentence():
	txt=input("文字列を入力してください")
	with open(txt+".txt","w",encoding="utf-8") as f:
		f.write(txt)
	return txt

def mk_parsed(fname,fname_parsed):
	with open(fname,"r",encoding="utf-8") as data_file,\
	open(fname_parsed,"w",encoding="utf-8") as out_file:
		cabocha=CaboCha.Parser()
		for line in data_file:
			out_file.write(cabocha.parse(line).toString(CaboCha.FORMAT_LATTICE))

def mk_chunks(fname_parsed):
	with open(fname_parsed,"r",encoding="utf-8") as f:
		chunks=dict()
		idx=0
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
					chunks[idx]=nlp41true.Chunk()
				else:
					yield []
			elif line.startswith("*"):
				idx=int(line.split(" ")[1])
				chunks[idx]=nlp41true.Chunk()
				chunks[idx].dst=int(pattern.sub(r"\1",line.split(" ")[2]))
			else:
				information=line.split("\t")[1].split(",")
				chunks[idx].morphs.append\
				(nlp40.Morph(line.split("\t")[0],information[6],\
				information[0],information[1]))
		raise StopIteration
	
def graph_from_edges_ex(edge_list,directed=False):
	if directed:
		graph=pydot.Dot(graph_type="digraph")
	else:
		graph=pydot.Dot(graph_type="graph")

	for edge in edge_list:
		id1=str(edge[0][0])
		label1=str(edge[0][1])
		id2=str(edge[1][0])
		label2=str(edge[1][1])
		
		graph.add_node(pydot.Node(id1,label=label1))
		graph.add_node(pydot.Node(id2,label=label2))

		graph.add_edge(pydot.Edge(id1,id2))
	
	return graph

if __name__=="__main__":
	txt=mk_sentence()
	mk_parsed(txt+".txt",txt+".txt.cabocha")
	chunks_by_sent=mk_chunks(txt+".txt.cabocha")
	for i,chunks in enumerate(chunks_by_sent):
		edge_list=[]
		src_ls=[]
		for chunk in chunks:
			src=""
			for morph in chunk.morphs:
				if morph.pos!="記号":
					src+=morph.surface
			src_ls.append(src)
		for p,chunk in enumerate(chunks):
			if chunk.dst!=-1:
				edge_list.append([[p,src_ls[p]],[chunk.dst,src_ls[chunk.dst]]])
		if len(edge_list)>0:
			graph=graph_from_edges_ex(edge_list,directed=True)
			graph.write_png("result.png")
