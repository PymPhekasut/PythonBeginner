#turtle program example
import turtle
import random

tao = turtle.Pen() #build turtle
tao.shape('turtle')


def Rect(x,y,size=30, clr ='black'):
    tao.penup() #lift pen up
    tao.goto(x,y) #follow the position
    tao.color(clr) #change color
    tao.pendown() #put pen down
    #-----------drawing sqaure--------
    for i in range(4): #for loop
            tao.forward(size)
            tao.left(90)
    #---------------------------------
    tao.penup() #lift pen up



##----------Run Program--------------##
allcolor = ['red','green','blue','orange']

count = int (input('what is square dimension?: ')) #user input

for i in range(count): #for loop 
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    print(x,y)
    select_color = random.choice(allcolor)
    Rect(x,y,40,select_color)
