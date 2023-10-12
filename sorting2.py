from turtle import*
import time

def bub():      

      v=Turtle()
      fill=Turtle()
      fil=Turtle()
      t=Turtle()
      ta=Turtle()
      w=Turtle()
      tell=Turtle()
      tit=Turtle()

      s=Screen()

      s.bgcolor("Black")

      global wy,k,swi,tay,f,c,x,ct,y,midarrow,iy,arr

      k=1
      swi=0
      tay=192
      f=80
      c=False
      x=-700
      ct=0
      y=300
      midarrow=0
      iy=305

      arr=[60,40,12,42,67]

      # arr=[7,-1,-3,2,3]

      # arr=[16,56,96,1,6]

      w.hideturtle()
      title=[" B U B B L E   S O R T "]
      w.pencolor("orange")
      w.penup()
      w.goto(40,310)
      w.pendown()

      w.write(title[0],font=("",20,"bold"))

      library=["int i,j,temp","int arr[]={77,21,93,20,3}","for (i=0 i<n;i++)","     for(j=0;j<n-1-i;j++)","          if(arr[j]>arr[j+1])",
      "              temp=arr[j]","              arr[j]=arr[j+1]","              arr[j+1]=temp" ]

      wy=250


      def scale():
            tit.hideturtle()
            tit.goto(550,350)
            tit.pencolor("white")
            tit.pensize(3)
            tit.fillcolor("Green")

            tit.begin_fill()
            for i in range(4):
                  tit.forward(25)
                  tit.right(90)
            tit.end_fill()
            tit.penup()
            tit.goto(583,332)
            tit.pendown()
            tit.write("Swap Two Values",font=("",12))

            tit.penup()
            tit.goto(550,300)
            tit.pendown()
            tit.fillcolor("Red")
            tit.pencolor("white")
            tit.begin_fill()
            for i in range(4):
                  tit.forward(25)
                  tit.right(90)
            tit.end_fill()

            tit.penup()
            tit.goto(583,280)
            tit.pendown()
            tit.write("Don't Swap Values",font=("",12))    



      def writee():
            w.pencolor("White")

            w.hideturtle()
            w.pensize(3)
            global wy
            for i in range(len(library)):
                  w.penup()
                  w.goto(40,wy)
                  w.pendown()
                  w.write(library[i],font=("",18))
                  wy=wy-40





      def tarrow(i,f):
            global midarrow,tay
            if swi==0:
                  wtx=-720
                  wty=120
            else:
                  wtx=-680
                  wty=345

            tell.pencolor("white")
            tell.hideturtle()
            tell.speed(0)
            tell.pensize(3)
            tell.penup()
            tell.goto(wtx,wty)
            tell.pendown()

            fillvalues()

            if i<((len(arr)-1)-swi):
                  if arr[i]<arr[i+1]:
                        des="Smaller Than"
                        d="So Dont Swap Them" 
                        ta.fillcolor("Red")
                  else:
                        des="Greater Than"
                        d="So Swap Them"
                        ta.fillcolor("Green")


                  if arr[i]<arr[i+1]:
                        s=f"{arr[i]} is {des} {arr[i+1]} {d}"
                        tell.write(s,font=("",17,"bold"))

                  else:
                        s=f"{arr[i]} is {des} {arr[i+1]} {d}"
                        tell.write(s,font=("",17,"bold"))


                  if arr[i]>arr[i+1]:
                        tmp=arr[i]
                        arr[i]=arr[i+1]
                        arr[i+1]=tmp



            # To make Sure length of Two array should not cross length of array and Should not goto already swapped array
            if i<(len(arr)-1)-swi:
                  midarrow=80

                  #To draw two arrays at same time
                  iarrow(i)
                  iarrow(i+1)

                  tax=x+15+(80*i)     #start position of first array 

                  ta.hideturtle()
                  ta.speed(0)
                  ta.penup()
                  ta.home()
                  ta.pendown()

                  ta.pensize(4)
                  ta.pencolor("white")
                  ta.penup()
                  ta.goto(tax,tay)
                  ta.pendown()


                  ta.begin_fill()
                  ta.forward(40)
                  ta.left(90)
                  ta.forward(20)
                  ta.left(90)
                  ta.forward(40)
                  ta.left(90)
                  ta.forward(20)
                  ta.end_fill()


                  ta.left(90)
                  ta.forward(20)
                  ta.right(90)
                  ta.forward(20)
                  ta.left(90)
                  ta.forward(midarrow)
                  ta.left(90)
                  ta.forward(20)

                  ta.begin_fill()
                  ta.left(90)
                  ta.forward(20)
                  ta.right(90)
                  ta.forward(20)
                  ta.right(90)
                  ta.forward(40)
                  ta.right(90)
                  ta.forward(20)
                  ta.right(90)
                  ta.forward(20)
                  ta.end_fill()

                  time.sleep(3)
                  fill.clear()




      def iarrow(i):
            t.fillcolor("yellow")

            ix=-650
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


      def box(boxi):
            global tay,iy
            v.speed(0)
            v.pensize(3)
            v.hideturtle()


            min=boxi
            global k,y,c,ct
            v.pencolor("black")
            v.fillcolor("pink")
            v.pensize(4)

            for j in range(5):
                  bx=x+(80*j)
                  v.penup()
                  v.goto(bx,y)
                  v.pendown()        
                  for i in range(2):
                        v.begin_fill()
                        v.forward(f)
                        v.right(90)
                        v.forward(f)
                        v.right(90)
                        v.end_fill()

            j=boxi+1
            n=len(arr)-1


            for o in range(5):

                  vb=n-o
                  if ct == vb :
                        c=True
                  tarrow(o,j)
                  t.clear()

                  tell.clear()
                  if j+1<len(arr):
                        j=j+1

                  ta.clear()

            iy=305-(150*k)

                  
            ct=ct+1

            y=y-150
            k=k+1
            tay=tay-150

      
      def fillvalues():
      #To fill values in array

            global c
            fil.pencolor("blaCk")

            if c==True:
                  c=False
                  # print("fill")
                  fil.speed(0)
                  fx=x+40
                  fil.hideturtle()
                  for i in range(5):
                        fil.penup()
                        fil.goto(fx,y-40)
                        fil.pendown()
                        fil.write(arr[i],font=("",12,"bold"))
                        fx=fx+80

            else:
                  # print("not fill")
                  fill.pencolor("blacK")
                  fill.speed(0)
                  fx=x+40
                  fill.hideturtle()
                  for i in range(5):
                        fill.penup()
                        fill.goto(fx,y-40)
                        fill.pendown()
                        fill.write(arr[i],font=("",12,"bold"))
                        fx=fx+80





      scale()
      writee()
      for i in range(len(arr)-1):
            min=i
            box(i)
            swi=swi+1


      done()

