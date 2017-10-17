import json,gzip
import re
def eng_tex():
    with gzip.open('jawiki-country.json.gz',"rt",encoding="utf-8") as jaw:
        for line in jaw:
            py_text=json.loads(line)
            if py_text["title"]=="イギリス":
                return py_text["text"]
if __name__=="__main__":
    pattern=re.compile(r"^(\[\[.*Category:.*\]\].*)$",re.MULTILINE+re.VERBOSE)
    com_text=pattern.findall(eng_tex())
    for i in com_text:
        print(i)
