def sucet(z,k):
    x=0
    for i in range(z,k+1):
        if i%2==1:
           x=x+i
    return x
print(sucet(6,10))