import random
f=open("kakugen.txt","r",encoding="utf_8")
lines =f.readlines()

kakugen=lines[random.randrange(len(lines))]
print(kakugen.rstrip("\n"))
