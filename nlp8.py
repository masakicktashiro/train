def cipher(sq):
    return "".join([chr(219-ord(p))if "a"<=p<="z" else p for p in sq])
if __name__=="__main__":
    print(cipher("Hello world"))
    print(cipher("I am human"))
