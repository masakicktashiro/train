def nlp35():
	flag=1
	kaburi_ls=[]
	with open("neko.txt.mecab","r",encoding="utf-8") as f:
		txt=f.read()
		verb_ls=[i.split("\t")[0] for i in txt.split("\n")]
		info_ls=[i.split("\t")[1] if len(i.split("\t"))>1 else " " for i in txt.split("\n")]
	for i in range(len(verb_ls)-1):
		if verb_ls[i]==verb_ls[i+1] and info_ls[i].split(",")[0]=="名詞":
			flag+=1
		elif flag>1:
			kaburi_ls.append((verb_ls[i-1],flag))
			flag=1
		else:
			flag=1
	if flag>2:
		kaburi_ls.append((verv_ls[len(verv_ls)-1],flag))
	return kaburi_ls

if __name__=="__main__":
	for i in nlp35():
		print(i[0],"が",i[1],"回")
