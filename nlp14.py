def n_output(tx_file):
    import sys
    n=sys.argv[1]
    with open(tx_file,"r",encoding="utf-8")as tx:
        f=tx.readlines()[:5]
        print("".join(f))
if __name__=="__main__":
    n_output("col3.txt")
