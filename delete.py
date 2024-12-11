from tkinter import *
import pymysql
from tkinter import messagebox

win4 = Tk()
def Delete():
	DUID = DUid.get()
	conobj = pymysql.connect(host='localhost', user='root', password='', port=3306)
	curobj = conobj.cursor()
	curobj.execute('use julybatch;')
	test1 = f'select * from demo where UID = "{DUID}";'
	curobj.execute(test1)

	record = curobj.fetchall()
	print(record)
	if len(record):
		d = f'delete from demo where UID = "{DUID}";'
		#print(d)
		curobj.execute(d)
		conobj.commit()
		messagebox.showinfo('showinfo', 'record deleted')
		win4.destroy()
	else:
		messagebox.showerror()('showerror',"invalid userid")
		win4.destroy()

	curobj.close()
	conobj.close()

win4.title('Delete Student!')
#win.geometry('600x300') #changes dimension of window
win4.maxsize(500,300)
win4.minsize(500,300)

Label(win4, text = 'Enter User ID', font=('Elephant', 13), bg='yellow', fg='maroon', width=18, height=1, relief=GROOVE).place(x=50, y=100)

DUid = Entry(win4, width=22, font=('Consolas', 13), bg ='pink', fg='black')
DUid.place(x=280, y=100)

Button(win4, text = 'Delete', font=('Consolas', 13), bg='blue',fg='black', relief=GROOVE, command=Delete).place(x=200, y=180)

win4.mainloop()