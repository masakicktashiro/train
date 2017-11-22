import xml.etree.ElementTree as ET
import nlp53cp
fname_parsed = "nlp.txt.xml"


def nlp54():
    root = ET.parse(fname_parsed)
    for wd,le,pos in zip(
        root.iter("word"),root.iter("lemma"),root.iter("POS")):
        yield wd.text + "\t" + le.text + "\t" + pos.text

if __name__ == "__main__":
    for i in nlp54():
        print(i)
