#napis funkciu ktora vrati sucet neparnych cisel v intervale z k kde z a k su vstupne parametre funkcie sucpar

#def sucpar(z,k):
    #x=0
    #for i in range(z, k+1):
        #if i %2 ==1:
            #x=x+i
    #return x
#print(sucpar(6,10))

#modifikuj proigram tak ye koncia cifrz na 3
def cifry(a,b):
    x=0
    for i in range(a,b):
        if i %10==3:
            x=x+i
    return x
print(cifry(1,30))

#napis funkxciu ktora vypise parne cisla zo zadaneho intervalu vratane jeho hranic
def parne(a,b):
    for i in range(a,b+1):
        if i%2==0:
            print(i)

parne(10,20)

#vsetkz stvorcif cisla kde prve dvojcislie je mocninou 2
def drticka():
    for i in range (1000,10000):
        if i//100==16:
            print(i)
        if i//100==32:
            print(i)
        if i//100==64:
            print(i)
drticka()