from tkinter import *
import pymysql
from tkinter import messagebox


win7= Tk()
def Update ():
	DUID = DUid.get()
	conobj = pymysql.connect(host = 'localhost',user = 'root',password = '',port = 3306)
	curobj = conobj.cursor()
	curobj.execute('use julybatch;')

	test1 = f'select * from demo where UID = "{DUID}";'
	curobj.execute(test1)
	
	record = curobj.fetchall ()
	#print (record)
	if len(record) :

		win8 = Tk()
		def Save () :
			a = UFname.get()
			b = ULname.get()
			c = UGvar.get()
			d = UAcYear.get()
			e = UBvar.get()
			U = f'update demo set FName = "{a}", LName = "{b}", Gender = "{c}", AccYear = "{d}", Branch ="{e}" where UID = "{DUID}";'
			#print(U)

			curobj.execute(U)
			conobj.commit ()
			#print(a,b,c,d,e)
		win8.title('Update Info!')

		win8.maxsize(600,700)
		win8.minsize(600,700)
		print('valid user')
		Label(win8, text='Enter First Name', font=('Book Antiqua', 12), bg='silver', fg='blue', width=15, relief=GROOVE).place(x=120, y=150)

		UFname = Entry(win8, font=('Book Antiqua', 12), bg='pink', fg='black', width=19, relief=GROOVE)
		UFname.place(x=330, y=150)

		Label(win8, text='Enter Last Name', font=('Book Antiqua', 12), bg='silver', fg='blue', width=15, relief=GROOVE).place(x=120, y=200)

		ULname = Entry(win8, font=('Book Antiqua', 12), bg='pink', fg='black', width=19, relief=GROOVE)
		ULname.place(x=330, y=200)

		Label(win8, text='Select Gender', font=('Book Antiqua', 12), bg='silver', fg='blue', width=15, relief=GROOVE).place(x=120, y=300)

		UGvar = StringVar() 
		#R1 = Radiobutton(win8, text="Male", font=('Book Antiqua', 12), variable= UGvar, value='M').place(x=325, y=300)
		#R2 = Radiobutton(win8, text="Female", font=('Book Antiqua', 12), variable= UGvar, value='F').place(x=405, y=300)
		Gvar.set('Select Gender ')
		G=OptionMenu(win8,Gvar,'Male','Female')
		G.place(x=330,y=300)

		Label(win8, text='Select Acc Year', font=('Book Antiqua', 12), bg='silver', fg='blue', width=15, relief=GROOVE).place(x=120, y=350)

		UAcYear = StringVar()
		UAcYear.set('Select Any Acc year')
		A = OptionMenu(win8, UAcYear, '2018-22', '2019-23', '2020-24', '2021-25')
		A.place(x=328, y=350)

		Label(win8, text='Select Branch', font=('Book Antiqua', 12), bg='silver', fg='blue', width=15, relief=GROOVE).place(x=120, y=400)

		UBvar = StringVar()
		UBvar.set('Select Any Branch')
		A = OptionMenu(win8, UBvar, 'CSE', 'CS-IT', 'Mech', 'Civil', 'EEE', 'ECE', 'EE')
		A.place(x=328, y=400)
		Button(win8, text = 'Update', font=('Consolas', 13), bg='#dcd6d0', command = Save).place(x=170, y=550)

		win8.mainloop()
		'''
		d=f'delete from demo where UID = "{DUID}";'
		curobj.execute(d)
		conobj.commit()
		messagebox.showinfo('showinfo','one record is delete')
		win7.destroy() 
		'''
	else :
		messagebox.showerror('showerror','invalid userid')
		win7.destroy() 	
	

	curobj.close()
	conobj.close()
	

win7.title('Delete Student')

win7.maxsize(500,300)
win7.minsize(500, 300)

Label (win7, text = 'Enter Uid',font=('Elephant',13),bg='olive',fg = 'maroon',width = 10 ,relief = GROOVE).place (x = 60, y = 100)


DUid=Entry (win7,width = 20,font=('Consolas',15),bg ='#00ffff',fg = 'black')
DUid.place (x=250,y = 100)

Button(win7,text='Update',font=('Ebrima',15),bg ='orange',fg="blue",relief=GROOVE,command= Update).place(x=150,y=250)

win7.mainloop ()



