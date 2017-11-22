import nlp51
from stemming.porter2 import stem


def nlp52():
    words = nlp51.nlp51()
    for word in words:
        if word.endswith("\n"):
            word = word.strip("\n")
            yield word+"\t"+stem(word)+"\n"
        else:
            yield word+"\t"+stem(word)

if __name__ == "__main__":
    word_stem = nlp52()
    for i in word_stem:
        print(i)
