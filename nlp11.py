with open("hightemp.txt","r",encoding="utf-8") as f:
    a=f.read().strip()
print(a.replace("/t"," "))
