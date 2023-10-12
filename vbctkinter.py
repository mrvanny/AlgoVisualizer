#importing required modules
import tkinter
import turtle
import time 
from sql import *
from searching2 import *
import time
from linkedlist2 import *
import re
from arrayfl import *
from  sorting2 import *
from queue2 import *
from stack2 import *
import customtkinter
from PIL import ImageTk,Image
import mysql.connector


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
# customtkinter.set

flag=False
fflag=False
rvala=False
ynflag=False
w=0

dbflg=False

# dbflg=True

a=True
app = customtkinter.CTk()  #creating cutstom tkinter window
app.geometry("1400x1400")
app.title('Algorithm Visualizer')

ctr=1
dlf=True
vl=False

def fm(f):
    global vl
    if f==True:
        print(vl)
        global dlf,lfm
        lfm=customtkinter.CTkFrame(master=app, width=800, height=40,fg_color='white',corner_radius=5)
        lfm.place(relx=0.3, rely=0.1)
        vl=True
        nt=customtkinter.CTkLabel(lfm,text='Please Login First',text_color='black',font=('Century Gothic',22,'bold'))
        nt.place(x=300,y=10)
        dlf=False
    
    else:
        dlf=True
        lfm.destroy()

    # time.sleep(0.4)
    # lf.destroy()

def fhome():
    global dlf,lf,dbflg

    if dbflg==False:
        fm(dlf)

    # if dlf==True:
    #     print(dlf)
    #     lf.destroy()    

def fabtus():
    if dbflg==False:
        fm(dlf)

def fads():
    if dbflg==False:
        fm(dlf)

def fdoc():
    if dbflg==False:
        fm(dlf)

def fmenu():
    if dbflg==False:
        fm(dlf)
    if dbflg==True:
        upd()

def fcwu():
    if dbflg==False:
        fm(dlf)

def fnote():
    if dbflg==False:
        fm(dlf)

def tr():
    print('hii')

def dslogin():
    if len(entry1.get())>0 and len(entry2.get())>0: 
        frame.destroy()

def lvalid():
    # print(entry1.get())
    # print(entry2.get())
    global dbflg
    ddbbflg = check(entry1.get(),entry2.get(),dbflg)
    dbflg=ddbbflg

    if dbflg == True:
        dslogin()

    
def abtdst():
    global ctr
    lff.destroy()
    ctrr=0


def dn():
    global nf,ctr
    nf.destroy()
    ctrrr=0


ctrrr=0

def notes():

        if dbflg==False:
            fm(dlf)

        if dbflg==True:
            global nf,ctrrr
            if ctrrr==0:
                nf=customtkinter.CTkFrame(master=app, width=600, height=400,fg_color='#F0A500',corner_radius=5)
                nf.place(relx=0.5, rely=0.1)
                k=0
                ctrrr=2

                nt=customtkinter.CTkLabel(nf,text='Write down your notes here: ',text_color='#03002C',font=('Century Gothic',25,'bold'))
                nt.place(x=20,y=20)

                n=customtkinter.CTkEntry(nf,width=520, height=50, placeholder_text="Topic Name :",corner_radius=8,fg_color='black')
                n.place(x=20,y=60)

                k=customtkinter.CTkTextbox(nf,width=560,height=250, corner_radius=8,fg_color='#323232')
                k.place(x=20,y=130)
                        
                crbutton = customtkinter.CTkButton(nf, width=50,height=30, text="X", command=dn, corner_radius=6,fg_color='black',text_color='red',hover_color='#43D8C9',font=('Century Gothic',26,'bold'))
                crbutton.place(x=530, y=13)





ctrr=0

