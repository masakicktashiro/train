import codecs
import nlp71
import re
from stemming.porter2 import stem
fname = "sentiment.txt"
fname_sosei = "sentiment_analyze.txt"
stop_word = ["a","all","almost","also","although","an","any","are",
            "as","at","be","because","been","both","but","by","can",
            "could","did","do","does","eihter","for","from","had",
            "has","have","having","he","her","here","hers","him",
            "his","how","however","i","if","in","into","is","it",
            "its","just","||","me","might","Mr","Mrs","Ms","my",
            "no","non","nor","not","of","on","one","only","onto",
            "our","ours","s","shall","she","should","since","so","some",
            "still","such","than","that","the","their","them","then",
            "there","there","therefore","these","they","this","those",
            "though","through","thus","to","too","until","ve","very",
            "was","we","were","what","when","where","whether","which",
            "while","who","whose","why","will","with","would","yet",
            "you","your","yours"]


def nlp72(stop_ls,fname):
    pos_dic = dict()
    pos_ls = []
    neg_dic = dict()
    neg_ls = []
    new_text = ""
    obj_pos_ls = []
    obj_neg_ls = []
    with codecs.open(fname,"r",encoding="utf-8") as f:
        text = f.readlines()
    for line in text:
        line = [stem(i.strip()) for i in line.split()]
        flg = None
        for i, wd in enumerate(line):
            if i == 0 and wd == "1":
                flg ="1"
            elif i == 0 and wd =="-1":
                flg = "-1"
            #pos,negリス作成
            if wd in stop_ls:
                line.remove(wd)
            elif flg == "1":
                pos_ls.append(wd)
                if pos_dic.get(wd) == None:
                    pos_dic[wd] = 1
                else:
                    pos_dic[wd] += 1
            else:
                neg_ls.append(wd)
                if neg_dic.get(wd) == None:
                    neg_dic[wd] = 1
                else:
                    neg_dic[wd] += 1
    
    for wd in pos_dic.keys():
        if neg_dic.get(wd) is not None:
            if pos_dic[wd]-neg_dic.get(wd) > 5:
               obj_pos_ls.append(wd)
        elif pos_dic[wd] > 5:
            obj_pos_ls.append(wd)

    for wd in neg_dic.keys():
        if pos_dic.get(wd) is not None:
            if neg_dic[wd]-pos_dic.get(wd) > 5:
               obj_neg_ls.append(wd)
        elif neg_dic[wd] > 5:
            obj_neg_ls.append(wd)
    return obj_pos_ls, obj_neg_ls

if __name__ == "__main__":
    obj_pos_ls, obj_neg_ls = nlp72(stop_ls=stop_word,fname=fname)
    #print("pos->",obj_pos_ls)
    #print("neg->",obj_neg_ls)
    print(len(obj_pos_ls))
