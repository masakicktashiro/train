a="paraparaparadise"
b="paragraph"
import nlp5
X=nlp5.myn_gram(a,2)[1]
Y=nlp5.myn_gram(b,2)[1]
print("和集合:",set(X+Y))
print("差集合:",{p for p in X if p not in Y})
print("積集合:",{p for p in X if p in Y})
print("se in X or Y",("se" in set(X+Y)))
