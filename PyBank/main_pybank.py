count = 0
total = 0
chng = []
change = 867884
change1 = 0
change2 = 0
change3 = 0

import csv
with open(r"C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Resources\budget_data.csv", mode='r') as infile:
    reader = csv.reader(infile)
    header = next(reader)   
    for row in reader: 
        count = count + 1
        total = total + int(row[1])
        change = int(row[1]) - change + change1
        change1 = change - int(row[1])
        change2 = change2+change
        chng.append(change)
#print(chng)
#print(min(chng))
#print(max(chng))
                
# I have to update this script to write the months against the grt inc, dec in profits. My thinking
# is to write a column using chng[] to the original file. then using the index of these values
# find the corresponding months. Need help here!!
            

print("Financial Analysis")
print("---------------------------------")
print("Total Months: " + str(count))
print("Total: " + str(total))          
print("Average Change: " + str(change2/(count-1)))
print("Greatest Increase in Profits: " + str(max(chng)))
print("Greatest deccrease in Profits: " + str(min(chng)))



        
