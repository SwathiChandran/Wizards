import csv
def reading_csv():
    csv_name=raw_input("enter the csv file name:")
    csv_list=[]
    with open(csv_name,"rb") as f:
        reader=csv.reader(f,delimiter=",")
        for line in reader:
            csv_list.append(line)
        print(csv_list)
    f.close()
reading_csv()
