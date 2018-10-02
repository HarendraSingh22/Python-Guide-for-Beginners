import sqlite3

conn = sqlite3.connect('emp.db')

c=conn.cursor()

#conn.execute("CREATE TABLE emp(SAP INT,NAME TEXT,CITY TEXT,SALARY INT)")

print("Enter\n1.insert\n2.delete\n3.update\n4.retrieve\n5.exit")

choice = int(input("Enter a choice:"))

while choice!=5:
	if choice==1:
		print("enter data to inset")
		name=(input("Enter name"))
		sid=int(input("Enter the sap"))
		city=(input("Enter city"))
		salary=int(input("Enter the salary"))
		c.execute("INSERT INTO emp values(:id,:name1,:city1,:sal1)",{'id':sid,'name1':name,'city1':city,'sal1':salary})
		conn.commit()
	if choice==2:
		print("enter sap to delete records")
		sid=int(input("Enter the sap"))
		c.execute("DELETE FROM emp WHERE SAP=?",(sid,))
		conn.commit()
	if choice==3:
		sid=int(input("Enter the sap to update"))
		salary=int(input("Enter the updated salary"))
		c.execute("UPDATE emp SET SALARY=? WHERE SAP=?",(salary,sid,))
		conn.commit()
	if choice==4:
		c.execute("SELECT * FROM emp")
		for i in c.fetchall():
			print(i)
	print("Enter\n1.insert\n2.delete\n3.update\n4.retrieve\n5.exit")
	choice = int(input("Enter a choice:"))	

