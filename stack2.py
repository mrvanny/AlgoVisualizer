from turtle import *
import time

def popitm():


    s=Screen()
    s.bgcolor("Black")

    c=Turtle()
    b=Turtle()
    p=Turtle()
    f=Turtle()
    t=Turtle()
    fill=Turtle()
    tit=Turtle()

    global k,loc,n,x,y,pm,arr

    k=0
    loc=0
    n=7
    x=-320
    y=200

    pm=[-160,-245]

    arr=[10,20,30,40,50,60,70]


    def textpop(i):
        f.hideturtle()
        f.goto(250,300)
        # b.goto(px,py)
        f.pencolor("white")
        f.write("P O P E D   I T E A M",font=("",18))
        f.forward(250)
        f.write(arr[i],font=("",18))
        f.penup()

    def fillval(i,h,w):
        fill.hideturtle()
        fill.pencolor("black")
        fill.hideturtle()
        fill.goto(loc[0],loc[1]+10)
        fill.forward(w/2)
        fill.write(arr[i],font=("",18,"bold"))
        fill.penup()


    def peaktxt(i):
        t.hideturtle()
        t.pencolor("red")
        t.penup()
        t.goto(loc[0]+5,loc[1]+60)
        t.pendown()
        t.write("PEAK =",font=("",18,"bold"))
        t.forward(100)
        t.write(arr[i],font=("",18,"bold"))
        time.sleep(3) 
        t.clear()

    def perm(i,color):
        global loc
        h=50
        w=160

        p.hideturtle()
        p.speed(0.5)
        p.penup()
        p.pensize(3)
        if color=="yellow":
            p.pencolor("green")
            p.fillcolor("yellow")
        else:
            p.pencolor("black")
            p.fillcolor("Black")

        p.goto(pm[0]-80,pm[1]+i*60)
        loc=p.position()
        print(loc)
        p.pendown()
        p.begin_fill()
        p.forward(w)
        p.left(90)
        p.forward(h)
        p.left(90)
        p.forward(w)
        p.left(90)
        p.forward(h)
        p.end_fill()
        p.penup()
        p.home()
        
        fillval(i,h,w)
        if color=="black":
            time.sleep(2)



    def pop(i):
        global k
        px=-240 
        py=175
        b.hideturtle()
        b.fillcolor("red")
        b.pencolor("white")
        b.shape("square")
        b.shapesize(2.5,8,2)
        b.penup()
        b.speed(0)

        b.goto(px+80,py+20-(i*50))
        b.showturtle()
        b.speed(1.1)
        time.sleep(2)
        b.goto(px+160,py+100)
        b.goto(px+350,py+100)
        b.goto(px+350+150,(py+100)-200)
        k=b.position()
        print(k)
        b.pendown()
        textpop((n-1)-i)



    def createstack():
        c.hideturtle()
        c.pensize(5)
        c.pencolor("white")
        c.penup()
        c.goto(x,y)
        c.pendown()
        #make edges of container
        c.goto(-295,170)
        c.right(90)
        c.forward(450)
        c.left(90)
        c.forward(250)
        c.left(90)
        c.forward(450)
        k=c.position()
        c.goto(k[0]+25,k[1]+30) #make edges of container


    tit.pencolor("orange")
    tit.penup()
    tit.hideturtle()
    tit.goto(-650,300)
    tit.pendown()
    tit.write("P O P   O P E R A T I O N   I N   S T A C K",font=("",18,"bold"))
    createstack()

    for j in range(n):

        for i in range(n-j):
            b.hideturtle()
            perm(i,"yellow") 

        peaktxt((n-1)-j)
        f.clear()
        pop(j)
        perm(n-(j+1),"black")
        p.clear()


    done()

def pushitm():

    s=Screen()
    s.bgcolor("Black")

    c=Turtle()
    b=Turtle()
    p=Turtle()
    f=Turtle()
    t=Turtle()
    fill=Turtle()
    tit=Turtle()

    global k,loc,x,y,arr

    k=0
    loc=0
    x=-320
    y=200

    arr=[10,20,30,40,50,60,70]

    def fillval(i,h,w):
        fill.hideturtle()
        fill.pencolor("black")
        fill.hideturtle()
        fill.goto(loc[0],loc[1]+10)

        fill.forward(w/2)
        fill.write(arr[i],font=("",18,"bold"))

        t.hideturtle()
        t.pencolor("GREEN")
        t.penup()
        t.goto(loc[0]+5,loc[1]+60)
        t.pendown()
        t.write("PEAK =",font=("",18,"bold"))
        t.forward(100)
        t.write(arr[i],font=("",18,"bold"))
        time.sleep(3)


    def perm(i):
        global loc
        h=50
        w=160

        p.hideturtle()
        p.speed(0.5)
        p.penup()
        p.pensize(3)
        p.pencolor("green")
        p.fillcolor("yellow")
        p.goto(k[0]-80,k[1]-20+(i*2))
        loc=p.position()
        p.pendown()
        p.begin_fill()
        p.forward(w)
        p.left(90)
        p.forward(h)
        p.left(90)
        p.forward(w)
        p.left(90)
        p.forward(h)
        p.end_fill()
        p.penup()
        p.home()

        fillval(i,h,w)



    def push(i):
        global k
        b.hideturtle()
        b.fillcolor("red")
        b.pencolor("white")
        b.shape("square")
        b.shapesize(2.5,8,2)
        b.penup()
        b.speed(0)
        f.hideturtle()
        f.goto(x-260,y+100)
        b.goto(x-200,y+50)
        f.pencolor("white")
        f.write("P U S H  =",font=("",18))
        f.forward(130)
        f.write(arr[i],font=("",18))
        f.penup()
        b.showturtle()
        b.speed(1.1)
        time.sleep(2)
        b.goto(x+150,y+30)
        b.goto(x+160,-245+(i*65))
        k=b.position()
        b.pendown()



    def createstack():
        c.hideturtle()
        c.pensize(5)
        c.pencolor("white")
        c.penup()
        c.goto(x,y)
        c.pendown()
        c.goto(-295,170)
        c.right(90)
        c.forward(450)
        c.left(90)
        c.forward(250)
        c.left(90)
        c.forward(450)
        k=c.position()
        c.goto(k[0]+25,k[1]+30)


    tit.pencolor("orange")
    tit.penup()
    tit.hideturtle()
    tit.goto(20,300)
    tit.pendown()
    tit.write("P U S H   O P E R A T I O N   I N   S T A C K",font=("",18,"bold"))
    createstack()
    for i in range(7):
        push(i)
        b.hideturtle()
        f.clear()
        perm(i)    
        t.clear()


    done()
