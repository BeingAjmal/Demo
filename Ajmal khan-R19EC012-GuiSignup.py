from tkinter import *
from tkinter import messagebox as MsgBoxVap

import sqlite3
from sqlite3 import Error
db = sqlite3.connect("signup.db")

#-------------- create table function -------------------------
def create_tabel():
    db = sqlite3.connect("signup.db") 
    try:
        cur=db.cursor()
        cur.execute('''CREATE TABLE khan(
        name TEXT (30) NOT NULL,
        email TEXT (30) NOT NULL,
        phone INTEGER,
        password TEXT (20) NOT NULL);''')
        MsgBoxVap.showinfo("Success","Tabel created successfully!!")
    except Error as e:
            print ('error in operation',e)
            db.rollback()
    db.close()
	
#---------------insert records function-------------------------

SupWdwVar = Tk()

SupWdwVar.title("Login and registration")

#SupWdwVar.geometry("600x600")

SupWdwVar.minsize(400,500)

SupWdwVar.configure(background="white")

UserInfo = {}

LblVar = Label(SupWdwVar, text="                    Login                   ", font="arial 24 bold",bg="yellow",fg="blue")
LblVar.pack()
LblVar = Label(SupWdwVar, text=" ", font="arial 16 bold", bg="white")
LblVar.pack()

LgnMylBoxVar = Entry(SupWdwVar, font="arial 24 bold",fg="blue",bg="white",relief="solid")
LgnMylBoxVar.insert(0,"Enter Email-id")
LgnMylBoxVar.pack()
LgnPwdBoxVar = Entry(SupWdwVar, font="arial 24 bold", show="*",bg="white",fg="blue",relief="solid")
LgnPwdBoxVar.insert(0,"Enter Password")
LgnPwdBoxVar.pack()
def LoginClickFnc():
	LgnMylVar = LgnMylBoxVar.get()
	LgnPwdVar = LgnPwdBoxVar.get()

	if(LgnMylVar == UserInfo["Email"] and LgnPwdVar == UserInfo["UsrPwdVar"]):
		MsgBoxVap.showinfo("Success","Login Successfull")
	else:
		MsgBoxVap.showerror("Error", "Invalid Login details")

Button(SupWdwVar, text="Login",
	bg="yellow", fg="blue",
    width=10, command=LoginClickFnc,
	font="arial 20 bold").pack()

LblVar = Label(SupWdwVar, text=" ", font="arial 16 bold", bg="white")
LblVar.pack()
LblVar = Label(SupWdwVar, text="***\t(OR)\t***", font="arial 16 bold",bg="red",fg="black")
LblVar.pack()
LblVar = Label(SupWdwVar, text=" ", font="arial 16 bold", bg="white")
LblVar.pack()
LblVar = Label(SupWdwVar, text="             Registration              ", font="arial 24 bold",bg="yellow",fg="blue")
LblVar.pack()
LblVar = Label(SupWdwVar, text=" ", font="arial 16 bold", bg="white")
LblVar.pack()
RegNamBoxVar = Entry(SupWdwVar, font="arial 24 bold",fg="blue",bg="white",relief="solid")
RegNamBoxVar.insert(0,"Enter  UserName")
RegNamBoxVar.pack()


RegMblBoxVar = Entry(SupWdwVar, font="arial 24 bold",fg="blue",bg="white",relief="solid")
RegMblBoxVar.pack()
RegMylBoxVar = Entry(SupWdwVar, font="arial 24 bold",fg="blue",bg="white",relief="solid")
RegMylBoxVar.insert(0,"Enter Email-id")
RegMylBoxVar.pack()

RegPwdBoxVar = Entry(SupWdwVar, font="arial 24 bold", show="*",fg="blue",bg="white",relief="solid")
RegPwdBoxVar.insert(0,"Enter Password")
RptPwdBoxVar = Entry(SupWdwVar, font="arial 24 bold", show="*",fg="blue",bg="white",relief="solid")
RptPwdBoxVar.pack()

def RegClickFnc():
	while(True):
		Username=RegNamBoxVar.get()
		if(Username =="Enter  UserName"):
			MsgBoxVap.showerror("Error", "Enter valid username")
			break
		elif (not(Username and Username.strip())):
			MsgBoxVap.showerror("Error", "username cannot be blank")
			break
		else:
			UserInfo["Username"] = RegNamBoxVar.get()

		Mblno=RegMblBoxVar.get()
		if((Mblno.isdigit() == False) or (len(Mblno) != 10)):
			MsgBoxVap.showerror("Error", "Enter valid mobile number")
			break
		else:
			UserInfo["Mblno"] = RegMblBoxVar.get()
		
		Email=RegMylBoxVar.get()
		if((('@' in Email)==False) or(Email[0].isdigit()== True)):
			MsgBoxVap.showerror("Error", "Enter valid Email id")
			break
		else:
			UserInfo["Email"] = RegMylBoxVar.get()

		Pwd = RegPwdBoxVar.get()
		Rptwd = RptPwdBoxVar.get()
		if(len(Pwd) < 8):
			MsgBoxVap.showerror("Error", "Enter valid password")
			break
		elif(Pwd!=Rptwd):
			MsgBoxVap.showerror("Error", "Passwords do not match")
			break
		else:
			MsgBoxVap.showinfo("Success" , "Registered Successfully")
			UserInfo["UsrPwdVar"] =Pwd 
			break
		
Button(SupWdwVar, text="Sign Up",
	bg="yellow", fg="blue",
	width=10, command=RegClickFnc,
    font="arial 20 bold").pack()

SupWdwVar.mainloop()




			


		








			


	
	