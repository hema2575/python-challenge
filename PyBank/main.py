count = 0
total = 0
d = []
pl = []
chng=[]
# Calculating total months, net total. 
import csv
with open(r"C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Resources\budget_data.csv", mode='r') as csv_file:
    inptreader = csv.reader(csv_file)
    header = next(inptreader)   
    for row in inptreader:
        count = count + 1
        total = total + int(row[1])
#Populating the list named chng[], calculating average difference in profit/losses       
        d.append(row[0])
        pl.append(int(row[1]))
chng = [y-x for x, y in zip(pl, pl[1:])]
mx = max(chng) 
mn = min(chng)
avgCh = (round(sum(chng)/len(chng), 2))
#determine the month where Greatest inc, dec in profits-diff occurs
mxindex = chng.index(mx)
mnindex = chng.index(mn)
dtemx = d[mxindex+1]
dtemn = d[mnindex+1]
       

#create the results
print("\n")
print("Financial Analysis")
print("---------------------------------")
print("Total Months: " + str(count))
print("Total: " + "$" + str(total))          
print("Average Change: " + "$" + str(avgCh))   
print("Greatest Increase in Profits: " + dtemx + "($"+str(mx)+")")
print("Greatest Decrease in Profits: " + dtemn + "($"+str(mn)+")")
     
# writing the output to a text file inside Analysis folder. 
f1 = open(r'C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Analysis\outfile.txt','w')

print("Financial Analysis", file=f1)
print("---------------------------------", file=f1)
print("Total Months: " + str(count), file=f1)
print("Total: " + "$" + str(total), file=f1)          
print("Average Change: " + "$" + str(avgCh), file=f1)   
print("Greatest Increase in Profits: " + dtemx + "($"+str(mx)+")", file=f1)
print("Greatest Decrease in Profits: " + dtemn + "($"+str(mn)+")", file=f1)
print("\n")
print("output to txtfile successful")
f1.close()
