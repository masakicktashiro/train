with open("col1.txt","r",encoding="utf-8") as col1:
    with open("col2.txt","r",encoding="utf-8") as col2:
        col3_ls="".join([str(i).strip("\n\t")+"\t"+str(p).strip("\n\t")+"\n" for i,p in zip(col1.readlines(),col2.readlines())])
        with open("col3.txt","w",encoding="utf-8")as col3:
            col3.write(col3_ls)
