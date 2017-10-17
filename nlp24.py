import nlp22no
import re
pattern=re.compile(r"^.*\[\[File:(.+?)(?=\.)(.+?)(?=\|).*$",re.MULTILINE)
pattern2=re.compile(r"^.*\[\[ファイル:(.+?)(?=\.)(.+?)(?=\|).*$",re.MULTILINE)
file1=pattern.findall(nlp22no.eng_tex())
file2=pattern2.findall(nlp22no.eng_tex())
for i in file1+file2:
    print(i[0]+i[1])
