import pymysql

conobj = pymysql.connect(host='localhost', user='root', password='',port=3306)

curobj = conobj.cursor()

#curobj.execute('create database JulyBatch;')

curobj.execute('use julybatch;')
#curobj.execute('create table DEMO (Fname varchar(20), Lname varchar(30), UID varchar(30), Gender varchar(9), AccYear varchar(10), Branch varchar(10), Password varchar(20));')

curobj.close()
conobj.close()
