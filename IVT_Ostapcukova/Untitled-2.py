from math import pi
from math import acos
from math import degrees
from math import sin
def obsahKruhu(r):
    s = pi*r**2
    return s 

def Heron(a,b,c):
    s = (a+b+c)/2
    S = (s*(s-a)*(s-b)*(s-c))**0.5
    return S

def uholAlpha(a,b,c):
    cosalpha = (-a**2+b**2+c**2)/(2*b*c)
    alpharad = acos(cosalpha)
    alpha = degrees(alpharad)
    return alpha
def uholBeta(a,b,c):
    cosbeta = (-b**2+a**2+c**2)/(2*a*c)
    betarad = acos(cosbeta)
    beta = degrees(betarad)
    return beta
def uholGamma(a,b,c):
    cosgamma = (-c**2+a**2+b**2)/(2*a*b)
    gammarad = acos(cosgamma)
    gamma = degrees(gammarad)
    return gamma
def vpisanaKruznica(a,b,c):
    o = a+b+c
    S = Heron(a,b,c)
    r = (2*S)/o
    return r
def opisanaKruznica(a,b,c):
    r = a/(2*sin(uholAlpha))
    rdegrees = degrees(r)
    return rdegrees
    
    
a = float(input("Zadaj stranu a:"))
b = float(input("Zadaj stranu b:"))
c = float(input("Zadaj stranu c:"))
#print(vpisanaKruznica(a,b,c))
print(opisanaKruznica(a,b,c))
