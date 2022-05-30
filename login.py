from optparse import Option
from tkinter import *
from PIL import ImageTk,Image,ImageDraw
class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("800x600")
        
        # BACKGROUND IMAGE
        self.bg =ImageTk.PhotoImage(file="images/image.jpg")
        self.bg_image = Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        # VARIABLE
        userNameVariable = StringVar
      
        
        
        
        
        # INSERT FRAME 
        
        frame = Frame(self.root,bg="white")
        frame.place(x=50,y=50,width=700,height=500)
        
        # TITLE
        title = Label(frame,text="PHARMACY LOGIN SYSTEM",font=("Impact",25,"bold"),fg="#FC990C",bg="white").place(x=150,y=30)
        
        # SUBTITLE
        subtitle = Label(frame,text="LOGIN HERE",font=("Goudy old style",15),fg="#1d1d1d",bg="white").place(x=150,y=100)
        
        # USERNAME
        username = Label(frame,text="Username",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=150,y=150)
        
        # userName Entry
        usernameEntry = Entry(frame,textvariable=userNameVariable,font=("Goudy old style",15,"bold",),bg="#E7E6E6").place(x=280,y=155,width=350,)
        
        # USER PASSWORD
        userpassword = Label(frame,text="password",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=150,y=200)
        
        # password Entry
        passwordEntry = Entry(frame,textvariable=userNameVariable,font=("Goudy old style",15,"bold",),bg="#E7E6E6").place(x=280,y=200,width=350,)
        
        # FORGOT PASSWORD
        forgot_Password = Button(frame,text="Forgot password?",bd=0,font=("Goudy old style",15,"bold"),fg="blue",bg="white").place(x=150,y=250)

        # DROPDOWN BUTTON
        # SUBMIT BUTTON
        button = Button(frame,text="LOGIN",width=40, font=("Goudy old style",15,"bold"),fg="white",bg="#6162ff").place(x=150,y=300)
       
    


root = Tk()
obj = Login(root)
root.mainloop()
