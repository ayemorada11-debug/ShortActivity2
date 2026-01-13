import csv
import os
import time

Base = os.path.dirname(os.path.abspath(__file__))
Csv_Folder = os.path.join(Base, "RESOURCES")
Csv_Path = os.path.join(Csv_Folder, "FIRSTCSV.csv")
print(Csv_Path)

csv_data = []#empty list

with open(Csv_Path, mode= 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)
        csv_data.append(row) #add list

print("----------------------------------------------------------------------------------")
print(csv_data)#list of lists
print(csv_data[3])#list

#NAME IS COLUMN 1
#ADDRESS IS COLUMN 5

csv_newdata = []
for row in csv_data:
    csv_newdata.append([row[1], row[5]])

print(csv_newdata)

with open(os.path.join(Csv_Folder, "WRITECSV.csv"), mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_newdata)