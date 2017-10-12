
with open("hightemp.txt","r",encoding="utf-8") as f:
    a=f.readlines()
    col1=" ".join([p.split()[0].strip()+"\n" for p in a])
    col2=" ".join([p.split()[1].strip()+"\n" for p in a])
for i,p in enumerate([col1,col2]):
    filename="col"+str(i+1)+".txt"
    with open(filename,"w",encoding="utf-8") as f:
        f.write(p)
