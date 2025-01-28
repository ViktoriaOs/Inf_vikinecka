#fr = open("ahoj.txt","r",encoding="utf-8")
#for riadok in fr:
    #print(riadok,end="")
#prvyriadok= fr.readline()
#print(prvyriadok)
#for riadok in fr:
   # print(riadok)

fr = open("D:\škola\Downloads\words.txt","r", encoding="UTF-8")
counter = 0
for riadok in fr:
    if "E" in riadok:
        counter+=1
print(counter)