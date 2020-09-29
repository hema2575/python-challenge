# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 12:58:47 2020

@author: muthukumar
"""

count = 0
total = 0
chng = []
change = 867884
change1 = 0
change2 = 0
change3 = 0
#calculating count, total. Populating the list named chng[]
import csv
with open(r"C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Resources\budget_data.csv", mode='r') as csv_file:
    reader = csv.reader(csv_file)
    header = next(reader)   
    for row in reader: 
        count = count + 1
        total = total + int(row[1])
        change = int(row[1]) - change + change1
        change1 = change - int(row[1])
        change2 = change2+change
        chng.append(change)

# writing the output to a text file inside Analysis folder. 
o = open(r'C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Analysis\outfile','w')

print("Financial Analysis", file=o)
print("---------------------------------", file=o)
print("Total Months: " + str(count), file=o)
print("Total: " + str(total), file=o)          
print("Average Change: " + str(round(change2/(len(chng)-1), 2)), file=o)
print("Greatest Increase in Profits: " + str(max(chng)), file=o)
print("Greatest Decrease in Profits: " + str(min(chng)), file=o)
print("output to txtfile successful")
o.close()