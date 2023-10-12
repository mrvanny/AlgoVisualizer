import mysql.connector
import re
import customtkinter

# from customtk import dbflg





def echeck(email,username,psw,cpsw):
    
    global pswmatch,eml,fe,fu,fp,fcp,fflag


    eml,pswmatch=False,False
    fe,fu,fp,fcp=True,True,True,True

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if len(email)==0:
        fe=False
        #print("Enter email id first")

    if len(username)==0:
        fu=False
        #print("Enter email id first")

    if len(psw)==0:
        fp=False
        #print("Enter email id first")

    if len(cpsw)==0:
        fcp=False
        #print("Enter email id first")



    if(re.fullmatch(regex, email)):
        eml=True  
        # print("Valid Email")
    else:
        eml=False 
        # print("Invalid Email")

    if psw==cpsw:
        pswmatch=True
    else:
        pswmatch=False   

    
    if eml==True and pswmatch==True:
        fflag=True
    else:
        fflag=False

    print("I am final flag broo",fflag)

    return fflag




def dbupdate(email,username,psw,cpsw,app):

    v=False
    v=echeck(email,username,psw,cpsw)
    print("insertion:",v)

    if v==True:

        db=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="vbonIg@44",
            database="vb"
        )

        mc=db.cursor()

        # print(email,username,psw)

        
        qry="Insert INTO lvalid() VALUES (%s, %s, %s)"
        dt=(username,psw,email)

        mc.execute(qry,dt)

        db.commit()


    fcheck(app)
    






def check(e,e2,dbflg):
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="vbonIg@44",
    database="vb"
    )

    mycursor = mydb.cursor()

    sflag=False

    # u='ggboiss'
    # p='tuteradekh$01'

    # # sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    # # val = [
    # #   (u,p)
    # # ]

    
    #sql= "SELECT * FROM lvalid WHERE username= '%s' and pass='%s' " %(e,e2)

    sql="SELECT * FROM lvalid where username='%s' and passwords='%s' " %(e,e2)

    # sql="SELECT * FROM lvalid"

    mycursor.execute(sql)

    # mydb.commit() // for modifying value in db

    c=mycursor.fetchall()

    k=[]

    loc=0


    for i in c:
        print(i)
        k=i


    # print(k[0],k[1])


    # if e!=k[0] and e2==k[1]:
    #     print("Wrong username ")

    # if e==k[0] and e2!=k[1]:
    #     print("Wrong Password ")



    try:
        if e==k[0] and e2==k[1]:
            print("Successfully login ")
            sflag=True
            
    except IndexError:

            print("Wrong credentials")
            sflag=False






    return sflag

bg=False

def dstoy():
    lf.destroy()
    if bg==True:   
        lfbg.destroy()



def fcheck(app):

    global dlf,lf,bg,lfbg,fflag
    t=True
    lf=customtkinter.CTkFrame(master=app, width=250, height=80,fg_color='white',corner_radius=5)
    lf.place(relx=0.4, rely=0.65)


    if fe and fu and fp and fcp:



        if t==True:
            ccos=customtkinter.CTkButton(lf, width=50,height=12, text="X", command=dstoy, corner_radius=6,fg_color='black',text_color='red',hover_color="#2F0F5D")
            ccos.place(x=200,y=3)            

        if pswmatch==False:
            nt=customtkinter.CTkLabel(lf,text='Sorry Password doent matched',text_color='black',font=('Century Gothic',15,'bold'))
            nt.place(x=10,y=20)
            #print("Password matched")



            #print("Pass Doent match")


        if eml==False :
            nt=customtkinter.CTkLabel(lf,text='Invalid Email',text_color='black',font=('Century Gothic',15,'bold'))
            nt.place(x=10,y=40)
            #print("Password matched")



        if fflag==True:
            nt=customtkinter.CTkLabel(lf,text='Congratulations Buddy !!!',text_color='black',font=('Century Gothic',15,'bold'))
            nt.place(x=10,y=20)            
            nt=customtkinter.CTkLabel(lf,text='You Registered SuccessfullY ',text_color='black',font=('Century Gothic',15,'bold'))
            nt.place(x=9,y=40)            



        

        dlf=False

    else:


        if t==True:
            ccos=customtkinter.CTkButton(lf, width=50,height=12, text="X", command=dstoy, corner_radius=6,fg_color='black',text_color='red',hover_color="#2F0F5D")
            ccos.place(x=200,y=3)

        if (fp==False):
            print("empyt huu")
            nt=customtkinter.CTkLabel(lf,text='Hey dude fill Password fied first  ',text_color='black',font=('Century Gothic',15,'bold'))
            nt.place(x=10,y=20)
        if (fe==False):
            print("Email not filled")
            nt=customtkinter.CTkLabel(lf,text='Hey dude enter Email Id First  ',text_color='black',font=('Century Gothic',15,'bold'))
            nt.place(x=10,y=40)            



    # else:
    #     dlf=True
    #     lf.destroy()


 
    