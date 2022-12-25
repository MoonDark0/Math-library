
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
#Visuals
def Ymar(Dx,Dy,Ranx,Rany,Sqar,funct,screen,ev):#Screen size X,Screen size Y,Range X,Range y, Quality,Draw function, screen, evaluate function
    lookup={0:[],
            1:[3,4],
            2:[3,2],
            3:[2,4],
            4:[1,2],
            5:[1,4,2,3],
            6:[1,3],
            7:[1,4],
            8:[1,4],
            9:[1,3],
            10:[1,2,3,4],
            11:[1,2],
            12:[2,4],
            13:[2,3],
            14:[3,4],
            15:[]}
    sx=Ranx/(Sqar+1)
    kx=(-Ranx/2)
    sy=Rany/(Sqar+1)
    ky=(-Rany/2)
    Values=[[0]*(Sqar+1) for _ in range(Sqar+1)]
    for iy in range((Sqar+1)):
        for ix in range((Sqar+1)):
            Values[iy][ix]=ev(ix*sx+kx,-(iy*sy+ky))
    draw=[]
    for yd in range(Sqar):
        for xd in range(Sqar):
            Square=[Values[yd][xd],Values[yd][xd+1],Values[yd+1][xd+1],Values[yd+1][xd]]
            Ymsd(Square,lookup,xd,yd,Sqar,Dx,Dy,funct,screen)
    return
def Ymsd(Val,Look,dx,dy,Qua,Sx,Sy,funct,screen):#Marching Squares Draw
    i=0
    cases=0
    Px=dx*(Sx/Qua)
    Py=dy*(Sy/Qua)
    while i<4:
        cases=cases*2
        if Val[i]>0:
            cases=cases+1
        else:
            cases=cases+0
        i=i+1
    todraw=Look[cases]
    i=0
    while i<len(todraw)/2:
        if todraw[i]==1:
            d1=(Px+Ymsi(Val[0],Val[1])*(Sx/Qua),Py)
        if todraw[i]==2:
            d1=(Px+(Sx/Qua),Py+Ymsi(Val[1],Val[2])*(Sy/Qua))
        if todraw[i]==3:
            d1=(Px+Ymsi(Val[3],Val[2])*(Sx/Qua),Py+(Sy/Qua))
        if todraw[i]==4:
            d1=(Px,Py+Ymsi(Val[0],Val[3])*(Sy/Qua))
        if todraw[i+1]==1:
            d2=(Px+Ymsi(Val[0],Val[1])*(Sx/Qua),Py)
        if todraw[i+1]==2:
            d2=(Px+(Sx/Qua),Py+Ymsi(Val[1],Val[2])*(Sy/Qua))
        if todraw[i+1]==3:
            d2=(Px+Ymsi(Val[3],Val[2])*(Sx/Qua),Py+(Sy/Qua))
        if todraw[i+1]==4:
            d2=(Px,Py+Ymsi(Val[0],Val[3])*(Sy/Qua))
        i=i+2
        funct(screen,(255,255,255),d1,d2)
    return
def Ymsi(a,b):#marching squares interpolate
    return -a/(b-a)
