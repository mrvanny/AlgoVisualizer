from turtle import *
import time

def insbeg():

    sc=Screen()
    sc.bgcolor("black")

    li=Turtle()
    li2=Turtle()
    tit=Turtle()

    li.hideturtle()
    li2.hideturtle()

    li.pencolor("white")
    li2.pencolor("white")

    global cx,cy,f,arr,arr2,nulll
    cx=-370
    cy=200
    f=150

    arr=[10,20,30,40,50]
    arr2=[60,10,20,30,40,50]
    nulll=["N","U","L","L"]




    def createll(rotate,nw,values):
        li.speed(0)
        li.hideturtle()
        li2=li
        li2.pensize(3)

        if nw==True:
            li.fillcolor("red")
        else:
            li.fillcolor("purple")

        for j in range(rotate):
            bx=cx+(180*j)
            li.penup()
            li.goto(bx,cy)
            li2=li
            li2.hideturtle()
            # li.forward(30)
            li.pendown()

            li.begin_fill()
            for i in range(2):
                li.forward(f-80)
                li.right(90)
                li.forward(f-98)
                li.right(90)
            li.end_fill()

            wx=bx+30
            wy=cy-30
            li.penup()
            li.goto(wx,wy)
            li.pendown()
            li.pencolor("black")  
            if values==False:
                if nw==True:
                    li.write("60",font=("",12,"bold"))
                else:
                    li.write(arr[j],font=("",12,"bold"))
            else:
                li.write(arr2[j],font=("",12,"bold"))


            if j==(rotate-1) and nw==False:
                li.penup()            
                li.goto(wx+55,cy-17)            
                li.pendown()            
                li.pencolor("white")
                k=cy-17    
                for i in range(len(nulll)):
                    li.write(nulll[i],font=("",8))
                    k=k-12
                    li.penup()
                    li.goto(wx+55,k)
                    li.pendown()

            li.penup()        
            li.goto(bx,cy)
            li.pendown() 

            li.pencolor("white")

            li2.forward(f-80+25)
            li2.right(90)
            li2.forward(f-98)
            li2.right(90)
            li2.forward(25)

            if nw==True:
                li2.speed(1)
                li2.backward(25)
                li2.left(90)
                li2.backward((f-100)/2)
                li2.pensize(4)
                li2.left(90)
                li2.forward(f-135)
                li2.right(90)
                li2.forward(100)
                li2.left(90)
                li2.forward(80)
                li2.pensize(3)       

            if j<(rotate-1):
                    li2.backward(25)
                    li2.left(90)
                    li2.backward((f-100)/2)
                    li2.pensize(4)
                    li2.left(90)
                    li2.forward(f-65)
                    li2.pensize(3)
            

            li2.penup()
            li2.home()
            li2.pendown()


    def newnode():
        global cy,cx
        tit.hideturtle()
        tit.penup()
        tit.goto(-620,330)
        tit.pendown()
        tit.pencolor("white")
        tit.write("New Node To Be Inserted",font=("",15,"bold"))
        cy=300
        cx=-570
        createll(1,True,False)

    def updatedll():
        tit.penup()
        tit.goto(-400,-20)
        tit.pendown()
        tit.pencolor("white")
        tit.write("Updated LinkedList After Insertion Of Node At The Beginning  ",font=("",18,"bold"))    
        
        global cy,cx
        cy=-70
        cx=-600
        createll(6,False,True)




    tit.hideturtle()
    tit.penup()
    tit.goto(-70,280)
    tit.pendown()
    tit.pencolor("white")
    tit.write("Insertion Of Node At The Beginning Of LinkedList",font=("",18,"bold"))

    createll(5,False,False)
    newnode()
    updatedll()
    done()

