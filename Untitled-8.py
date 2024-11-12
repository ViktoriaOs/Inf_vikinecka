fero="gfgflsgfgdfgjdfgjfg"
jano=fero[1:3:] #start:koniec:skok ak skok nie je napisany default je 1 start je default 0 a koniec je posledne cislo strtingu. ak dame do skoku -1 tak pojde string odzadu
peto="radar"
niko="jelenovipivonelej"
tomas="kobylamamalybok"
if niko==niko[::-1]:
   # print("je to palindrom")
   pass

#vypise postupne cele slovo
#b = input("napis mi nieco:")
#for i in range(0,len(b)+1):
    #print(b[:i:])
    




#domaca> abz to slovo postupne vzpisoval odyadu
#napis program na neviem  co
#a=input("napis mi cislo:")
#scitanie=0
#for cislica in a:
#    scitanie+=int(cislica)
#print(scitanie)



#def shredder(ret):
    #samo="aeiouy"
    #for i in samo:
       # print("Samohlaska",i,"sa tam nachadza:",ret.count(i))
#a=input("napis nieco:")
#shredder(a)
a=input("napis nieco so zatvprkami:")
def neviem(a):
    zat1=a.find("(")
    zat2=a.find(")")
    if zat2-zat1>0:
        print(a[zat1+1:zat2:])

#pokial sa tam nachadza "(" tak: zavolam funkciu a a zpravim hujuju bujuju aby som zatvorku odtal doatala
def opakuj(a):
   b = a
   while b.find("(")!=-1:
      neviem(b)
      b=b[:b.find("("):]+b[b.find(")")+1::]
opakuj(a)