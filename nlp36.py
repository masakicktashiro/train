def nlp36():
	with open("neko.txt.mecab","r",encoding="utf-8") as f:
		txt=f.read()
	verb_ls=[i.split("\t")[0] if len(i.split("\t"))>1 else " " for i in txt.split("\n")]
	info_ls=[i.split("\t")[1] if len(i.split("\t"))>1 else " " for i in txt.split("\n")]
	for i in verv_ls:
