import sqlite3
def database_connectivity():
	try:
		database_name = raw_input('Enter the Database Name :')
		database_name = database_name+".db"
		conn = sqlite3.connect(database_name)
		c= conn.cursor()
		return conn
	except Exception as error:
		print error
sample=database_connectivity()
if sample:
		print "connection successfull"	
else:
		print "no"