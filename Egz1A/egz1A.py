#Maciej Janusz
"""
    Idac od prawej do lewej z kazdej katapulty najbardziej oplaca nam sie zniszczyc pierwszy z prawej procesor w jej zasiegu.
    Wybor ten jest na pewno optymalny poniewaz jakbysmy niszczyli procer bardziej na prawo,
    procesory pomiedzy nimi i tak by byly nieosiagalne (strzaly nie moga sie krzyzowac),
    ponadto na pewno nie oplaca sie rezygnowac z takiego strzalu.
    W resultacie usuwajac pierwszy z prawej procesor uzyskujemy prostsza wersje podproblemu
    (niszczymy procesor i idziemy do pierwszej katapulty po lewej)
    O((n+m)*(n+m))
"""


from egz1Atesty import runtests

def battle(P,K,R):
    size = 4*(len(P) + len(K))+1
    catapults = [0] * size
    processors = [False] * size
    for i in range(len(P)):
        processors[P[i]] = True
    for i in range(len(K)):
        catapults[K[i]] = R[i]

    res = 0
    for x in range(size-1, -1, -1):
        if catapults[x] > 0:
            for i in range(1, catapults[x]+1):
                if processors[x+i]:
                    res += 1
                    processors[x+i] = False
                    break

    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( battle, all_tests=True )
