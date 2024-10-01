#def cif(cislo):
    #cifra=0
   # while cislo>0:
        # ld = cislo%10 #odtrhne poslednu cifru
         #cifra = cifra*10 +ld 
         #cislo = cislo//10 #pripravi cislo na prechod do dalsieho cyklu tym ze ju znizi
    #return cifra
#print (cif(15453))


def convertToBin(number):
     powTen = 1
     result = 0
     while number !=0:
          modulo = number % 2
          result = result+powTen * modulo 
          number = number // 2
          powTen *=10
     return result
print (convertToBin(32))
