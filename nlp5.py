def myn_gram(sq,n):
    ch_n_gram_ls=[]
    wd_n_gram_ls=[]
    if type(sq)==str:
        sq=sq.split()
    for i in range(len(sq)-n+1):
        wd_n_gram_ls.append(sq[i:i+n])
    sq="".join(sq)
    for p in range(len(sq)-n+1):
        ch_n_gram_ls.append(sq[p:p+n])
    return wd_n_gram_ls,ch_n_gram_ls
if __name__=="__main__":
    print("文字バイグラム:",myn_gram(sq="I am an NLPer",n=2)[0])
    print("単語バイグラム:",myn_gram(sq="I am an NLPer",n=2)[1])
