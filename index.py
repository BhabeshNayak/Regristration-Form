from tkinter import * #import module
from tkinter import messagebox
import pymysql
win = Tk() #Tk() is a predefined class, win is the obj of Tk() class

def Login():
	Lusername = Uid.get()
	Lpassword = Pwd.get()
	#print(Lusername, Lpassword)
	conobj = pymysql.connect(host='localhost', user='root', password='', port=3306)
	curobj = conobj.cursor()
	curobj.execute('use julybatch;')
	test = f'select * from demo where UID = "{Lusername}" and Password="{Lpassword}";' 
	curobj.execute(test)
	record = curobj.fetchall()
	if len(record):
		messagebox.showinfo('showinfo',"Login Sucessful") 
		import operation
	else:
		messagebox.showerror('showerror',"Invalid Username & Password")
		win.destroy()
	
	curobj.close()
	conobj.close()

def Reset():
	Uid.delete(0, END)
	Pwd.delete(0, END)
def Exit():
	win.destroy()
def NewUser():
	import signup


win.title('Login Page!')
#win.geometry('600x300') #changes dimension of window
win.maxsize(600,500)
win.minsize(600,500)

Label(win, text = 'Please Login Here!!!', font=('Elephant', 15), bg='aqua', width=30, height=2, relief=GROOVE).place(x=90, y=50)

Label(win, text = 'Enter User ID', font=('Consolas', 13), bg='silver', fg='blue', width=20, height=1, relief=GROOVE).place(x=100, y=150)

Uid = Entry(win, width=22, font=('Consolas', 13), bg ='pink', fg='black')
Uid.place(x=310, y=152)

Label(win, text = 'Enter Password', font=('Consolas', 13), bg='silver', fg='blue', width=20, height=1, relief=GROOVE).place(x=100, y=200)

Pwd = Entry(win, width=22, font=('Consolas', 13), bg ='pink', fg='black', show='*')
Pwd.place(x=310, y=202)

Button(win, text = 'Login', font=('Consolas', 13), bg='#dcd6d0', command=Login).place(x=180, y=300)
Button(win, text = 'Reset', font=('Consolas', 13), bg='#dcd6d0', command=Reset).place(x=280, y=300)
Button(win, text = 'Exit', font=('Consolas', 13), bg='#dcd6d0', command=Exit).place(x=380, y=300)

Button(win, text= 'New Registration', font=('Consolas', 13), bg='#dcd6d0',width=20, command=NewUser).place(x=210, y=400)





win.mainloop()