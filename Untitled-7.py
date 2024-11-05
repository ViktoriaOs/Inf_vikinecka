#a=input("mapis mi nieco:")
#b=input("napis pismenko ktore hladas:")
#print(a.count(b))
#na=""
#for znak in a:
    #if znak=="a":
        #na=na+"e" #+ znamena prilepenie nie spocitanie
    #else:
        #na=na+znak
#print(na)

import random    
dlzka=int(input("napis mi dlzku:"))
samohlasky="aeiouy"
spoluhlasky="qwrtzpsdfghjklxcvbnm"
novy=""
for i in range(0,dlzka):
    if i%2==0:
        novy=novy+random.choice(spoluhlasky)
    else:
        novy=novy+random.choice(samohlasky)
print(novy)