def aboutus():
        global dlf,lff,ctrr

        if dbflg==False:
            fm(dlf)
        if dbflg==True:
            if ctrr == 0:
                lff=customtkinter.CTkFrame(master=app, width=1150, height=600,fg_color='white',corner_radius=30)
                lff.place(relx=0.15, rely=0.2)
                k=0
                ctrr=2

                arr=[ 'Welcome to our app!    ',

        'Our mission is to provide our users with an easy-to-use platform that aids in simplifying their lives.','Whether you’re needing assistance with organization, meeting new people, or staying up-to-date with current events','our app has something for you , Our platform was developed with the user in mind. We recognize the importance of ','privacy and security and have implemented measures to ensure your information is protected. We are dedicated to',' continually improving  our app to meet the , ever-evolving needs of our users. Our team is made up of passionate individuals  ','who strive to create a better user experience with every update. Our developers are continuously enhancing the app’s ', 'functionality while our customer service team ensures that users receive the support they need. We want to thank you for' ,' choosing our app and hope that it makes your life a little easier. If you, have any questions or suggestions, we encourage','you to reach out to our customer service team, who would be happy to help.',

        'Thank you for being a part of our journey.']
                k=90                
                for i in range(50):
                        ntt=customtkinter.CTkLabel(lff,text='^',text_color='black',font=('Century Gothic',30,'bold'))
                        ntt.place(x=0,y=k)
                        k=k+10


                k=90                
                for i in range(50):
                        ntt=customtkinter.CTkLabel(lff,text='^',text_color='black',font=('Century Gothic',30,'bold'))
                        ntt.place(x=1130,y=k)
                        k=k+10


                nt=customtkinter.CTkLabel(lff,text='_______________________________________________________________________',text_color='black',font=('Century Gothic',40,'bold'),corner_radius=10)
                nt.place(x=0,y=0)

                nt=customtkinter.CTkLabel(lff,text='_______________________________________________________________________',text_color='black',font=('Century Gothic',85,'italic','bold'))
                nt.place(x=1,y=500)

                crbutton = customtkinter.CTkButton(master=lff, width=70,height=50, text="X", command=abtdst, corner_radius=6,fg_color='black',text_color='red',hover_color='purple',font=('Century Gothic',26,'bold'))
                crbutton.place(x=1070, y=13)

                k=0
                for i in range(11):
                    if i==0:
                        nt=customtkinter.CTkButton(lff,width=70,height=40,text=arr[i], command=abtdst,text_color='Red',font=('comic sans ms',35,'italic','bold'),fg_color='black',corner_radius=10,hover_color='black')
                        nt.place(x=30,y=16+k)
                        k=k+40
                        i=i+1

                    if i==10:
                        nt=customtkinter.CTkLabel(lff,text=arr[i],text_color='#951555',font=('Verdana',25,'bold'))
                        nt.place(x=135,y=70+k)
                        k=k+40  

                    else:
                        nt=customtkinter.CTkLabel(lff,text=arr[i],text_color='#0B032D',font=('comic sans ms',18,'bold'))
                        nt.place(x=25,y=50+k)
                        k=k+40                


def sorting(sort:str):

    if sort=='Quick sort':
        quicksort()
    if sort=='Insertion sort':
        insort()
    if sort=='Bubble sort':
        # bubblesort()
        bub()
    if sort=='Radix sort':
        radixsort()
    if sort=='Selection sort':
        # selectionsort()
        sel()

    if sort=='Count sort':
        countsort()
    if sort=='Shell sort':
        shellsort()



def linkedlist(ll:str):
    if ll=='Insertion at Beginning':
        insbeg()
    if ll=='Insertion at End':
        insend()
    if ll=='Insertion in Between':
        insbetn()
    if ll=='Deletion at Beginning':
        delbeg()
    if ll=='Deletion at End':
        delend()

    # if ll=='Deletion in Between':
    #     dbetween()
    # if ll=='Access Linked List':
    #     laccess()

def searching(search:str):
    if search=='Linear search':
        linsearch()
    if search=='Binary search':
        Binsearch()


def array(a:str):
    if a=='Deletion in Array':
        adel()
    if a=='Insertion in Array':
        ains()
    if a=='Array Create':
        ac()


def stack(opt:str):
    if opt=='Push':
        pushitm()
    if opt=='Pop':
        popitm()
        # pop()

def queue(oper:str):
    if oper=='Enqueue':
        enq()
    if oper=='Dequeue':
        deq()



def button_function():
    app.destroy()            # destroy current window and creating new one 
    w = customtkinter.CTk()  
    w.geometry("1280x720")
    w.title('Welcome')


    l1=customtkinter.CTkLabel(master=w, text="Home Page",font=('Century Gothic',60))
    l1.place(relx=0.5, rely=0.5,  anchor=tkinter.CENTER)


    w.mainloop()
    


def fbutton_function():
    app.destroy()            # destroy current window and creating new one 
    w = customtkinter.CTk()  
    w.geometry("1280x720")
    w.title('Forget ')
    l1=customtkinter.CTkLabel(master=w, text="Forget wali window",font=('Century Gothic',60))
    l1.place(relx=0.5, rely=0.5,  anchor=tkinter.CENTER)
    w.mainloop()
    



