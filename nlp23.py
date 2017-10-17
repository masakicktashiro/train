import nlp22no
import re
pattern=re.compile(r"^(={2,})\s*(.+?)\s*\1.*$",re.MULTILINE)
text=pattern.findall(nlp22no.eng_tex())
for i in text:
    length=len(i[0])-1
    print("{tab}{text}{length}".format(tab="\t"*(length-1),text=i[1],length=length))
