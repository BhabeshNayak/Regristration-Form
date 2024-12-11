from tkinter import *
import pymysql
from tkinter import messagebox

win5 = Tk()
def Search():
	DUID = DUid.get()
	conobj = pymysql.connect(host='localhost', user='root', password='', port=3306)
	curobj = conobj.cursor()
	curobj.execute('use julybatch;')
	test1 = f'select * from demo where UID = "{DUID}";'
	curobj.execute(test1)

	record = curobj.fetchall()
	if len(record):
		print(record)
		win5.destroy()
	else:
		messagebox.showerror()('showerror',"invalid userid")
		win5.destroy()

	curobj.close()
	conobj.close()

win5.title('Delete Student!')
#win.geometry('600x300') #changes dimension of window
win5.maxsize(500,300)
win5.minsize(500,300)

Label(win5, text = 'Enter User ID', font=('Elephant', 13), bg='yellow', fg='maroon', width=18, height=1, relief=GROOVE).place(x=50, y=100)

DUid = Entry(win5, width=22, font=('Consolas', 13), bg ='pink', fg='black')
DUid.place(x=280, y=100)

Button(win5, text = 'Search', font=('Consolas', 13), bg='blue',fg='black', relief=GROOVE, command=Search).place(x=200, y=180)

win5.mainloop()