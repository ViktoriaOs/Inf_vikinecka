#def parnecisla(a, b):
    #for i in range(a, b+1, 2): #ak je na konci 2 tak idu cisla ob jedno
        #print(i)
#parnecisla(42,100)

#musite nacitavat cisla pokial ich sucet nie je vacsi ako 500
#sucet = 0
#p = 0
#while sucet <500:
    #temp = int(input("Zadaj mi celé číslo:"))
    #if temp%2 ==0:   
        #sucet=(sucet+temp)
        #p=p+1 #p+=1
#print(sucet/p)

import random
#sucet = 0
#p = 0
#for i in range(0,100):
    #temp=random.randrange(1, 11)
    #sucet = sucet+temp
    #p+=1
    #print(temp)
    #print(sucet)
#print(sucet/p)

#hadzeme kockou xy krat
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
for i in range(1, 100000):
    temp=random.randrange(1, 7)
    if temp==1:
        a+=1
    if temp==2:
        b+=1
    if temp==3:
        c+=1
    if temp==4:
        d+=1
    if temp==5:
        e+=1
    if temp==6:
        f+=1
print(a,b,c,d,e,f)