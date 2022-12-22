
#all complex are a,b
import math
def Cadd(a0,b0,a1,b1):
    return a0+a1,b0+b1
def Csub(a0,b0,a1,b1):
    return a0-a1,b0-b1
def Cmul(a0,b0,a1,b1):
    return a0*a1-b0*b1,b0*a1+a0*b1
def Coon(a,b):
    divisor=a*a+b*b
    na=a/divisor
    nb=-b/divisor
    return na,nb
def Cdiv(a0,b0,a1,b1):
    an,bn=Coon(a1,b1)
    an,bn=Cmul(a0,b0,an,bn)
    return an,bn
def Cpow(a,b):
    return a*a-b*b,2*a*b
def Cexp(a,b,e):
    if e==0:
        return 1,0
    if e%2==0:
        a1,b1=Cexp(a,b,e/2)
        na,nb=Cmul(a1,b1,a1,b1)
    else:
        a1,b1=Cexp(a,b,e-1)
        na,nb=Cmul(a,b,a1,b1)
    return na,nb
def Ceti(i):
    a=math.cos(i)
    b=math.sin(i)
    return a,b
def Cetp(a,b):
    c=math.e**a
    an,bn=Ceti(b)
    return Cmul(c,0,an,bn)
