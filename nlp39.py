def nlp39():
    import nlp36
    import numpy as np
    import matplotlib.pyplot as plt
    hindo_dic=nlp36.nlp36()
    plt.bar(np.log(list(range(1,len(hindo_dic.keys())+1))),np.log(sorted(list(hindo_dic.values()),reverse=True)))
    plt.show()
    
if __name__=="__main__":
    nlp39()
