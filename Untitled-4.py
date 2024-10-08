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

def deli(m):
    delitel=2
    while m!=1:
        if m % delitel==0:
            m=m/delitel
            print(delitel)
        else:
            delitel +=1
deli(56)
