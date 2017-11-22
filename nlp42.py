import nlp41true
import re
fname_parsed="neko.txt.cabocha"
def nlp42():
    chunks_by_bun=nlp41true.neko_lines()
    for chunks in chunks_by_bun:
        for i,chunk in enumerate(chunks):
            yield "".join([i.surface if i.pos!="記号" else "" 
            for i in chunk.morphs])+"\t"+"".join([i.surface 
            if i.pos!="記号" else "" for i in chunks[chunk.dst].morphs])

if __name__=="__main__":
    for i in nlp42():
        print(i)
