from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import os



class login:
    def __init__(self,root):

        self.root = root
        self.root.title("LOGIN | CGPA Calculator")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)
        self.bg = ImageTk.PhotoImage(file="images/login2.jpg")
        self.bg_image = Label(self.root,image=self.bg).place(x=0,y=0,relwidth= 1, relheight= 1)


    def login_form(self):

        global username_verify
        global regpassword_verify
        username_verify = StringVar()
        regpassword_verify = StringVar()


        Frame_Login=Frame(self.root,bg="white")
        Frame_Login.place(x=150,y=150,height=340,width=500)

        title=Label(Frame_Login,text="Login Here",font=("impact",35,"bold"),fg="#000000",bg="white").place(x=90,y=30)
        desc=Label(Frame_Login,text="Student Login Here",font=("Goudy old style",15,"bold"),fg="#eb0505",bg="white").place(x=90,y=100)

        lbl_user=Label(Frame_Login,text="Username", font=("Goudy old style",12,"bold"),fg="gray",bg="white").place(x=90,y=140)
        self.txt_user=Entry(Frame_Login,textvariable = username_verify,font = ("times new roman",12),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)

        lbl_pass=Label(Frame_Login,text="Password",font=("Goudy old style",12,"bold"),fg="gray",bg="white").place(x=90,y=210)
        self.txt_pass=Entry(Frame_Login,textvariable = regpassword_verify,font = ("times new roman",12),bg="lightgray")
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        lbl_register=Button(self.root,command=self.register_data,cursor="hand2",bd=0,text="New? Register here",font=("Goudy old style",10,"bold"),fg="red",bg="white").place(x=450,y=430)
        


        Login_btn=Button(self.root,command=self.login_verify,cursor="hand2",text="Login",fg="white",bg="#eb0505",font=("times new roman",20)).place(x=300,y=470,width=180,height=40)


    def login_verify(self):
        username1 = username_verify.get()
        password1 = regpassword_verify.get()

        if username_verify.get() =="" or regpassword_verify.get()=="":
            messagebox.showerror("Entry Error","All Fields are Required",parent=self.root)
        
        else:
            filelist = os.listdir()
            if username1 in filelist:
                file1 = open(username1,"r")
                verify = file1.read().splitlines()
                if password1 in verify:
                    self.cgpacalculator()
                else:
                    messagebox.showerror("Password Error","The password you entered doesnt match our records",parent=self.root)

            else:
                messagebox.showerror("User Error","It seems like you entered wrong username",parent=self.root)
                

    def register_user(self):
        self.username_info = username.get()
        self.password_info = regpassword.get()

        file = open(self.username_info, "w")
        file.write(self.username_info+"\n")
        file.write(self.password_info)
        file.close()

        self.user_entry.delete(0,END)
        self.pass_entry.delete(0,END)

        messagebox.showinfo("Registration Success!","Now you can try logging in",parent=self.root)        


    def register_data(self):
        screen1 = Toplevel(root)
        screen1.title("REGISTER | CGPA CALCULATOR")
        screen1.geometry("700x600+500+70")
        screen1.resizable(False,False)
        screen1.bg = ImageTk.PhotoImage(file="images/login1.jpg")
        screen1.bg_image = Label(screen1,image=screen1.bg).place(x=0,y=0,relwidth= 1, relheight= 1)

        Frame_Login=Frame(screen1,bg="white")
        Frame_Login.place(x=150,y=150,height=340,width=500)
        title=Label(Frame_Login,text="Register Here",font=("impact",35,"bold"),fg="#000000",bg="white").place(x=90,y=30)
        desc=Label(Frame_Login,text="Student Registration Form",font=("Goudy old style",15,"bold"),fg="#0895d1",bg="white").place(x=90,y=100)
        lbl_user=Label(Frame_Login,text="Create a Username",font=("Goudy old style",12,"bold"),fg="gray",bg="white").place(x=90,y=140)
        
        global username
        global regpassword


        username = StringVar()
        regpassword = StringVar()
        self.user_entry=Entry(Frame_Login,textvariable = username,font = ("times new roman",12),bg="lightgray")
        self.user_entry.place(x=90,y=170,width=350,height=35)
        lbl_pass=Label(Frame_Login,text="Enter a Password",font=("Goudy old style",12,"bold"),fg="gray",bg="white").place(x=90,y=210)
        self.pass_entry=Entry(Frame_Login,textvariable= regpassword,font = ("times new roman",12),bg="lightgray")
        self.pass_entry.place(x=90,y=240,width=350,height=35)
        regn_btn=Button(screen1,cursor="hand2",text="Register",fg="white",bg="#0895d1",command = self.register_user,font=("times new roman",20)).place(x=300,y=470,width=180,height=40)
      
    

    def cgpacalculator(self):
        global screen
        screen = Toplevel(root)
        screen.title("CGPA CALCULATOR")
        screen.geometry("1000x800+500+70")
        screen.resizable(False,False)

        heading = Label(screen,text = "CGPA CALCULATOR", fg = "black", bg="grey",font=(20), width = "500", height= "3").pack()

        Label(screen,text = "First Semester",fg='white',font=(10), bg = "black",width = '500', height='2').pack()
        global Sem
        Sem=Frame(screen,bg="white")
        Sem.place(x=10,y=150,height=340,width=980)
        sub1 = Label(Sem, text = "Enter Subject 1 grade: ",font=("Goudy old style",12,"bold"),fg="gray",bg="white").place(x=12,y=30)
        sub2 = Label(Sem, text = "Enter Subject 2 grade: ",font=("Goudy old style",12,"bold"),fg="gray",bg="white").place(x=12,y=70)
        sub3 = Label(Sem, text = "Enter Subject 3 grade: ",font=("Goudy old style",12,"bold"),fg="gray",bg="white").place(x=12,y=110)
        sub4 = Label(Sem, text = "Enter Subject 4 grade: ",font=("Goudy old style",12,"bold"),fg="gray",bg="white").place(x=12,y=150)
        sub5 = Label(Sem, text = "Enter Subject 5 grade: ",font=("Goudy old style",12,"bold"),fg="gray",bg="white").place(x=12,y=190)   

        global grade1
        global grade2
        global grade3
        global grade4
        global grade5
        grade1=StringVar()
        grade2=StringVar()
        grade3=StringVar()
        grade4=StringVar()
        grade5=StringVar()
        Entry(Sem, textvariable = grade1,font=("Goudy old style",12,"bold"),bg="lightgray").place(x=210,y=30)   
        Entry(Sem, textvariable = grade2,font=("Goudy old style",12,"bold"),bg="lightgray").place(x=210,y=70) 
        Entry(Sem, textvariable = grade3,font=("Goudy old style",12,"bold"),bg="lightgray").place(x=210,y=110) 
        Entry(Sem, textvariable = grade4,font=("Goudy old style",12,"bold"),bg="lightgray").place(x=210,y=150)  
        Entry(Sem, textvariable = grade5,font=("Goudy old style",12,"bold"),bg="lightgray").place(x=210,y=190)  

        global credit1
        global credit2
        global credit3
        global credit4
        global credit5
        cred1 = Label(Sem, text = "Enter Subject 1 credit: ",font=("Goudy old style",12,"bold"),fg="gray",bg="white").place(x=500,y=30)
        cred2 = Label(Sem, text = "Enter Subject 2 credit: ",font=("Goudy old style",12,"bold"),fg="gray",bg="white").place(x=500,y=70)
        cred3 = Label(Sem, text = "Enter Subject 3 credit: ",font=("Goudy old style",12,"bold"),fg="gray",bg="white").place(x=500,y=110)
        cred4 = Label(Sem, text = "Enter Subject 4 credit: ",font=("Goudy old style",12,"bold"),fg="gray",bg="white").place(x=500,y=150)
        cred5 = Label(Sem, text = "Enter Subject 5 credit: ",font=("Goudy old style",12,"bold"),fg="gray",bg="white").place(x=500,y=190)   

        credit1=IntVar()
        credit2=IntVar()
        credit3=IntVar()
        credit4=IntVar()
        credit5=IntVar()
        Entry(Sem, textvariable = credit1,font=("Goudy old style",12,"bold"),bg="lightgray").place(x=700,y=30)   
        Entry(Sem, textvariable = credit2,font=("Goudy old style",12,"bold"),bg="lightgray").place(x=700,y=70) 
        Entry(Sem, textvariable = credit3,font=("Goudy old style",12,"bold"),bg="lightgray").place(x=700,y=110) 
        Entry(Sem, textvariable = credit4,font=("Goudy old style",12,"bold"),bg="lightgray").place(x=700,y=150)  
        Entry(Sem, textvariable = credit5,font=("Goudy old style",12,"bold"),bg="lightgray").place(x=700,y=190)  
        global result
        result = 0.0
        tgpa1_btn=Button(Sem,cursor="hand2",text="Calculate TGPA",fg="white",bg="#0895d1",command = self.tgpacalc,font=("times new roman",20)).place(x=150,y=250,width=250,height=40)
        global tgpa1
        tgpa1 = Label(Sem, text= result,font=("Goudy old style",20,"bold"),fg="red",bg="white").place(x=500,y=250)
        next = Button(Sem,bd=0,cursor='hand2', text= "NEXT >>",font=("Goudy old style",11,"bold"),command=self.tgpa2calc,fg="#07b3e3",bg="white").place(x=900,y=300)

    def tgpa2calc(self):
        screen3 = Toplevel(root)
        screen3.title("CGPA CALCULATOR")
        screen3.geometry("1000x800+500+70")
        screen3.resizable(False,False)

        heading = Label(screen3,text = "CGPA CALCULATOR", fg = "black", bg="grey",font=(20), width = "500", height= "3").pack()

        Label(screen3,text = "Second Semester",fg='white',font=(10), bg = "black",width = '500', height='2').pack()
        global Sem3
        Sem3=Frame(screen3,bg="white")
        Sem3.place(x=10,y=150,height=500,width=980)
        sub1 = Label(Sem3, text = "Enter Subject 1 grade: ",font=("Goudy old style",12,"bold"),fg="gray",bg="white").place(x=12,y=30)
        sub2 = Label(Sem3, text = "Enter Subject 2 grade: ",font=("Goudy old style",12,"bold"),fg="gray",bg="white").place(x=12,y=70)
        sub3 = Label(Sem3, text = "Enter Subject 3 grade: ",font=("Goudy old style",12,"bold"),fg="gray",bg="white").place(x=12,y=110)
        sub4 = Label(Sem3, text = "Enter Subject 4 grade: ",font=("Goudy old style",12,"bold"),fg="gray",bg="white").place(x=12,y=150)
        sub5 = Label(Sem3, text = "Enter Subject 5 grade: ",font=("Goudy old style",12,"bold"),fg="gray",bg="white").place(x=12,y=190)   

        global tgrade1
        global tgrade2
        global tgrade3
        global tgrade4
        global tgrade5
        tgrade1=StringVar()
        tgrade2=StringVar()
        tgrade3=StringVar()
        tgrade4=StringVar()
        tgrade5=StringVar()
        Entry(Sem3, textvariable = tgrade1,font=("Goudy old style",12,"bold"),bg="lightgray").place(x=210,y=30)   
        Entry(Sem3, textvariable = tgrade2,font=("Goudy old style",12,"bold"),bg="lightgray").place(x=210,y=70) 
        Entry(Sem3, textvariable = tgrade3,font=("Goudy old style",12,"bold"),bg="lightgray").place(x=210,y=110) 
        Entry(Sem3, textvariable = tgrade4,font=("Goudy old style",12,"bold"),bg="lightgray").place(x=210,y=150)  
        Entry(Sem3, textvariable = tgrade5,font=("Goudy old style",12,"bold"),bg="lightgray").place(x=210,y=190)  

        global tcredit1
        global tcredit2
        global tcredit3
        global tcredit4
        global tcredit5
        tcred1 = Label(Sem3, text = "Enter Subject 1 credit: ",font=("Goudy old style",12,"bold"),fg="gray",bg="white").place(x=500,y=30)
        tcred2 = Label(Sem3, text = "Enter Subject 2 credit: ",font=("Goudy old style",12,"bold"),fg="gray",bg="white").place(x=500,y=70)
        tcred3 = Label(Sem3, text = "Enter Subject 3 credit: ",font=("Goudy old style",12,"bold"),fg="gray",bg="white").place(x=500,y=110)
        tcred4 = Label(Sem3, text = "Enter Subject 4 credit: ",font=("Goudy old style",12,"bold"),fg="gray",bg="white").place(x=500,y=150)
        tcred5 = Label(Sem3, text = "Enter Subject 5 credit: ",font=("Goudy old style",12,"bold"),fg="gray",bg="white").place(x=500,y=190)   

        tcredit1=IntVar()
        tcredit2=IntVar()
        tcredit3=IntVar()
        tcredit4=IntVar()
        tcredit5=IntVar()
        Entry(Sem3, textvariable = tcredit1,font=("Goudy old style",12,"bold"),bg="lightgray").place(x=700,y=30)   
        Entry(Sem3, textvariable = tcredit2,font=("Goudy old style",12,"bold"),bg="lightgray").place(x=700,y=70) 
        Entry(Sem3, textvariable = tcredit3,font=("Goudy old style",12,"bold"),bg="lightgray").place(x=700,y=110) 
        Entry(Sem3, textvariable = tcredit4,font=("Goudy old style",12,"bold"),bg="lightgray").place(x=700,y=150)  
        Entry(Sem3, textvariable = tcredit5,font=("Goudy old style",12,"bold"),bg="lightgray").place(x=700,y=190)  
        global tresult
        tresult = 0.0
        tgpa2_btn=Button(Sem3,cursor="hand2",text="Calculate TGPA",fg="white",bg="#0895d1",command = self.tgpacalc2,font=("times new roman",20)).place(x=150,y=250,width=250,height=40)
        global tgpa2
        tgpa2 = Label(Sem3, text= tresult,font=("Goudy old style",20,"bold"),fg="red",bg="white").place(x=500,y=250)
        final_button = Button(Sem3,cursor="hand2",text="Know your CGPA",fg="white",bg="#000000",command = self.finalcgpa,font=("times new roman",20)).place(x=350,y=400,width=250,height=40)
        
        
    def tgpacalc2(self):
        a,b,c,d,e=0,0,0,0,0
        global tc1
        global tc2
        global tc3
        global tc4
        global tc5
        tc1=tcredit1.get()
        tc2=tcredit2.get()
        tc3=tcredit3.get()
        tc4=tcredit4.get()
        tc5=tcredit5.get()

        if(tgrade1.get()=="O" or tgrade1.get()=="o"):
            a = 10
        elif(tgrade1.get()=="A+" or tgrade1.get()=='a+'):
            a=9
        elif(tgrade1.get()=="A" or tgrade1.get()=='a'):
            a=8
        elif(tgrade1.get()=="B+" or tgrade1.get()=='b+'):
            a=7
        elif(tgrade1.get()=="B" or tgrade1.get()=='b'):
            a=6
        elif(tgrade1.get()=="C" or tgrade1.get()=='c'):
            a=5
        elif(tgrade1.get()=="D" or tgrade1.get()=="d"):
            a=4
        elif(tgrade1.get()=="E" or tgrade1.get()=='e'):
            a=0
        
        if(tgrade2.get()=="O" or tgrade2.get()=='o'):
            b=10
        elif(tgrade2.get()=="A+" or tgrade2.get()=='a+'):
            b=9
        elif(tgrade2.get()=="A" or tgrade2.get()=='a'):
            b=8
        elif(tgrade2.get()=="B+" or tgrade2.get()=='B+'):
            b=7
        elif(tgrade2.get()=="B" or tgrade2.get()=='B'):
            b=6
        elif(tgrade2.get()=="C" or tgrade2.get()=='c'):
            b=5
        elif(tgrade2.get()=="D" or tgrade2.get()=='d'):
            b=4
        elif(tgrade2.get()=="E" or tgrade2.get()=='e'):
            b=0

        if(tgrade3.get()=="O" or tgrade3.get()=='o'):
            c=10
        elif(tgrade3.get()=="A+" or tgrade3.get()=='a+'):
            c=9
        elif(tgrade3.get()=="A" or tgrade3.get()=='a'):
            c=8
        elif(tgrade3.get()=="B+" or tgrade3.get()=='B+'):
            c=7
        elif(tgrade3.get()=="B" or tgrade3.get()=='B'):
            c=6
        elif(tgrade3.get()=="C" or tgrade3.get()=='c'):
            c=5
        elif(tgrade3.get()=="D" or tgrade3.get()=='d'):
            c=4
        elif(tgrade3.get()=="E" or tgrade3.get()=='e'):
            c=0
            
        if(tgrade4.get()=="O" or tgrade4.get()=='o'):
            d=10
        elif(tgrade4.get()=="A+" or tgrade4.get()=='a+'):
            d=9
        elif(tgrade4.get()=="A" or tgrade4.get()=='a'):
            d=8
        elif(tgrade4.get()=="B+" or tgrade4.get()=='B+'):
            d=7
        elif(tgrade4.get()=="B" or tgrade4.get()=='B'):
            d=6
        elif(tgrade4.get()=="C" or tgrade4.get()=='c'):
            d=5
        elif(tgrade4.get()=="D" or tgrade4.get()=='d'):
            d=4
        elif(tgrade4.get()=="E" or tgrade4.get()=='e'):
            d=0
            
        if(tgrade5.get()=="O" or tgrade5.get()=='o'):
            e=10
        elif(tgrade5.get()=="A+" or tgrade5.get()=='a+'):
            e=9
        elif(tgrade5.get()=="A" or tgrade5.get()=='a'):
            e=8
        elif(tgrade5.get()=="B+" or tgrade5.get()=='B+'):
            e=7
        elif(tgrade5.get()=="B" or tgrade5.get()=='B'):
            e=6
        elif(tgrade5.get()=="C" or tgrade5.get()=='c'):
            e=5
        elif(tgrade5.get()=="D" or tgrade5.get()=='d'):
            e=4
        elif(tgrade5.get()=="E" or tgrade5.get()=='e'):
            e=0

        global tgparesult1
        tresult = ((a*c1)+(b*c2)+(c*c3)+(d*c4)+(e*c5))/(c1+c2+c3+c4+c5)
        round(tresult,2)
        tgparesult1=((a*c1)+(b*c2)+(c*c3)+(d*c4)+(e*c5))
        tgpa1 = Label(Sem3, text= tresult,font=("Goudy old style",20,"bold"),fg="red",bg="white").place(x=500,y=250)
        


    def tgpacalc(self):
        a,b,c,d,e=0,0,0,0,0
        global c1
        global c2
        global c3
        global c4
        global c5
        c1=credit1.get()
        c2=credit2.get()
        c3=credit3.get()
        c4=credit4.get()
        c5=credit5.get()
        if(grade1.get()=="O" or grade1.get()=="o"):
            a = 10
        elif(grade1.get()=="A+" or grade1.get()=='a+'):
            a=9
        elif(grade1.get()=="A" or grade1.get()=='a'):
            a=8
        elif(grade1.get()=="B+" or grade1.get()=='b+'):
            a=7
        elif(grade1.get()=="B" or grade1.get()=='b'):
            a=6
        elif(grade1.get()=="C" or grade1.get()=='c'):
            a=5
        elif(grade1.get()=="D" or grade2.get()=="d"):
            a=4
        elif(grade1.get()=="E" or grade1.get()=='e'):
            a=0
        
        if(grade2.get()=="O" or grade2.get()=='o'):
            b=10
        elif(grade2.get()=="A+" or grade2.get()=='a+'):
            b=9
        elif(grade2.get()=="A" or grade2.get()=='a'):
            b=8
        elif(grade2.get()=="B+" or grade2.get()=='B+'):
            b=7
        elif(grade2.get()=="B" or grade2.get()=='B'):
            b=6
        elif(grade2.get()=="C" or grade2.get()=='c'):
            b=5
        elif(grade2.get()=="D" or grade2.get()=='d'):
            b=4
        elif(grade2.get()=="E" or grade2.get()=='e'):
            b=0

        if(grade3.get()=="O" or grade3.get()=='o'):
            c=10
        elif(grade3.get()=="A+" or grade3.get()=='a+'):
            c=9
        elif(grade3.get()=="A" or grade3.get()=='a'):
            c=8
        elif(grade3.get()=="B+" or grade3.get()=='B+'):
            c=7
        elif(grade3.get()=="B" or grade3.get()=='B'):
            c=6
        elif(grade3.get()=="C" or grade3.get()=='c'):
            c=5
        elif(grade3.get()=="D" or grade3.get()=='d'):
            c=4
        elif(grade3.get()=="E" or grade3.get()=='e'):
            c=0
            
        if(grade4.get()=="O" or grade4.get()=='o'):
            d=10
        elif(grade4.get()=="A+" or grade4.get()=='a+'):
            d=9
        elif(grade4.get()=="A" or grade4.get()=='a'):
            d=8
        elif(grade4.get()=="B+" or grade4.get()=='B+'):
            d=7
        elif(grade4.get()=="B" or grade4.get()=='B'):
            d=6
        elif(grade4.get()=="C" or grade4.get()=='c'):
            d=5
        elif(grade4.get()=="D" or grade4.get()=='d'):
            d=4
        elif(grade4.get()=="E" or grade4.get()=='e'):
            d=0
            
        if(grade5.get()=="O" or grade5.get()=='o'):
            e=10
        elif(grade5.get()=="A+" or grade5.get()=='a+'):
            e=9
        elif(grade5.get()=="A" or grade5.get()=='a'):
            e=8
        elif(grade5.get()=="B+" or grade5.get()=='B+'):
            e=7
        elif(grade5.get()=="B" or grade5.get()=='B'):
            e=6
        elif(grade5.get()=="C" or grade5.get()=='c'):
            e=5
        elif(grade5.get()=="D" or grade5.get()=='d'):
            e=4
        elif(grade5.get()=="E" or grade5.get()=='e'):
            e=0
            


        global tgparesult2
        result = ((a*c1)+(b*c2)+(c*c3)+(d*c4)+(e*c5))/(c1+c2+c3+c4+c5)
        rs = round(result,2)
        tgparesult2 = ((a*c1)+(b*c2)+(c*c3)+(d*c4)+(e*c5))
        tgpa1 = Label(Sem, text= rs,font=("Goudy old style",20,"bold"),fg="red",bg="white").place(x=500,y=250)
        

        
    def finalcgpa(self):
        t=tgparesult2+tgparesult1
        print(t)
        f = c1+c2+c3+c4+c5+tc1+tc2+tc3+tc4+tc5
        print(f)
        cgpa = t/f
        ccgpa = round(cgpa,2)
        if(ccgpa>=8):
            messagebox.showinfo("What a score! Amazing!","You got a CGPA of {}".format(ccgpa),parent=Sem3)
        elif(ccgpa>=6 and ccgpa<8):
            messagebox.showinfo("Do a little hardwork!","You got a CGPA of {}".format(ccgpa),parent=Sem3)
        else:
            messagebox.showinfo("You must try harder!","You got a CGPA of {}".format(ccgpa),parent=Sem3)
        
        


root=Tk()

obj = login(root)
obj.login_form()


root.mainloop()