def insend():

    sc=Screen()
    sc.bgcolor("black")

    li=Turtle()
    li2=Turtle()
    tit=Turtle()

    li.hideturtle()
    li2.hideturtle()

    li.pencolor("white")
    li2.pencolor("white")

    global cx,cy,f,arr,arr2,nulll

    cx=-570
    cy=200
    f=150

    arr=[10,20,30,40,50]
    arr2=[10,20,30,40,50,60]

    nulll=["N","U","L","L"]



    # To Draw Linked List Nodes
    def createll(rotate,nw,values):
        li.speed(0)
        li.hideturtle()
        li2=li
        li2.pensize(3)
        
        # If It Is New Node 
        if nw==True:
            li.fillcolor("red")
            dd=f-80+25
            wdt=f-80
            inr=30
        else:
            li.fillcolor("purple")
            dd=f-80+25
            wdt=f-80
            inr=30

        for j in range(rotate):
            bx=cx+(180*j)
            li.penup()
            li.goto(bx,cy)
            li2=li
            li2.hideturtle()
            # li.forward(30)
            li.pendown()

            li.begin_fill()
            for i in range(2):
                li.forward(wdt)
                li.right(90)
                li.forward(f-98)
                li.right(90)
            li.end_fill()

        # To Fill Values in Nodes
            wx=bx+inr
            wy=cy-30
            li.penup()
            li.goto(wx,wy)
            li.pendown()
            li.pencolor("black") 

            #To FIll Values From  Origional or Updated Array 

            if values==False:
                if nw==True:
                    li.write("60",font=("",12,"bold"))
                else:
                    li.write(arr[j],font=("",12,"bold"))
            else:                
                li.write(arr2[j],font=("",12,"bold"))

            if j==5 and values==True:
                li.penup()            
                li.goto(wx+55,cy-17)            
                li.pendown()            
                li.pencolor("white")
                k=cy-17    
                for i in range(len(nulll)):
                    li.write(nulll[i],font=("",8))
                    k=k-12
                    li.penup()
                    li.goto(wx+55,k)
                    li.pendown()

            li.penup()        
            li.goto(bx,cy)
            li.pendown() 

            li.pencolor("white")

            # To Draw Separation Line i.e Another Line

            li2.forward(dd)
            li2.right(90)
            li2.forward(f-98)
            li2.right(90)
            li2.forward(25)





            if nw==True:
                li2.speed(1)


                li2.right(90)
                li2.forward((f-100)/2)
                li2.pensize(4)
                li2.left(90)
                li2.penup()
                li2.forward(wdt)
                li2.pendown()
                li2.forward(f-135)

                li2.left(90)
                li2.forward(100)
                li2.right(90)
                li2.forward(120)
                li2.pensize(3)       

    #   Connecting Lines Between Two Nodes 
            if j<(rotate-1):
                    li2.backward(25)
                    li2.left(90)
                    li2.backward((f-100)/2)
                    li2.pensize(4)
                    li2.left(90)
                    li2.forward(f-65)
                    li2.pensize(3)
            

            li2.penup()
            li2.home()
            li2.pendown()


    # To Draw New Node

    def newnode():
        global cy,cx
        tit.hideturtle()
        tit.penup()
        tit.goto(380,330)
        tit.pendown()
        tit.pencolor("white")
        tit.write("New Node To Be Inserted",font=("",15,"bold"))
        cy=300
        cx=380
        createll(1,True,False)

    # To Print Final LinkedList
    def updatedll():
        tit.penup()
        tit.goto(-400,-20)
        tit.pendown()
        tit.pencolor("white")
        tit.write("Updated LinkedList After Insertion Of Node At The End  ",font=("",18,"bold"))    
        
        global cy,cx
        cy=-70
        cx=-600
        createll(6,False,True)




    tit.hideturtle()
    tit.penup()
    tit.goto(-470,280)
    tit.pendown()
    tit.pencolor("white")
    tit.write("Insertion Of Node At The End Of LinkedList",font=("",18,"bold"))

    createll(5,False,False)
    newnode()
    updatedll()

    done()    

