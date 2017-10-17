import nlp22no
import re
pattern=re.compile(r"^|(.*?)(?=\s=\s)(.*?)$",re.MULTILINE)
text=pattern.findall(nlp22no.eng_tex())
dic={}
for i in text:
    if i[0]!=None:
        dic[i[0]]=i[1]
print(dic)
