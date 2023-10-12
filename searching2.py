from turtle import *
import time

def Binsearch():

    s=Screen()

    s.bgcolor("black")

    v=Turtle()
    fil=Turtle()
    sch=Turtle()
    t=Turtle()
    tit=Turtle()

    global x,y,val,f,svalue,arr
    x=-400
    y=200
    val=21
    f=80
    svalue=89

    #Array must be in sorted order
    arr=[88,60,16,21,44,56,96,97] 



    arr.sort()


    def iarrow(i,color):

        if color=="red":
            t.fillcolor("red")
            lmh="H I G H"
        elif color=="blue":
            t.fillcolor("blue")
            lmh="L O W  "
        elif color=="green":
            lmh="M I D"
            if (arr[mid]==arr[low]):
                t.fillcolor("red")
            else:
                t.fillcolor("green")
        else:
            pass

        ix=-350
        iy=200
        t.penup()
        t.home()
        t.pendown()
        t.speed(0)
        t.hideturtle()
        t.penup()
        t.pensize(2)
        t.goto(ix+(80*i),iy)
        t.right(46)
        t.pendown()

        t.begin_fill()
        t.backward(40)
        t.right(313)
        t.forward(15)
        t.left(90)
        t.forward(30)
        t.right(90)
        t.forward(15)
        t.right(90)

        loc=t.position()

        t.penup()
        t.left(90)
        t.backward(27)
        t.forward(0)
        t.pencolor("white")
        t.write(lmh,font=("",12,"bold"))
        t.pencolor("black")
        t.goto(loc[0],loc[1])
        t.right(90)

        t.pendown()
        
        t.forward(30)
        t.left(90)
        t.forward(15)
        t.right(128)
        t.forward(35)
        t.end_fill()
        

        

    def schval(pos):
        if arr[pos]==svalue:
            sch.fillcolor("Green")
        else:
            sch.fillcolor("red")

        sch.speed(0)
        sch.hideturtle()
        sch.penup()
        sch.pencolor("white")
        sx=-380+(80*pos)
        sy=100
        sch.goto(sx,sy)
        sch.pendown()

        sch.begin_fill()
        for i in range(2):
            sch.forward(50)
            sch.right(90)
            sch.forward(30)
            sch.right(90)
        sch.end_fill()

        fillvalues(1,sx,100,30,True)






    def fillvalues(boxes,imx,imy,imh,ctr):
        global c
        fil.pencolor("black")
        fil.speed(0)
        i=0
        if ctr==True:
            fy=imy-24
            fx=imx+10
        else:
            fy=imy-(imh/2)
            fx=imx+40

        fil.hideturtle()
        for i in range(boxes):
            fil.penup()
            fil.goto(fx,fy)
            fil.pendown()
            if ctr==True:
                fil.write(svalue,font=("",16,"bold"))
            else:
                fil.write(arr[i],font=("",16,"bold"))
            fx=fx+80


    def arraycreate(boxes):
        v.speed(0)
        v.hideturtle()
        v.pencolor("black")
        v.pensize(3)
        v.fillcolor("yellow")
        for j in range(boxes):
            bx=x+(80*j)
            v.penup()
            v.goto(bx,y)
            v.pendown()
            v.begin_fill()
            for i in range(2):
                v.forward(f)
                v.right(90)
                v.forward(f)
                v.right(90)
            v.end_fill()

        fillvalues(boxes,x,y,80,False)



    tit.hideturtle()
    tit.goto(-650,320)
    tit.pencolor("white")
    tit.write("B I N A R Y   S E A R C H",font=("",25,"bold"))


    def Bsearch():
        global high,low,mid
        n=8
        i=0
        high=n-1
        low=i

        while(low<=high):
            
            mid=(low+high)//2
            print("mid",mid)

            if  svalue<arr[mid]:
                # print("svalue<mid")
                print("high Low Mid",high,low,mid)
                schval(mid)
                iarrow(low,"blue")
                iarrow(high,"red")
                iarrow(mid,"green")

                time.sleep(3)
                sch.clear()
                t.clear()
                high=mid-1
                if arr[low]==svalue:
                    break

            
            elif (svalue>arr[mid]):
                # print("svalue>mid")
                print("high Low Mid",high,low,mid)

                schval(mid)
                iarrow(low,"blue")
                iarrow(high,"red")
                iarrow(mid,"green")

                time.sleep(3)
                sch.clear()
                t.clear()
                low=mid+1
                if arr[high]==svalue:
                    break

            elif (svalue==arr[mid]):
                schval(mid)
                iarrow(low,"blue")
                iarrow(high,"red")
                iarrow(mid,"green")
                time.sleep(3)
                sch.clear()
                t.clear()
                tit.penup()
                tit.goto(-220,10)
                tit.pencolor("orange")
                tit.pendown()   
                tit.write("Element Found In Array At Index",font=("",18,"bold"))
                tit.forward(380)  
                tit.write(mid,font=("",18,"bold"))
                break          

            else:
                print("elsesr")
                break
            
            
            print("high Low Mid =",high,low,mid)

        
        if(mid==low):
            tit.penup()
            tit.goto(-220,10)
            tit.pencolor("white")
            tit.pendown()   
            tit.write("Element Not Found In Array",font=("",18,"bold"))

    arraycreate(8)
    Bsearch()

    done()


