import nlp41true
import nlp42
fname_parsed = "neko.txt.cabocha"


def nlp46():
    chunks_by_bun=nlp41true.neko_lines()
    for chunks in chunks_by_bun:
        for i,chunk in enumerate(chunks):
            if "動詞" in [i.pos for i in chunks[chunk.dst].morphs] and \
            "助詞" in [i.pos for i in chunk.morphs]:
                yield [i.base for i in chunks[chunk.dst].morphs
                if i.pos == "動詞"][0] + \
                "\t" + " ".join([i.surface for i in chunk.morphs
                 if i.pos == "助詞"]) + \
                 "\t" + "".join([i.surface for i in chunk.morphs])
                
if __name__ == "__main__":
    flg = 0
    for i,doushi_joshi in enumerate(nlp46()):
        
        if i == 0:
            doushi = doushi_joshi.split("\t")[0]
            joshi_ls=[doushi_joshi.split("\t")[1]]
            raw_joshi_ls=[doushi_joshi.split("\t")[2]]
        
        if i == 0:
            continue

        elif doushi == doushi_joshi.split("\t")[0]:
            joshi_ls.append(doushi_joshi.split("\t")[1])
            raw_joshi_ls.append(doushi_joshi.split("\t")[1])
            flg = 0    
        else:
            print(doushi + "\t" + " ".join(joshi_ls) + "\t" + \
            " ".join(raw_joshi_ls)) 
            doushi = doushi_joshi.split("\t")[0]
            joshi_ls = [doushi_joshi.split("\t")[1]]
            raw_joshi_ls = [doushi_joshi.split("\t")[2]]
            flg = 1
    if flg == 0:
        print(doushi*"\t"+" ".join(joshi_ls) + "\t" + \
        " ".join(raw_joshi_ls))