def dele():
    frame.destroy()
    login()
    #rframe.destroy()


# def tdel():
#     global frame,rframe
#     frame.destroy()
#     rframe.destroy()  

def upd():
    global flag,w,sd

    if(flag==False):

        flag=True

        w=170
        sd=customtkinter.CTkFrame(master=app, width=w, height=860,fg_color='#0B2447')
        sd.place(relx=0, rely=0.5, anchor=tkinter.W)

        lb=customtkinter.CTkLabel(master=sd,text="Data",font=("Century Gothic",36,"bold"))
        lb.place(x=30,y=50)

        lb2=customtkinter.CTkLabel(master=sd,text="Structure",font=('Century Gothic',35,'bold'))
        lb2.place(x=10,y=90)


        opt=customtkinter.CTkOptionMenu(master=sd,values=["Searching","Linear search","Binary search"],height=40,text_color='black', command=searching,fg_color='red',font=('Century Gothic',22,'bold'))
        opt.place(x=00,y=180)




        opt4=customtkinter.CTkOptionMenu(master=sd,values=["Enqueue","Dequeue"],height=40,text_color='black', command=queue,font=('Century Gothic',22,'bold'),corner_radius=6)
        #opt4.grid(row=4, column=0, padx=0, pady=10)
        opt4.place(x=00,y=260)
        opt4.set("Queue")


        # opt2=customtkinter.CTkOptionMenu(master=sd,values=["Array Create","Insertion in Array","Deletion in Array"],height=40,text_color='black', command=array,font=('Century Gothic',22,'bold'),corner_radius=6)
        # opt2.place(x=00,y=340)
        # opt2.set("Array")

        opt=customtkinter.CTkOptionMenu(master=sd,values=["Bubble sort","Insertion sort","Selection sort",],height=40,command=sorting, font=('Century Gothic',22,'bold'))
        opt.place(x=00,y=420)
        opt.set("Sorting")

        opt=customtkinter.CTkOptionMenu(master=sd,values=["Push","Pop"],height=40,text_color='black', command=stack ,fg_color='orange',font=('Century Gothic',22,'bold'))
        opt.place(x=00,y=500)
        opt.set("Stack")

        opt=customtkinter.CTkOptionMenu(master=sd,values=["Access Linked List","Insertion at Beginning","Insertion at End","Insertion in Between","Deletion at Beginning","Deletion at End"],height=40,text_color='black', command=linkedlist ,fg_color='orange',font=('Century Gothic',22,'bold'))
        opt.place(x=00,y=340)
        opt.set("Linked List")

        p=customtkinter.CTkLabel(master=sd, text="--The SNV Product",font=('Century Gothic',15,'bold'),text_color='White')
        p.place(x=0,y=700)




    else :
        print("In Another stream:",w)        
        w=0
        flag=False
        sd.destroy()

def rdest():
    rframe.destroy()




def dbupd():
 
    # fflag=echeck(reml.get() ,ru.get(),rp.get(),l4.get())

    fflag= dbupdate(reml.get() ,ru.get(),rp.get(),l4.get(),app)
    rdest()    

    if fflag==True:
        print("Registered successfully")

    if fflag==False:
        fcheck(app)        
        #print("invalllid data entry")
    




def dsttoy():
    global cs
    cs.destroy()

def ldsttoy():
    global lcs
    lcs.destroy()

lflag=False


def congl(lg):
    global dlf,cs,bg,lfbg,lcs,ynflag
    t=True
    ynflag=True
    
    # if lflag==True:
    #     alt=''
    # if lflag==False:
    #     alt=


    if dbflg==True:
        cs=customtkinter.CTkFrame(master=app, width=400, height=40,fg_color='white',corner_radius=5)
        cs.place(relx=0.4, rely=0.1)

        if t==True:
            ccos=customtkinter.CTkButton(cs, width=35,height=12, text="X", command=dsttoy, corner_radius=6,fg_color='black',text_color='yellow',hover_color="red",font=('Century Gothic',14,'bold'))
            ccos.place(x=350,y=3)

        nt=customtkinter.CTkLabel(cs,text='Congratulations Bro... Login Successfull',text_color='black',font=('Century Gothic',15,'bold'))
        nt.place(x=10,y=10)    

    if dbflg==False:
        lcs=customtkinter.CTkFrame(master=app, width=400, height=40,fg_color='white',corner_radius=5)
        lcs.place(relx=0.4, rely=0.1)

        if t==True:
            ccos=customtkinter.CTkButton(lcs, width=35,height=12, text="X", command=ldsttoy, corner_radius=6,fg_color='black',text_color='yellow',hover_color="red",font=('Century Gothic',14,'bold'))
            ccos.place(x=350,y=3)

        nt=customtkinter.CTkLabel(lcs,text='Invalid Credentials Dude',text_color='black',font=('Century Gothic',15,'bold'))
        nt.place(x=10,y=10)    



