from tkinter import*
from tkinter import messagebox
win2 = Tk()

def Submit():
	import pymysql

	conobj = pymysql.connect(host='localhost', user='root', password='',port=3306)

	curobj = conobj.cursor()

	a = RFname.get()
	b = RLname.get()
	c = RUname.get()
	d = Gvar.get()
	e = AcYear.get()
	f = Bvar.get()
	g = Rpwd.get()
	#print(a,b,c,d,e,f,g)

	

	#curobj.execute('create database JulyBatch;')

	curobj.execute('use julybatch;')
	#curobj.execute('create table DEMO (Fname varchar(20), Lname varchar(30), UID varchar(30), Gender varchar(9), AccYear 	tvarchar(10), Branch varchar(10), Password varchar(20));')

	r = 'insert into DEMO values("{Fname}", "{Lname}", "{UID}", "{Gender}", "{AccYear}", "{Branch}", "{Password}");'
	r1 = r.format(Fname=a, Lname=b, UID=c, Gender=d, AccYear=e, Branch=f, Password=g)

	#print(r1)
	curobj.execute(r1)
	conobj.commit()

	curobj.close()
	conobj.close()
	messagebox.showinfo('showinfo',"Registration Sucessful")

	win2.destroy()
def Reset():
	RFname.delete(0, END)
	RLname.delete(0, END)
	RUname.delete(0, END)
	Gvar.set(None)
	AcYear.set(None)
	Bvar.set(None)
	Rpwd.delete(0, END)
def Exit():
	win2.destroy()

win2.title("signup")
win2.maxsize(600, 700)
win2.minsize(600, 700)

Label(win2, text='Please Signup Here!!', font=('Felix Titling', 20), bg='aqua', fg='white', width=20, relief=GROOVE).place(x=120, y=50)

Label(win2, text='Enter First Name', font=('Book Antiqua', 12), bg='silver', fg='blue', width=15, relief=GROOVE).place(x=120, y=150)

RFname = Entry(win2, font=('Book Antiqua', 12), bg='pink', fg='black', width=19, relief=GROOVE)
RFname.place(x=330, y=150)

Label(win2, text='Enter Last Name', font=('Book Antiqua', 12), bg='silver', fg='blue', width=15, relief=GROOVE).place(x=120, y=200)

RLname = Entry(win2, font=('Book Antiqua', 12), bg='pink', fg='black', width=19, relief=GROOVE)
RLname.place(x=330, y=200)

Label(win2, text='Enter User Name', font=('Book Antiqua', 12), bg='silver', fg='blue', width=15, relief=GROOVE).place(x=120, y=250)

RUname = Entry(win2, font=('Book Antiqua', 12), bg='pink', fg='black', width=19, relief=GROOVE)
RUname.place(x=330, y=250)

Label(win2, text='Select Gender', font=('Book Antiqua', 12), bg='silver', fg='blue', width=15, relief=GROOVE).place(x=120, y=300)

Gvar = StringVar() 
#R1 = Radiobutton(win2, text="Male", font=('Book Antiqua', 12), variable= Gvar, value='M').place(x=325, y=300)
#R2 = Radiobutton(win2, text="Female", font=('Book Antiqua', 12), variable= Gvar, value='F').place(x=405, y=300)
Gvar.set('Select Gender ')
G=OptionMenu(win2,Gvar,'Male','Female')
G.place(x=330,y=300)

Label(win2, text='Select Acc Year', font=('Book Antiqua', 12), bg='silver', fg='blue', width=15, relief=GROOVE).place(x=120, y=350)

AcYear = StringVar()
AcYear.set('Select Any Acc year')
A = OptionMenu(win2, AcYear, '2018-22', '2019-23', '2020-24', '2021-25')
A.place(x=328, y=350)

Label(win2, text='Select Branch', font=('Book Antiqua', 12), bg='silver', fg='blue', width=15, relief=GROOVE).place(x=120, y=400)

Bvar = StringVar()
Bvar.set('Select Any Branch')
A = OptionMenu(win2, Bvar, 'CSE', 'CS-IT', 'Mech', 'Civil', 'EEE', 'ECE', 'EE')
A.place(x=328, y=400)

Label(win2, text='Enter Password', font=('Book Antiqua', 12), bg='silver', fg='blue', width=15, relief=GROOVE).place(x=120, y=450)

Rpwd = Entry(win2, font=('Book Antiqua', 12), bg='pink', fg='black', width=19, relief=GROOVE, show='*')
Rpwd.place(x=330, y=450)

Button(win2, text = 'Signup', font=('Consolas', 13), bg='#dcd6d0', command=Submit).place(x=170, y=550)
Button(win2, text = 'Reset', font=('Consolas', 13), bg='#dcd6d0', command=Reset).place(x=270, y=550)
Button(win2, text = 'Exit', font=('Consolas', 13), bg='#dcd6d0', command=Exit).place(x=370, y=550)




win2.mainloop()