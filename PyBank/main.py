count = 0
total = 0
d = []
pl = []
chng=[]

#calculating count, total. Populating the list named chng[]
import os
import csv
import itertools
with open(r"C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Resources\budget_data.csv", mode='r') as csv_file:
    inptreader = csv.reader(csv_file)
    header = next(inptreader)   
    for row in inptreader: 
        d.append(row[0])
        pl.append(int(row[1]))
chng = [y-x for x, y in zip(pl, pl[1:])]

mx = max(chng) 
mn = min(chng)
mxindex = chng.index(mx)
mnindex = chng.index(mn)
dtemx = d[mxindex+1]
dtemn = d[mnindex+1]

#create the results
with open(r"C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Resources\budget_data_1.csv", mode='r') as csv_file:
    resultreader = csv.reader(csv_file)
    header = next(resultreader)   
    for row in resultreader: 
        count = count + 1
        total = total + int(row[1])
        avgCh = (round(sum(chng)/len(chng), 2))
     
# writing the output to a text file inside Analysis folder. 
f1 = open(r'C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Analysis\outfile.txt','w')

print("Financial Analysis", file=f1)
print("---------------------------------", file=f1)
print("Total Months: " + str(count), file=f1)
print("Total: " + "$" + str(total), file=f1)          
print("Average Change: " + "$" + str(avgCh), file=f1)   
print("Greatest Increase in Profits: " + dtemx + "($"+str(mx)+")", file=f1)
print("Greatest Decrease in Profits: " + dtemn + "($"+str(mn)+")", file=f1)
print("output to txtfile successful")
f1.close()

#print(d)
#print(pl)
#print(chng)
#print(round(sum(chng)/len(chng), 2))
#print (mx)
#print (mn)
#print(mxindex)
#print(mnindex)
#print(f" {dtemx} ($ {mx} ) ")
#print(f" {dtemn} ($ {mn} )")




