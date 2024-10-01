#uloha 1
x = range(1,11)
#for n in x:
    #print(n)

#uloha 2a
N=(15)
y = range(1,N+1)
#for n in y:
   # print(n)

#uloha 2b
#def cisla_riadok(N):
    #print(', '.join(str(i) for i in range(1, N + 1)))
#cisla_riadok(N)

#uloha 3
M=15
#for n in range(5, M + 1, 2):
    #print(n)

#uloha 4
O=9
#for n in range(1, O + 1):
    #print(n, n**2)

#uloha 5
import math

#def vypis_odmocniny(odkial, pokial):
    #for cislo in range(odkial, pokial + 1):
        #odmocnina = round(cislo**(1/2), 2)
        #print(cislo, odmocnina)
#vypis_odmocniny(1, 10)

#uloha 6
#def vypocitaj_hodnoty():
    #for x in range(1, 21): 
        ##if x == 3:
            #print("x = 3 Nie je definovana")
        #else:
            #y = (x**2 - 1) / (x - 3)
            #print(f"x = {x}, y = {y}")
#vypocitaj_hodnoty()

#uloha 7
#def delitelne_troma(N):
    #for cislo in range(1, N + 1):
        #if cislo % 3 == 0:
            #print(cislo)
#delitelne_troma(20)

#uloha 8
#def delitelne_dvoma(N):
    #for cislo in range(1, 21):
        #if cislo % 2 == 0:
            #print(cislo)
#delitelne_dvoma(20)

#uloha 9
#def vypis_neparne(z, k):
    #for cislo in range(z, k + 1):
        #if cislo % 2 != 0:
            #print(cislo)
#vypis_neparne(6, 10)

#uloha 10


#uloha 11
#def delitelne_siedmymi_a_styrmi(N):
    #for cislo in range(0, N + 1):
        #if cislo % 7 == 0 and cislo % 4 == 0:
            #print(cislo)
#delitelne_siedmymi_a_styrmi(100)

#uloha 12
#def sucet(N):
    #sucet = sum(range(1, N + 1))
    #return sucet
#print(sucet(10))  #vysledok je 55

#uloha 13
#def sucet_parnych(N):
    #sucet = sum(cislo for cislo in range(1, N + 1) if cislo % 2 == 0)
    #return sucet
#print(sucet_parnych(10))  

#uloha 14
#def pocet_delitelnych_osmimi(zaciatok, koniec):
    #pocet = sum(1 for cislo in range(zaciatok, koniec + 1) if cislo % 8 == 0)
    #return pocet
#print(pocet_delitelnych_osmimi(1, 100)) 
