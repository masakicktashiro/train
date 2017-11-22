import re
stop_ls = ["test","movie","make"]
fname = "sentiment.txt"

def nlp71(stop_ls):
    
    with open(fname,"r",encoding="utf-8") as f:
        for line in f:
            for stop_wd in stop_ls:
                if re.match(r"^.*?{}.*?".format(stop_wd),line) is not None:
                    yield True
                else:
                    yield False

if __name__ == "__main__":
    for i in nlp71(stop_ls=stop_ls):
        print(i)
