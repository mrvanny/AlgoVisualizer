from turtle import *
import time

def deq():
    sc=Screen()
    sc.bgcolor("black")
    li=Turtle()
    mover=Turtle()
    fl=Turtle()
    bx=Turtle()
    tbx=Turtle()
    tit=Turtle()
    t=Turtle()
    t2=Turtle()
    global l,locarray,x,y,db,obj,arr
    l=0
    locarray={}
    x=-500
    y=200

    db=[bx,tbx]
    obj=[t,t2]

    arr=[10,20,30,40,50,60,70,80]

    def cont():
        li.speed(0)
        li.pensize(5)
        li.pencolor("white")
        li.penup()
        li.goto(x-100,y)
        li.pendown()
        li.forward(1200)
        pos=li.position()
        li.penup()
        li.goto(pos[0],pos[1]-150)
        li.pendown()
        li.backward(1200)

    def Box(loc,i,r):
        global l,locarray
        db[i].penup()
        db[i].home()
        db[i].pendown()
        db[i].speed(0)
        if i==1:
            imx=-700
            by=-100
        else:
            imx=loc[0]-50
            by=loc[1]+45
            


        db[i].hideturtle()
        db[i].pencolor("brown")
        db[i].pensize(3)
        db[i].penup()
        db[i].goto(imx,by)
        if i==0:
            locarray[l]=db[i].position()
            print("locarray",locarray)
            l=l+1
        db[i].hideturtle()
        db[i].pendown()
        db[i].fillcolor("yellow")
        db[i].begin_fill()
        for j in range(2):
            db[i].forward(100)
            db[i].right(90)
            db[i].forward(90)
            db[i].right(90)
        db[i].end_fill()

        place=loc
        fill(place,i,r)



    def fill(loc,i,r):
        fl.speed(0)
        if i==0:
            fx=loc[0]-10
            fy=loc[1]
        else:
            fx=loc[0]+50
            fy=loc[1]-50



        fl.hideturtle()
        fl.pencolor("Black")
        fl.penup()
        fl.goto(fx,fy)
        fl.pendown()
        fl.write(arr[r],font=("",15,"bold"))


    def iarrow(i,loc,flg):
        obj[i].speed(0)

        if i==0:
            obj[i].fillcolor("green")
            txt="F R O N T"
        else:
            obj[i].fillcolor("red")
            txt="R A R E"

        if flg==True:
            ix=loc[0]+110
            iy=loc[1]+27        
            
        else:
            ix=loc[0]+70
            iy=loc[1]+75

        obj[i].penup()
        obj[i].home()
        obj[i].pendown()
        obj[i].speed(0)
        obj[i].hideturtle()
        obj[i].penup()
        obj[i].pensize(2)
        obj[i].goto(ix-70,iy)
        obj[i].right(46)
        obj[i].pendown()

        obj[i].begin_fill()
        obj[i].backward(40)
        obj[i].right(313)
        obj[i].forward(15)
        obj[i].left(90)
        obj[i].forward(30)
        obj[i].right(90)
        obj[i].forward(15)
        obj[i].right(90)



        spc=obj[i].position()

        obj[i].penup()
        obj[i].left(90)
        obj[i].backward(40)
        obj[i].forward(0)
        obj[i].pencolor("white")
        obj[i].write(txt,font=("",12,"bold"))
        obj[i].pencolor("black")
        obj[i].goto(spc[0],spc[1])
        obj[i].right(90)



        obj[i].forward(30)
        obj[i].left(90)
        obj[i].forward(15)
        obj[i].right(128)
        obj[i].forward(35)
        obj[i].end_fill()

    def deque(k):
        global l
        mover.goto(630-((k-1)*120),130)
        mover.showturtle()
        mover.fillcolor("purple")
        mover.pensize(1)
        mover.speed(1)
        mover.penup()
        mover.pencolor("white")
        mover.shape("square")
        mover.shapesize(4,5,3)
        mover.speed(1)
        mover.goto(680,130)
        mover.goto(680,-130)
        time.sleep(1)    
        mx=locarray[l][0]-2
        my=locarray[l][1]+2
        print("deque",locarray[0][0],locarray[0][1])
        mover.hideturtle()
        mover.goto(mx,my)
        l=l+1
        mover.pencolor("black")
        mover.fillcolor("black")
        mover.speed(0)
        mover.pensize(3)
        mover.begin_fill()
        for j in range(2):
            mover.forward(107)
            mover.right(90)
            mover.forward(95)
            mover.right(90)
        mover.end_fill()


    def IamMover(i):
        if i==0:
            des=1
        else:
            des=0
        mover.hideturtle()
        mover.goto(-700,-100)
        loc=mover.position()
        Box(loc,1,i)

        time.sleep(2)

        mover.goto(-650,-30)

        mover.showturtle()
        mover.fillcolor("purple")
        mover.speed(1)
        # mover.speed(0)
        mover.penup()
        mover.pencolor("white")
        mover.shape("square")
        mover.shapesize(4,5,3)
        mover.speed(1)
        # mover.speed(0)
        mover.goto(-650,-30)
        time.sleep(0.5)

        mover.goto(-650,y-70)
        time.sleep(0.5)
        mover.forward(1150-(i*120))

        db[1].clear()


        loc=mover.position()
        mover.hideturtle()
        t.clear()
        iarrow(des,loc,False)
        Box(loc,0,i)

        # time.sleep(2)

    k=1
    tit.penup()
    tit.pencolor("Orange")
    tit.hideturtle()
    tit.goto(-700,310)
    tit.pendown()
    tit.write("D E Q U E U E   O P E R A T I O N ",font=("",22,"bold"))
    cont()
    for i in range(8):
        IamMover(i)
    l=0
    for j in range(8):
        deque(k)
        obj[1].clear()
        iarrow(1,locarray[k],True)
        k=k+1
    done()

