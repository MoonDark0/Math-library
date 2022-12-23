
#all complex are a,b
import math
#Complex Numbers
def Cadd(a0,b0,a1,b1):
    return a0+a1,b0+b1
def Csub(a0,b0,a1,b1):
    return a0-a1,b0-b1
def Cmul(a0,b0,a1,b1):
    return a0*a1-b0*b1,b0*a1+a0*b1
def Coon(a,b):    #invert
    divisor=a*a+b*b
    na=a/divisor
    nb=-b/divisor
    return na,nb
def Cdiv(a0,b0,a1,b1):#division
    an,bn=Coon(a1,b1)
    an,bn=Cmul(a0,b0,an,bn)
    return an,bn
def Cpot(a,b):#Power of two
    return a*a-b*b,2*a*b
def Cexp(a,b,e):#exponentiantion
    if e==0:
        return 1,0
    if e%2==0:
        a1,b1=Cexp(a,b,e/2)
        na,nb=Cmul(a1,b1,a1,b1)
    else:
        a1,b1=Cexp(a,b,e-1)
        na,nb=Cmul(a,b,a1,b1)
    return na,nb
def Ceti(i):#e to imaginaru
    a=math.cos(i)
    b=math.sin(i)
    return a,b
def Cetp(a,b): #e to something
    c=math.e**a
    an,bn=Ceti(b)
    return Cmul(c,0,an,bn)
#Sort
def Squi(array): #quicksort
    if len(array)<2:
        return array
    pivot=array[int(len(array)/2)]
    pivots=[]
    small=[]
    big=[]
    i=0
    while i<len(array):
        if array[i]==pivot:
            pivots.append(array[i])
        if array[i]>pivot:
            big.append(array[i])
        if array[i]<pivot:
            small.append(array[i])
        i=i+1
    return Squi(small)+pivots+Squi(big)

def Ssor(lis): #is sorted
        leng=len(lis)
        i=0
        rn=0
        while i<leng:
            if lis[i]>rn:
                rn=lis[i]
            if lis[i]<rn:
                return False
            i=i+1
        return True
