Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle.Pen()
>>> tao.shape('turtle')
>>> tao.forward(50)
>>> tao.left(90)
>>> tao.right(45)
>>> tao.left(45)
>>> tao.forward(50)
>>> tao.left(90)
>>> tao.forward(50)
>>> tao.left(90)
>>> tao.forward(50)
>>> tao.left(90)
>>> tao.left(180)
>>> tao.reset()
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> range(5)
range(0, 5)
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> for i in [50, 60, 70]:
	print(i)

	
50
60
70
>>> print (i)
70
>>> for i in range(4):
	print('step walk', i)
	tao.forward(50)
	tao.left(90)

	
step walk 0
step walk 1
step walk 2
step walk 3
>>> tao.goto(-100,100)
>>> tao.reset()
>>> tao.penup()
>>> tao.goto(-100,100)
>>> for i in range(4):
	print('walk step', i)
	tao.forward(50)
	tao.left(90)

	
walk step 0
walk step 1
walk step 2
walk step 3
>>> tao.pendown()
>>> for i in range(4):
	print('walk step',i)
	tao.forward(50)
	tao.left(90)

	
walk step 0
walk step 1
walk step 2
walk step 3
>>> tao.reset()
>>> def Rect():
	for i in range(4):
		tao.forward(50)
		tao.left(90)

		
>>> Rect()
>>> tao.clear()
>>> tao.goto(100,100)
>>> Rect()
>>> tao.reset()
>>> def Rect():
	tao.pendown()
	for i in range(4):
		tao.forward(50)
		tao.left(90)
	tao.penup()

	
>>> Rect()
>>> 
>>> tao.reset()
>>> tao.penup()
>>> tao.goto(100,100)
>>> Rect()
>>> tao.goto(-100,-100)
>>> Rect()
>>> tao.gptp(-100,-100)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    tao.gptp(-100,-100)
AttributeError: 'Turtle' object has no attribute 'gptp'
>>> tao.goto(-100,-100)
>>> Rect()
>>> tao.goto(50,-100)
>>> Rect()
>>> tao.reset()
>>> def Rect(size):
	tao.pendown()
	for i in range(4):
		tao.forward(size)
		tao.left(90)
	tao.penup()

	
>>> Rect(30)
>>> tao.goto(-100,-100)
>>> Rect(200)
>>> def Rect(size=30):
	tao.pendown()
	for i in range(4):
		tao.forward(size)
		tao.left(90)
	tao.penup()

	
>>> Rect()
>>> Rect(100)
>>> Rect(120)
>>> tao.reset()
>>> for sz in [30,50,80]:
	Rect(sz)

	
>>> tao.reset()
>>> for sz in [30,50,80,40,100,200]:
	Rect(sz)

	
>>> def Rect(x,y,size=30):
	tao.penup()
	tao.goto(x,y)
	tao.pendown()
	for i in range(4):
		tao.forward(size)
		tao.left(90)
	tao.penup()

	
>>> tao.reset()
>>> Rect(100,100)
>>> for i in range(5)
SyntaxError: invalid syntax
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> def Rect(x,y,size=30, clr ='black'):
	tao.penup()
	tao.goto(x,y)
	tao.color(clr)
	tao.pendown()
	for i in range(4):
		tao.forward(size)
		tao.left(90)
	tao.penup()

	
>>> Rect(150,150,40,'green')
>>> 