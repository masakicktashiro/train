import nlp50
import re


def nlp51():
    sentences = nlp50.nlp50()
    for i in sentences:
        words = i.split(" ")
        for word in words:
            if re.match(r".*?\.", word):
                word = re.sub(r"([a-z]+?)[\.|,]", r"\1",word)
                yield word+"\n"
            elif re.match(r".*?,",word):
                word = re.sub(r"([a-z]+?)[\.|,]", r"\1",word)
                yield word
            else:
                yield word
if __name__ == "__main__":
    for i in nlp51():
        print(i)