def rgst():
    # global frame
    # frame.destroy()
    frame.destroy()
    global rframe,ctr,reml,ru,rp,l4,entry1,entry2,rvala

    # ctr=1
    rframe=customtkinter.CTkFrame(master=app, width=520, height=560, corner_radius=50,fg_color='#D3DBFF')
    rframe.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2=customtkinter.CTkLabel(master=rframe, text="Register With US",font=('Century Gothic',35,'bold'),text_color='black')
    l2.place(x=90, y=45)

    le=customtkinter.CTkLabel(master=rframe,text='Email Id here:',text_color='Black',font=('Century Gothic',17,'bold'))
    le.place(x=70, y=110)

    reml=customtkinter.CTkEntry(master=rframe, width=220,height=30, placeholder_text='Enter Email Id')
    reml.place(x=230, y=110)



    le=customtkinter.CTkLabel(master=rframe,text='Username here:',text_color='Black',font=('Century Gothic',17,'bold'))
    le.place(x=70, y=155)

    ru=customtkinter.CTkEntry(master=rframe, width=220, placeholder_text='Enter Username')
    ru.place(x=230, y=155)


    le=customtkinter.CTkLabel(master=rframe,text='New Password here:',text_color='Black',font=('Century Gothic',17,'bold'))
    le.place(x=70, y=200)

    rp=customtkinter.CTkEntry(master=rframe, width=220, height=30, placeholder_text="Create password",show="*")
    rp.place(x=230,y=200)


    le=customtkinter.CTkLabel(master=rframe,text='Confirm Password:',text_color='Black',font=('Century Gothic',17,'bold'))
    le.place(x=70, y=250)

    l4=customtkinter.CTkEntry(master=rframe, width=220, height=30, placeholder_text="Confirm password")
    l4.place(x=230,y=250)

        #Create custom button
    button1 = customtkinter.CTkButton(master=rframe, width=120, text="Let's Begin", command=dbupd, corner_radius=6,fg_color='orange',text_color='black',font=('Century Gothic',18,'bold'))
    button1.place(x=170, y=305)
        

    le=customtkinter.CTkLabel(master=rframe,text='Already Have Account?',text_color='Black',font=('Century Gothic',17,'bold'))
    le.place(x=70, y=355)

    rvala=True
    lbutton1 = customtkinter.CTkButton(master=rframe, width=180, text="Login", command=login, corner_radius=6,fg_color='orange',text_color='black',font=('Century Gothic',18,'bold'))
    lbutton1.place(x=270, y=355)

    crbutton = customtkinter.CTkButton(master=rframe, width=70,height=40, text="X", command=rdest, corner_radius=6,fg_color='black',text_color='red',hover_color='yellow',font=('Century Gothic',22,'bold'))
    crbutton.place(x=430, y=10)
    
    ctr=1


def clogin():
    global dbflg

    lflag=check(entry1.get(),entry2.get(),dbflg)
    #print("login:",lflag)
    if lflag==True:
        dbflg=True
        frame.destroy()
        congl(lflag)
    else :
        congl(lflag)



