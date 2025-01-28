import random
zoznam=[]

for i in range(0,10):
    zoznam.append(random.randint(0,10000))
vysledok=""
for cislo in zoznam:
    vysledok=vysledok+chr(cislo)
print(vysledok)
#upravit tak aby generoval 10tice dokym nevygeneruhje euurp