import csv
import sqlite3

def table_csv_comparing():
	csv_list=[]
	table_list = []
	database_name = raw_input('Enter the Database Name :')
	csv_name=raw_input("enter the csv file name:")
	database_name = database_name+".db"
	conn = sqlite3.connect(database_name)
	c= conn.cursor()
	table_values = c.execute("SELECT * FROM cricket")
	for i in table_values:
		table_list.append(list(i))
	print table_list
	
	with open(csv_name,"rb") as f:
		reader=csv.reader(f,delimiter=",")
		for line in reader:
			csv_list.append(line)
	print(csv_list)
	f.close()
	conn.close()
	
table_csv_comparing()