def login():

    # #creating custom frame
    global ctr,frame,lflag
    global entry1,entry2,rvala

    # if vl==True:
    #     lf.destroy()

    if rvala==True:
        frame.destroy()

        rvala=False

    if vl==True:
        print(vl)
        global lfm
        lfm.destroy()


    if ctr==1:
        frame=customtkinter.CTkFrame(master=app, width=520, height=560, corner_radius=50,fg_color='#D0E8F2')
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        l2=customtkinter.CTkLabel(master=frame, text="Welcome Back",font=('Century Gothic',35,'bold'),text_color='black')
        l2.place(x=90, y=45)

        le=customtkinter.CTkLabel(master=frame,text='Username Here:',text_color='Black',font=('Century Gothic',17,'bold'))
        le.place(x=70, y=110)

        entry1=customtkinter.CTkEntry(master=frame, width=220,height=35,placeholder_text='Please Enter Username',fg_color="#191825")
        entry1.place(x=210, y=110)

        # entry1=customtkinter.CTkEntry(master=frame, width=220,height=35,placeholder_text='Enter Username')
        # entry1.place(x=110, y=110)


        le2=customtkinter.CTkLabel(master=frame,text='Password Here:',text_color='Black',font=('Century Gothic',17,'bold'))
        le2.place(x=80, y=165)

        entry2=customtkinter.CTkEntry(master=frame, width=220, height=35, placeholder_text='Please Enter Password', show="*",fg_color="#191825")
        entry2.place(x=210, y=165)



        l3=customtkinter.CTkButton(master=frame, width=220, height=30,text="Forget password?",command=button_function,font=('Century Gothic',17,'bold'),fg_color="#000000",text_color='red')
        l3.place(x=120,y=260)

        #Create custom button
        button1 = customtkinter.CTkButton(master=frame, width=120, height=40, text="Login", command=clogin, corner_radius=6,fg_color="#000000",text_color='pink' ,font=('Century Gothic',20,'bold'))
        button1.place(x=160, y=310)

        # img2=customtkinter.CTkImage(Image.open("Google__G__Logo.svg.webp").resize((20,20), Image.ANTIALIAS))
        # img3=customtkinter.CTkImage(Image.open("124010.png").resize((20,20), Image.ANTIALIAS))

        # button2= customtkinter.CTkButton(master=frame, image=img2, text="Google", width=100, height=40, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
        # button2.place(x=130, y=290)

        # button3= customtkinter.CTkButton(master=frame, image=img3, text="Facebook", width=100, height=40, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
        # button3.place(x=240, y=290)

        # crbutton= customtkinter.CTkButton(master=frame, text="X",width=50, height=40, fg_color='red', text_color='black')
        # crbutton3.place(x=340, y=30)

        crbutton1 = customtkinter.CTkButton(master=frame, width=70,height=40, text="X", command=dele, corner_radius=6,fg_color='black',text_color='red',hover_color='yellow',font=('Century Gothic',22,'bold'))
        crbutton1.place(x=430, y=10)


        lbl= customtkinter.CTkLabel(master=frame, text="Dont have Account?",font=('Century Gothic',17,'bold','italic'),text_color='black')
        lbl.place(x=150,y=400)


        button4= customtkinter.CTkButton(master=frame,text="Create Acoount", width=120, height=40, compound="left", fg_color='black', text_color='yellow', hover_color='#AFAFAF',command=rgst,font=('Century Gothic',20,'bold'))
        button4.place(x=160, y=440)

        ctr=2

    else:
        ctr=ctr-1
        # frame.destroy()
        # rframe.destroy()    






img1=ImageTk.PhotoImage(Image.open("dsa4.png"))
l1=customtkinter.CTkLabel(master=app,image=img1)
l1.pack()

# customtkinter.CTkButton()

hbtn = customtkinter.CTkButton(app,width=220,height=40,text="Home",command=fhome,corner_radius=7,hover_color='red',font=('Century Gothic',22,'bold'))
hbtn.place(x=180,y=20)

dbtn = customtkinter.CTkButton(app,width=220,height=40,text="Documentations",command=fdoc,corner_radius=7,hover_color='red',font=('Century Gothic',22,'bold'))
dbtn.place(x=405,y=20)

abtn = customtkinter.CTkButton(app,width=220,height=40,text="About Us",command=aboutus,corner_radius=7,hover_color='red',font=('Century Gothic',22,'bold'))
abtn.place(x=630,y=20)

cbtn = customtkinter.CTkButton(app,width=220,height=40,text="Connect With Us",command=fcwu,corner_radius=7,hover_color='red',font=('Century Gothic',22,'bold'))
cbtn.place(x=855,y=20)

b=customtkinter.CTkButton(app,width=70,height=40,text='☰',command=fmenu,corner_radius=7,hover_color='red',font=('Century Gothic',22,'bold'))
b.place(x=150,y=20)

lbtn = customtkinter.CTkButton(app,width=220,height=40,text="Notes",command=notes,corner_radius=7,hover_color='red',font=('Century Gothic',22,'bold'))
lbtn.place(x=1080,y=20)

lbtn = customtkinter.CTkButton(app,width=180,height=50,text="Login",text_color='black',command=login,corner_radius=4,hover_color='purple',fg_color="yellow",font=('Century Gothic',22,'bold'))
lbtn.place(x=1320,y=16)



app.mainloop()
