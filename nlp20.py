import json
def eng_tex():
    with open("jawiki-country.json","r",encoding="utf-8") as jaw:
        f=jaw.read().strip()
        for i in f.split("\n"):
            temp=json.loads(i)
            if temp["title"]=="イギリス":
                print(temp["text"])
                return temp["text"]
if "__name__"=="__main__":
    eng_tex()
eng_tex()