def enq():

    sc=Screen()
    sc.bgcolor("black")
    li=Turtle()
    mover=Turtle()
    fl=Turtle()
    bx=Turtle()
    tbx=Turtle()
    tit=Turtle()
    t=Turtle()
    t2=Turtle()

    global x,y,arr

    x=-500
    y=200

    db=[bx,tbx]

    arr=[10,20,30,40,50,60,70,80]

    def cont():
        li.speed(0)
        li.pensize(5)
        li.pencolor("white")
        li.penup()
        li.goto(x,y)
        li.pendown()
        li.forward(1200)
        pos=li.position()
        li.penup()
        li.goto(pos[0],pos[1]-150)
        li.pendown()
        li.backward(1200)

    def Box(loc,i,r):
        db[i].penup()
        db[i].home()
        db[i].pendown()
        db[i].speed(0)
        if i==1:
            imx=-700
            by=-100
        else:
            imx=loc[0]-50
            by=loc[1]+45
            


        db[i].hideturtle()
        db[i].pencolor("brown")
        db[i].pensize(3)
        db[i].penup()
        db[i].goto(imx,by)
        db[i].hideturtle()
        db[i].pendown()
        db[i].fillcolor("yellow")
        db[i].begin_fill()
        for j in range(2):
            db[i].forward(100)
            db[i].right(90)
            db[i].forward(90)
            db[i].right(90)
        db[i].end_fill()

        place=loc
        print(place,i)
        fill(place,i,r)



    def fill(loc,i,r):
        fl.speed(0)
        if i==0:
            fx=loc[0]-10
            fy=loc[1]
        else:
            fx=loc[0]+50
            fy=loc[1]-50



        fl.hideturtle()
        fl.pencolor("Black")
        fl.penup()
        fl.goto(fx,fy)
        fl.pendown()
        fl.write(arr[r],font=("",15,"bold"))


    def iarrow(i,loc):

        obj=[t,t2]
        obj[i].speed(0)
        if i==0:
            obj[i].fillcolor("green")
            txt="F R O N T"
        else:
            obj[i].fillcolor("red")
            txt="R E A R"


        ix=loc[0]+70
        iy=loc[1]+70
        obj[i].penup()
        obj[i].home()
        obj[i].pendown()
        obj[i].speed(0)
        obj[i].hideturtle()
        obj[i].penup()
        obj[i].pensize(2)
        obj[i].goto(ix-70,iy)
        obj[i].right(46)
        obj[i].pendown()

        obj[i].begin_fill()
        obj[i].backward(40)
        obj[i].right(313)
        obj[i].forward(15)
        obj[i].left(90)
        obj[i].forward(30)
        obj[i].right(90)
        obj[i].forward(15)
        obj[i].right(90)



        spc=obj[i].position()

        obj[i].penup()
        obj[i].left(90)
        obj[i].backward(40)
        obj[i].forward(0)
        obj[i].pencolor("white")
        obj[i].write(txt,font=("",12,"bold"))
        obj[i].pencolor("black")
        obj[i].goto(spc[0],spc[1])
        obj[i].right(90)



        obj[i].forward(30)
        obj[i].left(90)
        obj[i].forward(15)
        obj[i].right(128)
        obj[i].forward(35)
        obj[i].end_fill()


    def IamMover(i):
        if i==0:
            des=1
        else:
            des=0
        mover.hideturtle()
        mover.goto(-700,-100)
        loc=mover.position()
        Box(loc,1,i)

        time.sleep(2)

        mover.goto(-650,-30)

        mover.showturtle()
        mover.fillcolor("purple")
        mover.speed(1)
        mover.penup()
        mover.pencolor("white")
        mover.shape("square")
        mover.shapesize(4,5,3)
        mover.speed(1)
        mover.goto(-650,-30)
        time.sleep(0.5)

        mover.goto(-650,y-70)
        time.sleep(0.5)
        mover.forward(1250-(i*120))

        db[1].clear()


        loc=mover.position()
        mover.hideturtle()
        t.clear()
        iarrow(des,loc)
        Box(loc,0,i)

        # time.sleep(2)


    tit.penup()
    tit.pencolor("Orange")
    tit.goto(-200,300)
    tit.pendown()
    tit.write("E N Q U E U E   O P E R A T I O N ",font=("",22,"bold"))
    cont()
    for i in range(8):
        IamMover(i)


    done()    
