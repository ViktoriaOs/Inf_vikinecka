#def collatz(n):
    #while n!=1:
        #if n%2==0:
            #n//=2 #n=n//2
            #print(n,  end=",")
        #else:
            #n=3*n+1
            #print(n, end=",")
    #print()
#for i in range(1, 2):
    #collatz(i)

#def deli(m):
    #delitel=2
    #while m!=1:
        #if m % delitel==0:
            #m=m/delitel
            #print(delitel)
        #else:
            #delitel +=1
#deli(56)

#def sucdel(n):
    #m=0
    #for i in range(1,n+1):
        #if n%i==0:
           # m += i
    #return m
#print(sucdel(13))

#def is_perfect(n):
       # if sucdel(n) == n*2:
#            return True
 #       else:
 #           return False
#print(is_perfect(6))        

def poccif(n):
    poc = 0
    while n!=0:
        poc = poc+1
        n = n //10
    return poc
def shredder(n):
    if poccif(n) % 2 == 0:
        pozicia = poccif(n)//2
        sucet = 0
        poc = 0
        while n!=0:
            poc = poc+1
            if poc == pozicia or poc == pozicia-1:
                sucet = sucet+ n%10
            n = n //10
        return sucet
    else:
        pozicia = poccif(n)//2
        sucet = 0
        poc = 0
        while n!=0:
            poc = poc+1
            if poc == pozicia+1:
                sucet = sucet+ n%10
            n = n //10
        return sucet
print(shredder(1234))

