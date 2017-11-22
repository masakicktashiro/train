from tqdm import tqdm
import nlp72
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
import codecs
import numpy as np
from stemming.porter2 import stem
fname = ("sentiment.txt")
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


def mk_x_data(fname):
    pos_ls,neg_ls = nlp72.nlp72(stop_ls=stop_word,fname=fname)
    pos_neg_ls = pos_ls + neg_ls
    with codecs.open(fname,"r",encoding="utf-8") as lines:
        all_x_data = None
        for line in tqdm(lines):
            line = [stem(i.strip()) for i in line.split()]
            x_data = np.zeros(len(pos_ls)+len(neg_ls))
            for text in line:
                if text in pos_neg_ls:
                    x_data[pos_neg_ls.index(text)] = 1
            if all_x_data is None:
                all_x_data = x_data
            else:
                all_x_data = np.vstack([all_x_data,x_data])
        print("all_x_data->",all_x_data)
        return all_x_data


def mk_y_data(fname):
    with codecs.open(fname,"r",encoding="utf-8") as lines:
        all_y_data = None
        for line in lines:
            y_data = np.zeros(1)
            if line.split()[0] == "-1":
                y_data[0] = -1
            else:
                y_data[0] = 1
            if all_y_data is None:
                all_y_data = y_data
            else:
                all_y_data = np.vstack([all_y_data,y_data])
    print("all_y_data->",all_y_data)
    return all_y_data 


def prediction(fname,):
    clf = LogisticRegression()
    x_train,x_test,y_train,y_test = train_test_split(
        mk_x_data(fname),mk_y_data(fname),random_state=0, test_size=0.3)
    clf.fit(x_train,y_train)
    print("train_accuracy->",accuracy_score(
        y_true=y_train,y_pred=clf.predict(x_train)))
    print("test_accuracy->",accuracy_score(
        y_true=y_test,y_pred=clf.predict(x_test)))


if __name__ == "__main__":
    print(mk_x_data(fname=fname))
    prediction(fname=fname)