def sel():
      v=Turtle()
      fill=Turtle()
      fil=Turtle()
      t=Turtle()
      ta=Turtle()
      w=Turtle()
      tit=Turtle()
      tell=Turtle()
      s=Screen()

      s.bgcolor("Black")
      global k,swi,tay,f,c,x,ct,y,midarrow,arr,wy
      k=0
      swi=0
      tay=192
      f=80
      c=False

      x=-700
      ct=0
      y=300
      midarrow=0

      # arr=[60,40,12,42,67]

      # arr=[7,-1,-3,2,3]

      arr=[16,56,96,1,6]

      w.hideturtle()
      title=["S E L E C T I O N  S O R T "]
      w.pencolor("orange")
      w.penup()
      w.goto(40,310)
      w.pendown()

      w.write(title[0],font=("",15,"bold"))

      library=["int i,min,j,temp","int arr[]={77,21,93,20,3}","for (i=0 i<n-1;i++)","     min=i","     for(j=i+1;j<n;j++)","          if(arr[min]>arr[j])","            min=j",
      "     temp=arr[i]","     arr[i]=arr[min]","     arr[min]=temp" ]

      wy=250


      def writee():
            w.pencolor("White")

            w.hideturtle()
            w.pensize(3)
            global wy
            for i in range(len(library)):
                  w.penup()
                  w.goto(40,wy)
                  w.pendown()
                  w.write(library[i],font=("",18))
                  wy=wy-40


      def scale():
            tit.hideturtle()
            tit.goto(550,350)
            tit.pencolor("white")
            tit.pensize(3)
            tit.fillcolor("Green")

            tit.begin_fill()
            for i in range(4):
                  tit.forward(25)
                  tit.right(90)
            tit.end_fill()
            tit.penup()
            tit.goto(583,332)
            tit.pendown()
            tit.write("Swap Two Values",font=("",12))

            tit.penup()
            tit.goto(550,300)
            tit.pendown()
            tit.fillcolor("Red")
            tit.pencolor("white")
            tit.begin_fill()
            for i in range(4):
                  tit.forward(25)
                  tit.right(90)
            tit.end_fill()

            tit.penup()
            tit.goto(583,280)
            tit.pendown()
            tit.write("Don't Swap Values",font=("",12))    


      def tarrow(i,min,boxi,f):
            wtx=-600
            wty=345
            tell.pencolor("white")
            tell.hideturtle()
            tell.speed(0)
            tell.pensize(3)
            tell.penup()
            tell.goto(wtx,wty)
            tell.pendown()



            global midarrow,tay



            fillvalues()

            midarrow=80*i

            if arr[min]<arr[boxi]:
                  des="Smaller Than"
                  d="So Swap Them"
                  ta.fillcolor("Green")


            else:
                  des="Greater Than"
                  d="So Dont Swap Them" 
                  ta.fillcolor("Red")


            if arr[swi]>arr[f]:

                  s=f"{arr[f]} is {des} {arr[swi]} {d}"
                  tell.write(s,font=("",17,"bold"))

            else:

                  s=f"{arr[f]} is {des} {arr[swi]} {d}"
                  tell.write(s,font=("",17,"bold"))

            # print(arr[min],arr[boxi])




            if arr[min]<arr[boxi]:
            

                  tmp=arr[boxi]
                  arr[boxi]=arr[min]
                  arr[min]=tmp




            if i<(len(arr)-1)-swi:

                  tax=x+15+(80*swi)


                  ta.hideturtle()
                  ta.speed(0)
                  ta.penup()
                  ta.home()
                  ta.pendown()

                  ta.pensize(4)
                  ta.pencolor("white")
                  ta.penup()
                  ta.goto(tax,tay)
                  ta.pendown()


                  ta.begin_fill()
                  ta.forward(40)
                  ta.left(90)
                  ta.forward(20)
                  ta.left(90)
                  ta.forward(40)
                  ta.left(90)
                  ta.forward(20)
                  ta.end_fill()


                  ta.left(90)
                  ta.forward(20)
                  ta.right(90)
                  ta.forward(20)
                  ta.left(90)
                  ta.forward(80+midarrow)
                  ta.left(90)
                  ta.forward(20)

                  ta.begin_fill()
                  ta.left(90)
                  ta.forward(20)
                  ta.right(90)
                  ta.forward(20)
                  ta.right(90)
                  ta.forward(40)
                  ta.right(90)
                  ta.forward(20)
                  ta.right(90)
                  ta.forward(20)
                  ta.end_fill()

                  time.sleep(3)
                  fill.clear()




      def iarrow(i):
            # t.pencolor("yellow")
            t.fillcolor("yellow")

            ix=-650
            iy=305-(150*i)
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


      def box(boxi):
            global tay
            v.speed(0)
            v.pensize(3)
            v.hideturtle()


            min=boxi
            global k,y,c,ct
            v.pencolor("black")
            v.fillcolor("pink")
            v.pensize(4)
            for j in range(5):
                  bx=x+(80*j)
                  v.penup()
                  v.goto(bx,y)
                  v.pendown()        
                  for i in range(2):
                        v.begin_fill()
                        v.forward(f)
                        v.right(90)
                        v.forward(f)
                        v.right(90)
                        v.end_fill()

            iarrow(boxi)
            j=boxi+1
            n=len(arr)-1

            for o in range(5):
                  # print("iambefore updation",boxi,min,j)
                  if arr[min]>arr[j]:
                        min=j
                        # print("iamj",boxi,min,j)

                  vb=n-o
                  if ct == vb :
                        c=True
                  # print(arr[min],arr[boxi])
                  tarrow(o,min,boxi,j)
                  tell.clear()
                  if j+1<len(arr):
                        j=j+1

                  ta.clear()
                  
            ct=ct+1

            y=y-150
            k=k+1
            tay=tay-150
            t.clear()

      
      def fillvalues():
            global c
            fil.pencolor("blaCk")

            if c==True:
                  c=False
                  # print("fill")
                  fil.speed(0)
                  fil.showturtle()
                  fx=x+40
                  fil.hideturtle()
                  for i in range(5):
                        fil.penup()
                        fil.goto(fx,y-40)
                        fil.pendown()
                        fil.write(arr[i],font=("",12,"bold"))
                        fx=fx+80

            else:
                  # print("not fill")
                  fill.pencolor("blacK")
                  fill.speed(0)
                  fx=x+40
                  fill.hideturtle()
                  for i in range(5):
                        fill.penup()
                        fill.goto(fx,y-40)
                        fill.pendown()
                        fill.write(arr[i],font=("",12,"bold"))
                        fx=fx+80




      scale()
      writee()
      for i in range(len(arr)-1):
            min=i
            box(i)
            swi=swi+1


      done()