def delbeg():
    sc=Screen()
    sc.bgcolor("black")

    li=Turtle()
    li2=Turtle()
    tit=Turtle()
    cr=Turtle()

    li.hideturtle()
    li2.hideturtle()

    li.pencolor("white")
    li2.pencolor("white")

    global cx,cy,f,arr,arr2

    cx=-550
    cy=200
    f=150

    arr=[10,20,30,40,50,60]
    arr2=[60,10,20,30,40,50]


    def connectinglines(li2,flag):

        # For Erasing First Connecting line
        if flag==True:
            li2.penup()
            li2.goto(-452,173.5)
            li2.pendown()
            li2.pencolor("black")
            li2.pensize(4)
            li2.forward(f-70.6)
            li2.pensize(3)

        #For drawing all connection lines
        else:
            li2.pencolor("white")
            li2.pensize(4)
            li2.forward(f-65)
            li2.pensize(3)



    def redcross(n):
        if n==0:
            return

        cr.hideturtle()
        cr.pensize(4)
        cr.pencolor("Red")
        cr.penup()
        cr.goto(-430,184)
        cr.pendown()
        cr.goto(-410,160)
        cr.penup()
        cr.goto(-430,160)
        cr.pendown()
        cr.goto(-410,184)

        time.sleep(1)

        cr.clear()

        redcross(n-1)

    def createll(rotate,nw,values):
        li.speed(0)
        li.hideturtle()
        li2=li
        li2.pensize(3)



        for j in range(rotate):
            bx=cx+(180*j)
            li.penup()
            li.goto(bx,cy)
            li2=li
            li2.hideturtle()
            li.pendown()

            #Differentiate First Node From Others

            if j==0 and values==False:
                li.fillcolor("red")
            else:
                li.fillcolor("purple")

            li.begin_fill()
            for i in range(2):
                li.forward(f-80)
                li.right(90)
                li.forward(f-98)
                li.right(90)
            li.end_fill()


            wx=bx+30
            wy=cy-30
            li.penup()
            li.goto(wx,wy)
            li.pendown()
            li.pencolor("black")  

            if rotate==6:
                li.write(arr[j],font=("",12,"bold"))
            else:
                li.write(arr[j+1],font=("",12,"bold"))

            li.penup()        
            li.goto(bx,cy)
            li.pendown() 

            li.pencolor("white")

            li2.forward(f-80+25)
            li2.right(90)
            li2.forward(f-98)
            li2.right(90)
            li2.forward(25) 

            if j<(rotate-1):
                li2.backward(25)
                li2.left(90)
                li2.backward((f-100)/2)
                li2.left(90)
                connectinglines(li2,False)

            

            li2.penup()
            li2.home()
            li2.pendown()



    def updatedll():
        #To Print Final LinkedList
        tit.penup()
        tit.goto(-400,-20)
        tit.pendown()
        tit.pencolor("white")
        tit.write("Updated LinkedList After Deletion Of Node From The Beginning  ",font=("",18,"bold"))    
        
        global cy,cx
        cy=-70
        cx=-600
        createll(5,False,True)





    tit.hideturtle()
    tit.penup()
    tit.goto(-70,280)
    tit.pendown()
    tit.pencolor("white")
    tit.write("Deletion Of Node From The Beginning Of LinkedList",font=("",18,"bold"))

    createll(6,False,False)

    tit.hideturtle()
    tit.penup()
    tit.goto(-620,230)
    tit.pendown()
    tit.pencolor("white")
    tit.write("First  Node To Be Deleted",font=("",15,"bold"))
    redcross(3)
    connectinglines(li2,True)

    updatedll()

    done()    

