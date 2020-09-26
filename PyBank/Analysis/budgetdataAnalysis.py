
count = 0
total = 0
change = []
import csv
with open(r"C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Resources\budget_data.csv", newline ='') as csvfile:
   reader = csv.reader(csvfile)
   #Iterate over each row after the header in the csv
   header = next(reader)
#  print(header)
   for row in reader:
       count = count + 1
       total = total + int(row[1])
print(count)
print(total)
print(total / count)

def grtprofit(budget_data):
    
    grtprofit(row)

def grtloss(budget_data):
    
    grtloss(row)


def avgPLChange(budget_data):
    
    avgPLChange(row)
    

   
 
            
            

       
  

    
  