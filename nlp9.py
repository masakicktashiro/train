def typo(sq):
    import numpy as np
    sq=sq.split()
    new_sq_ls=[]
    for n in sq:
        n=n.strip(".,:")
        if len(n)>4:
            new_sq_id=[0]+list(np.random.permutation(range(1,len(n)-1)))+[len(n)-1]
        else:
            new_sq_id=list(range(len(n)))
        new_sq_ls.append("".join([n[i] for i in new_sq_id]))
    print(" ".join(new_sq_ls))
if __name__=="__main__":
    typo("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")