def delend():
    sc=Screen()

    sc.bgcolor("black")

    li=Turtle()
    li2=Turtle()
    tit=Turtle()
    cr=Turtle()

    li.hideturtle()
    li2.hideturtle()

    li.pencolor("white")
    li2.pencolor("white")

    global cx,cy,f,arr,arr2,nulll

    cx=-550
    cy=200
    f=150

    nulll=["N","U","L","L"]

    arr=[10,20,30,40,50,60]
    arr2=[60,10,20,30,40,50]


    def connectinglines(li2,flag):

        # For Erasing Last Connecting line
        if flag==True:
            li2.speed(0)
            li2.penup()
            li2.goto(267.7,173.5)
            li2.pendown()
            li2.pencolor("black")
            li2.pensize(4)
            li2.forward(f-70.6)
            li2.pensize(3)

        #For drawing all connection lines
        else:
            li2.pencolor("white")
            li2.pensize(4)
            li2.forward(f-65)
            li2.pensize(3)


    # To Print Red Cross
    def redcross(n):
        if n==0:
            return

        cr.hideturtle()
        cr.pensize(4)
        cr.pencolor("Red")
        cr.penup()
        cr.goto(300,184)
        cr.pendown()
        cr.goto(330,160)
        cr.penup()
        cr.goto(300,160)
        cr.pendown()
        cr.goto(330,184)

        time.sleep(1)

        cr.clear()

        redcross(n-1)

    def createll(rotate,nw,values):
        li.speed(0)
        li.hideturtle()
        li2=li
        li2.pensize(3)



        for j in range(rotate):
            bx=cx+(180*j)
            li.penup()
            li.goto(bx,cy)
            li2=li
            li2.hideturtle()
            li.pendown()

            #Differentiate First Node From Others

            if j==5 and values==False:
                li.fillcolor("red")
            else:
                li.fillcolor("purple")

            li.begin_fill()
            for i in range(2):
                li.forward(f-80)
                li.right(90)
                li.forward(f-98)
                li.right(90)
            li.end_fill()


            wx=bx+30
            wy=cy-30
            li.penup()
            li.goto(wx,wy)
            li.pendown()
            li.pencolor("black")  

            if rotate==6:
                li.write(arr[j],font=("",12,"bold"))
            else:
                li.write(arr[j],font=("",12,"bold"))

            if j==(rotate-1):
                li.penup()            
                li.goto(wx+55,cy-17)            
                li.pendown()            
                li.pencolor("white")
                k=cy-17    
                for i in range(len(nulll)):
                    li.write(nulll[i],font=("",8))
                    k=k-12
                    li.penup()
                    li.goto(wx+55,k)
                    li.pendown()



            li.penup()        
            li.goto(bx,cy)
            li.pendown() 

            li.pencolor("white")

            li2.forward(f-80+25)
            li2.right(90)
            li2.forward(f-98)
            li2.right(90)
            li2.forward(25) 

            if j<(rotate-1):
                li2.backward(25)
                li2.left(90)
                li2.backward((f-100)/2)
                li2.left(90)
                connectinglines(li2,False)

            

            li2.penup()
            li2.home()
            li2.pendown()



    def updatedll():
        #To Print Final LinkedList
        tit.penup()
        tit.goto(-400,-20)
        tit.pendown()
        tit.pencolor("white")
        tit.write("Updated LinkedList After Deletion Of Node From The End  ",font=("",18,"bold"))    
        
        global cy,cx
        cy=-70
        cx=-600
        createll(5,False,True)





    tit.hideturtle()
    tit.penup()
    tit.goto(-500,320)
    tit.pendown()
    tit.pencolor("white")
    tit.write("Deletion Of Node From The End Of LinkedList",font=("",18,"bold"))

    createll(6,False,False)

    tit.hideturtle()
    tit.penup()
    tit.goto(280,240)
    tit.pendown()
    tit.pencolor("white")
    tit.write("Last Node To Be Deleted",font=("",15,"bold"))
    redcross(3)
    connectinglines(li2,True)

    updatedll()

    done()