def insort():
      v=Turtle()
      fill=Turtle()
      fil=Turtle()
      t=Turtle()
      ta=Turtle()
      w=Turtle()
      tell=Turtle()
      s=Screen()
      nbx=Turtle()
      s.bgcolor("Black")

      global m,minOne,k,swi,tay,f,l,c,x,flag,ct,tmp,y,midarrow,nb,wy,arr
      m=1
      minOne=0
      k=0
      swi=0
      tay=192
      f=80
      l=0
      c=False
      x=-700
      flag=False
      ct=0
      tmp=True
      y=300
      midarrow=0
      nb=0

      # arr=[60,40,12,42,67]

      # arr=[7,-1,-3,2,3]

      arr=[56,16,80,1,6]
      # arr=[6,16,56,96,1]

      w.hideturtle()
      title=["I N S E R T I O N  S O R T "]
      w.pencolor("orange")
      w.penup()
      w.goto(40,310)
      w.pendown()

      w.write(title[0],font=("",15,"bold"))

      library=["int i,min,j,temp","int arr[]={77,21,93,20,3}","for (i=0 i<n-1;i++)","     min=i","     for(j=i+1;j<n;j++)","          if(arr[min]>arr[j])","            min=j",
      "     temp=arr[i]","     arr[i]=arr[min]","     arr[min]=temp" ]

      wy=250


      def writee():
            w.pencolor("White")

            w.hideturtle()
            w.pensize(3)
            global wy
            for i in range(len(library)):
                  w.penup()
                  w.goto(40,wy)
                  w.pendown()
                  w.write(library[i],font=("",18))
                  wy=wy-40





      def tarrow(i,min,boxi,f,minne):
            print(i,minne,swi)
            global minOne,flag,c

            if swi==0:
                  wtx=-720
                  wty=120
            else:
                  wtx=-680
                  wty=345

            # wtx=-600
            # wty=345

            tell.pencolor("white")
            tell.hideturtle()
            tell.speed(0)
            tell.pensize(3)
            tell.penup()
            tell.goto(wtx,wty)
            tell.pendown()



            global midarrow,tay,l

            if arr[minne]<val:
                  print(arr[minne],val)
                  c=True
                  ta.fillcolor("red")
            else:
                  c=False
                  ta.fillcolor("green")

            fillvalues()
            if minne==m-1:
                  midarrow=80
                  # print("midarrow 1",midarrow)

            else:
                  midarrow=80*((5-minne)-1)+100
                  # print("midarrow 2",midarrow)


            if arr[minne]>val:
                  des="Smaller Than"
                  d="So Move arr[i] To arr[i-1] Location"


            else:
                  des="Greater Than"
                  d="So Dont Perform Any Action" 


            # if arr[swi]>arr[f]:
            s=f"{val} is {des} {arr[minne]} {d}"
            tell.write(s,font=("",17,"bold"))

            # else:

            #     s=f"{arr[f]} is {des} {arr[swi]} {d}"
            #     tell.write(s,font=("",17,"bold"))




            # if i<swi+1:
            if True:

                  tax=x+15+(80*(swi-i))


                  ta.hideturtle()
                  ta.speed(0)
                  ta.penup()
                  ta.home()
                  ta.pendown()

                  ta.pensize(4)
                  ta.pencolor("white")
                  ta.penup()
                  ta.goto(tax,tay)
                  ta.pendown()


                  ta.begin_fill()
                  ta.forward(40)
                  ta.left(90)
                  ta.forward(20)
                  ta.left(90)
                  ta.forward(40)
                  ta.left(90)
                  ta.forward(20)
                  ta.end_fill()


                  ta.left(90)
                  ta.forward(20)
                  ta.right(90)
                  ta.forward(20)
                  ta.left(90)
                  ta.forward(midarrow)
                  ta.left(90)
                  ta.forward(20)

                  ta.begin_fill()
                  ta.left(90)
                  ta.forward(20)
                  ta.right(90)
                  ta.forward(20)
                  ta.right(90)
                  ta.forward(40)
                  ta.right(90)
                  ta.forward(20)
                  ta.right(90)
                  ta.forward(20)
                  ta.end_fill()

                  time.sleep(3)
                  fill.clear()

                  
                  if arr[minne]>val:

                        arr[minne+1]=arr[minne]
                        # arr[minne]=0
                        
                        fill.clear()
                        fillvalues()
                        # print(arr)
                        
                        time.sleep(2)

                        if minne==0:
                              arr[minne]=val
                        # if arr[minne-1]>arr[minne]:
                        if arr[minne-1]<val:
                              flag=True
                              arr[minne]=val
                              # l=l+1
                        
                        # print("If",arr)


                  else: 
                        pass
                        # if minne-1>=0:
                        #     if arr[minne]<val and arr[minne-1]>arr[minne]:
                        #         arr[minne+1]=val
                        #         flag=True
                        #         print("else",arr)

                  fill.clear()
                  # c=True
                  if i==swi:
                        c=True   
                  else:
                        c=False  

                  fillvalues()
                  # print(arr)
                  time.sleep(2)
      

      def xtrabox(tmpflag):
            nbx.hideturtle()
            if tmpflag==True:
                  nbx.penup()
                  nbx.goto(nb[0]+50,nb[1]+20)
                  nbx.pendown()
                  nbx.pencolor("orange")
                  nbx.write("Temporary Stored ",font=("",18,"bold"))

            nbx.penup()
            nbx.goto(nb[0]+100,nb[1])
            nbx.pencolor("white")

            nbx.pendown()
            nbx.fillcolor("Green")

            nbx.begin_fill()
            for i in range(2):
                  nbx.forward(f)
                  nbx.right(90)
                  nbx.forward(f)
                  nbx.right(90)
            nbx.end_fill()
            nbx.penup()
            nbx.goto(nb[0]+130,nb[1]-50)
            nbx.pendown()
            nbx.pencolor("black")
            nbx.write(arr[m],font=("",18,"bold"))



            nbx.penup()

      def iarrow(i):
            global minOne
            # t.pencolor("yellow")
            t.fillcolor("yellow")

            ix=-580
            iy=305-(150*i)
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


      def box(boxi,m):
            global tay,tmp,flag
            v.speed(0)
            v.pensize(3)
            v.hideturtle()


            min=boxi
            global k,y,c,ct,nb
            v.pencolor("black")
            v.fillcolor("pink")
            v.pensize(4)
            for j in range(5):
                  bx=x+(80*j)
                  v.penup()
                  v.goto(bx,y)
                  v.pendown()        
                  for i in range(2):
                        v.begin_fill()
                        v.forward(f)
                        v.right(90)
                        v.forward(f)
                        v.right(90)
                        v.end_fill()
            
            nb=v.position()
            xtrabox(tmp)
            tmp=False

            iarrow(boxi)
            j=boxi+1
            n=len(arr)-1
            minOne=m-1

            l=swi
            for o in range(0,swi+1):
                  # print(minOne,m,swi)
                  vb=swi-o
                  tarrow(o,min,boxi,j,minOne)
                  if arr[minOne]<val:
                        ta.clear()
                        tell.clear()
                        break
                  # else:
                  #     c=False
                  # if ct == vb :
                  #     c=True
                  tell.clear()
                  ta.clear()
                  minOne=minOne-1
                  l=l+1
                  tell.clear() 
                  if flag==True:
                        flag=False
                        break               


            ct=ct+1

            y=y-150
            k=k+1
            tay=tay-150
            t.clear()

      
      def fillvalues():
            global c
            fil.pencolor("blaCk")

            if c==True:
                  c=False
                  # print("fill")
                  fil.speed(0)
                  fil.showturtle()
                  fx=x+40
                  fil.hideturtle()
                  for i in range(5):
                        fil.penup()
                        fil.goto(fx,y-40)
                        fil.pendown()
                        fil.write(arr[i],font=("",12,"bold"))
                        fx=fx+80

            else:
                  # print("not fill")
                  fill.pencolor("blacK")
                  fill.speed(0)
                  fx=x+40
                  fill.hideturtle()
                  for i in range(5):
                        fill.penup()
                        fill.goto(fx,y-40)
                        fill.pendown()
                        fill.write(arr[i],font=("",12,"bold"))
                        fx=fx+80


      writee()
      for i in range(len(arr)-1):
            # print(m)
            val=arr[m]
            box(i,m)
            swi=swi+1
            m=m+1

      done()      

# insort()