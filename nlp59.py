import xml.etree.ElementTree as ET
fname_parsed = "nlp.txt.xml"


def list_pls(ls,n):
    return [i+n if i is not None else None for i in ls]


def list_ap(ls,wd):
    return [i.append(wd) for i in ls]


def nlp59():
    root = ET.parse(fname_parsed)
    
    for parse in root.iter("parse"):
        parse = parse.text
        kakko_num = [None]
        toji_num = []
        res_wd_ls = []
        wd_ls = []

        for wd in parse.split(" "):
            
            if wd == "(NP":
                kakko_num[-1] = 0
                kakko_num.append(None)
                toji_num.append(0)
                wd_ls.append([])
            
            if kakko_num[0] is not None:
                
                del_num = None

                if ")" in wd:
                    list_ap(wd_ls,wd.strip(")"))
                    toji_num = list_pls(
                        toji_num,len(wd.strip(wd.strip(")"))))
                
                elif "(" in wd:
                    kakko_num = list_pls(kakko_num,1)
                
                for i,kakko,toji in zip(range(len(kakko_num)-1),
                    kakko_num[:len(kakko_num)-1],toji_num):

                    if kakko - toji <= 0:
                        kakko_num = kakko_num[:len(kakko_num)-1] 
                        toji_num = toji_num[:len(toji_num)-1]
                        res_wd_ls.append(" ".join(wd_ls[i]))
                        if del_num is None:
                            del_num = i
                if del_num is not None:
                    wd_ls = wd_ls[:del_num]
                    del_num = None

        yield res_wd_ls
if __name__ == "__main__":
    wd_lses = nlp59()
    for wd_ls in wd_lses:
        for wd in wd_ls:
            print(wd)