def linsearch():

    s=Screen()
    s.bgcolor("black")

    v=Turtle()
    fil=Turtle()
    sch=Turtle()
    t=Turtle()
    tit=Turtle()
    global x,y,val,f,arr
    x=-400
    y=200

    val=56 #value for searching

    f=80

    arr=[16,56,96,1,6,21,44,97]



    def iarrow(i):
        if arr[i-1]==val:
            t.fillcolor("Green")
        else:
            t.fillcolor("red")

        ix=-430
        iy=200
        t.penup()
        t.home()
        t.pendown()
        t.speed(0)
        t.hideturtle()
        t.penup()
        t.pensize(2)
        t.goto(ix+(80*i),iy)
        t.right(46)
        t.pendown()

        t.begin_fill()
        t.backward(40)
        t.right(313)
        t.forward(15)
        t.left(90)
        t.forward(30)
        t.right(90)
        t.forward(15)
        t.right(90)
        t.forward(30)
        t.left(90)
        t.forward(15)
        t.right(128)
        t.forward(35)
        t.end_fill()
        
        time.sleep(3)

        

    def schval(pos):
        if arr[pos]==val:
            sch.fillcolor("Green")
        else:
            sch.fillcolor("red")

        sch.speed(0)
        sch.hideturtle()
        sch.penup()
        sch.pencolor("white")
        sx=-380+(80*pos)
        sy=100
        sch.goto(sx,sy)
        sch.pendown()

        sch.begin_fill()
        for i in range(2):
            sch.forward(50)
            sch.right(90)
            sch.forward(30)
            sch.right(90)
        sch.end_fill()

        fillvalues(1,sx,100,30,True)






    def fillvalues(boxes,imx,imy,imh,ctr):
        global c
        fil.pencolor("black")
        fil.speed(0)
        i=0
        if ctr==True:
            fy=imy-24
            fx=imx+10
        else:
            fy=imy-(imh/2)
            fx=imx+40

        fil.hideturtle()
        for i in range(boxes):
            fil.penup()
            fil.goto(fx,fy)
            fil.pendown()
            if ctr==True:
                fil.write(val,font=("",16,"bold"))
            else:
                fil.write(arr[i],font=("",16,"bold"))
            fx=fx+80


    def arraycreate(boxes):
        v.speed(0)
        v.hideturtle()
        v.pencolor("black")
        v.pensize(3)
        v.fillcolor("yellow")
        for j in range(boxes):
            bx=x+(80*j)
            v.penup()
            v.goto(bx,y)
            v.pendown()
            v.begin_fill()
            for i in range(2):
                v.forward(f)
                v.right(90)
                v.forward(f)
                v.right(90)
            v.end_fill()

        fillvalues(boxes,x,y,80,False)



    tit.hideturtle()
    tit.goto(-150,300)
    tit.pencolor("white")
    tit.write(">>  L I N E A R  S E A R C H  <<",font=("",22,"bold"))
    arraycreate(8)
    for i in range(8):
        schval(i)
        iarrow(i+1)
        sch.clear()
        t.clear()
        if val==arr[i]:
            tit.penup()
            tit.goto(-200,-100)
            tit.pendown()
            tit.pencolor("orange")
            tit.write("Element Found At Location",font=("",18,"bold"))
            tit.goto(120,-100)
            tit.write(i,font=("",18,"bold"))

            break


    done()

