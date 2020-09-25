

#import csv
#with open(r"C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Resources\budget_data.csv", newline ='') as csvfile:
#   reader = csv.reader(csvfile)
#   for row in reader:
#       sum()
#       print(total)
       
       
#from csv import DictReader
# open file in read mode
#with open(r"C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Resources\budget_data.csv", 'r') as read_obj:
    # pass the file object to Dictreader() to get the reader object
 #   csv_dict_reader = DictReader(read_obj)  
        # Iterate over each row after the header in the csv
#    for row in csv_dict_reader:
            # row variable is a dictionary that represents a row in csv
#            print(row['Date'],row['Profit/Losses'])
            


from csv import DictReader
# open file in read mode
with open(r"C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Resources\budget_data.csv", 'r') as read_obj:
    count = 0
    # pass the file object to Dictreader() to get the reader object
    csv_dict_reader = DictReader(read_obj)  
        # Iterate over each row after the header in the csv
    for row in enumerate(csv_dict_reader):
            # row variable is a dictionary that represents a row in csv
            count = count + 1
           
    print ('Total Months: ' + str(count))