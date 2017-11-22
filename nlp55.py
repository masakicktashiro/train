import xml.etree.ElementTree as ET
fname_parsed = "nlp.txt.xml"


def nlp55():
    root = ET.parse(fname_parsed)
    for i in root.iter("token"):
        if i.find("NER").text == "PERSON":
            yield i.find("word").text


if __name__ == "__main__":
    for i in nlp55():
        print(i)
