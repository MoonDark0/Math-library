from MathLib import *
import random
import math
import pygame
fps=60
run=True
timer = pygame.time.Clock()

screen = pygame.display.set_mode((1000,1000))
def Ymev(x,y):
    global xs
    global ys
    global size
    i=0
    numb=0
    while i<len(xs):
        numb=size[i]/((x-xs[i])**2+(y-ys[i])**2)+numb
        i=i+1
    numb=numb-1
    return numb

xs=[]
ys=[]
sxs=[]
sys=[]
size=[]
for i in range(0,7):
    xs.append(random.randint(-10,10))
    ys.append(random.randint(-10,10))
    size.append(random.randint(2,4))
    sxs.append(random.randint(-10,10)/100)
    sys.append(random.randint(-10,10)/100)
a=5
def move():
    global xs
    global ys
    global sxs
    global sys
    i=0
    while i<len(xs):
        if xs[i]>10 or xs[i]<-10:
            sxs[i]=-sxs[i]
        if ys[i]>10 or ys[i]<-10:
            sys[i]=-sys[i]
        xs[i]=xs[i]+sxs[i]
        ys[i]=ys[i]+sys[i]
        i=i+1

while run:
    screen.fill((0,0,0))
    move()
    Ymar(1000,1000,20,20,50,pygame.draw.line,screen,Ymev)
    timer.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
    pygame.display.update()
