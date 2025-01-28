#vytvor prazdbny zoznam potom napln raandom cislami 1-100
import random
a=0
b=0
zoznam=[]
for i in range(10):
    zoznam.append(random.randint(1,100))
for i in zoznam:
    if i%2==1:
        a+=1
maxik = zoznam
pozmax=0
for i in range(1, len(maxik)):
    if b <= maxik[i]:
        b=maxik[i]
        pozmax=i
print(zoznam,b,pozmax+1)