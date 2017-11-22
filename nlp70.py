import os
import random
import codecs
pos_data = "rt-polarity.pos"
neg_data = "rt-polarity.neg"
fname = "sentiment.txt"


def nlp70():
    f = []
    g = []
    with codecs.open(pos_data,"r",encoding="windows-1252") as pos_lines:
            for pos_line in pos_lines:
                f.append("1 " + pos_line)
    with codecs.open(neg_data,"r",encoding="windows-1252") as neg_lines:
            for neg_line in neg_lines:
                g.append("-1 " + neg_line)
    f.extend(g)
    random.shuffle(f)
    if not os.path.exists(fname):
        with open(fname,"w",encoding="utf-8") as t:
            for i in f:
                t.write(i)

if __name__ == "__main__":
    nlp70()