def insbetn():
    sc=Screen()
    sc.bgcolor("black")

    li=Turtle()
    li2=Turtle()
    tit=Turtle()
    jn=Turtle()
    cr=Turtle()
    e=Turtle()
    li.hideturtle()
    li2.hideturtle()

    li.pencolor("white")
    li2.pencolor("white")

    global cx,cy,f,bx,h,arr,arr2,nulll

    cx=-500
    cy=180
    f=150
    bx=0
    h=0
    arr=[10,20,30,40,50]
    arr2=[10,20,50,30,40]
    nulll=["N","U","L","L"]

    def redcross(n):
        if n==0:
            return

        cr.hideturtle()
        cr.pensize(5)
        cr.pencolor("Red")
        cr.penup()
        cr.goto(-120,170)
        cr.pendown()
        cr.goto(-80,140)
        cr.penup()
        cr.goto(-120,140)
        cr.pendown()
        cr.goto(-80,170)

        time.sleep(1)
        cr.clear()

        redcross(n-1)



    def eraseline():
        ex=cx+95*2+145
        e.speed(0)
        e.pencolor("Black")
        e.pensize(5)
        e.goto(ex+3.5,cy-(h/2))
        e.forward(137.2)

    def createll(rotate,nw,values):
        global bx,h
        li.speed(0)
        li.hideturtle()
        li2=li
        li2.speed(0)
        li2.pensize(3)
        h=f-98
        if nw==True:
            li.fillcolor("red")
        else:
            li.fillcolor("purple")

        for j in range(rotate):

            bx=cx+(240*j)
            li.penup()
            li.goto(bx,cy)
            li2=li
            li2.hideturtle()
            # li.forward(30)
            li.pendown()

            for i in range(2):
                li.begin_fill()
                li.forward(f-80)
                li.right(90)
                li.forward(h)
                li.right(90)
                li.end_fill()

            wx=bx+30
            wy=cy-30
            li.penup()
            li.goto(wx,wy)
            li.pendown()
            li.pencolor("black")  
            if values==False:
                if nw==True:
                    li.write("50",font=("",12,"bold"))
                else:
                    li.write(arr[j],font=("",12,"bold"))
            else:
                li.write(arr2[j],font=("",12,"bold"))


            if j==(rotate-1) and nw==False:
                li.penup()            
                li.goto(wx+55,cy-17)            
                li.pendown()            
                li.pencolor("white")
                k=cy-17    
                for i in range(len(nulll)):
                    li.write(nulll[i],font=("",8))
                    k=k-12
                    li.penup()
                    li.goto(wx+55,k)
                    li.pendown()

            li.penup()        
            li.goto(bx,cy)
            li.pendown() 

            li.pencolor("white")

            li2.forward(f-80+25)
            li2.right(90)
            li2.forward(f-98)
            li2.right(90)
            li2.forward(25)

            if nw==True:
                li2.speed(1)
                li2.backward(25)
                li2.left(90)
                li2.backward((f-100)/2)
                li2.pensize(4)
                li2.left(90)

                li2.forward(f-140)
                li2.right(90)
                li2.forward(120)
                li2.left(90)
                li2.forward(10)
                li2.pensize(3)

                jn.hideturtle()
                jn.speed(1)
                jn.penup()
                jn.goto(-135,300)   
                jn.pensize(4)    
                jn.pencolor("White")
            
                jn.left(270)
                jn.forward((f-100)/2)
                jn.right(90)
                jn.pendown()
                jn.forward(10)
                jn.left(90)
                jn.forward(120)
                jn.right(90)
                jn.forward(18)

            if j<(rotate-1):
                li2.backward(25)
                li2.left(90)
                li2.backward((f-100)/2)
                li2.pensize(4)
                li2.left(90)
                li2.forward(f-5)
                li2.pensize(3)
            

            li2.penup()
            li2.home()
            li2.pendown()


    def newnode():
        tit.hideturtle()
        tit.penup()
        tit.goto(-70,320)
        tit.pendown()
        tit.pencolor("white")
        tit.write("New Node To Be Inserted",font=("",12,"bold"))

        global cy,cx
        cy=300
        cx=-135
        createll(1,True,False)

    def updatedll():
        tit.penup()
        tit.goto(-400,-20)
        tit.pendown()
        tit.pencolor("white")
        tit.write("Updated LinkedList After Insertion Of Node In Between 2 Nodes  ",font=("",18,"bold"))    
        
        global cy,cx
        cy=-70
        cx=-600
        createll(5,False,True)





    tit.hideturtle()
    tit.penup()
    tit.goto(-730,330)
    tit.pendown()
    tit.pencolor("white")
    tit.write("Insertion Of Node At The In Between Of LinkedList",font=("",15,"bold"))

    createll(4,False,False)
    redcross(3)
    eraseline()
    newnode()
    updatedll()
    done()

