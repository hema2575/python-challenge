count = 0
total = 0
d = []
pl = []
chng=[]

mx = 0
mn = 0
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
#print(d)
#print(pl)
#print(chng)
#print(round(sum(chng)/len(chng), 2))
mx = max(chng) 
mn = min(chng)
print (mx)
print (mn)
mxindex = chng.index(mx)
mnindex = chng.index(mn)
print(mxindex)
print(mnindex)
dtemx = d[mxindex+1]
print(f" {dtemx} ($ {mx} ) ")
dtemn = d[mnindex+1]
print(f" {dtemn} ($ {mn} )")
#create the results
with open(r"C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Resources\budget_data_1.csv", mode='r') as csv_file:
    resultreader = csv.reader(csv_file)
    header = next(resultreader)   
    for row in resultreader: 
        count = count + 1
        total = total + int(row[1])
        avgCh = (round(sum(chng)/len(chng), 2))
#        print(row)
      
# writing the output to a text file inside Analysis folder. 
o1 = open(r'C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Analysis\outfile_01','w')

print("Financial Analysis", file=o1)
print("---------------------------------", file=o1)
print("Total Months: " + str(count), file=o1)
print("Total: " + "$" + str(total), file=o1)          
print("Average Change: " + "$" + str(avgCh), file=o1)   
print("Greatest Increase in Profits: " + dtemx + "($"+str(mx)+")", file=o1)
print("Greatest Decrease in Profits: " + dtemn + "($"+str(mn)+")", file=o1)
print("output to txtfile successful")
o1.close()










