count = 0
total = 0
Date = []
PrLss = []
chng = []
change = 867884
change1 = 0
change2 = 0
change3 = 0
#calculating count, total. Populating the list named chng[]
import os
import csv
with open(r"C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Resources\budget_data.csv", mode='r') as csv_file:
    inptreader = csv.reader(csv_file)
    header = next(inptreader)   
    for row in inptreader: 
        change = int(row[1]) - change + change1
        change1 = change - int(row[1])
        change2 = change2+change
        chng.append(change)
#print(chng)
#creating 2 more lists namely Date, PrLss
        Date.append(row[0]) 
        PrLss.append(row[1])
        
# Zip lists together
ziplistsfornewcsv = zip(Date, PrLss, chng)   

#Now writing to a new csv     
#set variable for outputfile
outputwrtr = os.path.join(r'C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Resources\budget_data_1.csv')
#  Open the output file
with open(outputwrtr, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    # Write the header row
    writer.writerow(["Date", "Profit/Losses", "Difference"])
    # Write in zipped rows
    writer.writerows(ziplistsfornewcsv)
print("File write successful")

#Creating functions that will determine the row where the max profit change, max loss change occur(not working as of 9/29 :-())

def grInc(number):
    with open(r"C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Resources\budget_data_1.csv", mode='r') as csv_file:
        resultreader = csv.reader(csv_file)
        header = next(resultreader)  
        for row in resultreader:
            if row[2] == number:
                print(row)
                dte1 = row[0]
                prls1 = row[1]
                print(f" {dte1} {prls1} ")
#Creating functions that will determine the row where the max profit change, max loss change occur(not working as of 9/29 :-())
def grDec(number):
    with open(r"C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Resources\budget_data_1.csv", mode='r') as csv_file:
        resultreader = csv.reader(csv_file)
        header = next(resultreader)  
        for row in resultreader:
            if row[2] == number:
                dte2 = row[0]
                prls2 = row[1]
                print(f" {dte2} {prls2} ")
  
#create the results
with open(r"C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Resources\budget_data_1.csv", mode='r') as csv_file:
    resultreader = csv.reader(csv_file)
    header = next(resultreader)   
    for row in resultreader: 
        count = count + 1
        total = total + int(row[1])
        avgCh = round(change2/(len(chng)-1), 2) 
        gprInc = max(chng)
        gprDec = min(chng)
#print(row[2])
# writing the output to a text file inside Analysis folder. 
o = open(r'C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Analysis\outfile','w')

print("Financial Analysis", file=o)
print("---------------------------------", file=o)
print("Total Months: " + str(count), file=o)
print("Total: " + "$" + str(total), file=o)          
print("Average Change: " + "$" + str(round(change2/(len(chng)-1), 2)), file=o)
print("Greatest Increase in Profits: " + "$" + str(grInc(max(chng))), file=o)
print("Greatest Decrease in Profits: " + "$" + str(grDec(min(chng))), file=o)
print("output to txtfile successful")
o.close()










