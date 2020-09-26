
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

def grt(budget_data):
    # For readability, it can help to assign your values to variables with descriptive names
    profitOrloss = int(budget_data[1])

    # Total months can be found by counting the number of rows
    total_months = wins + losses + draws

    # The average of the changes in "Profit/Losses" over the entire period can be found by dividing the nettotal by count
     

    # Draw percent can be found by dividing the total draws by the total matches and multiplying by 100
    draw_percent = (draws / total_matches) * 100

    # If the loss percentage is over 50, type_of_wrestler is "Jobber". Otherwise it is "Superstar".
    if loss_percent > 50:
        type_of_wrestler = "Jobber"
    else:
        type_of_wrestler = "Superstar"

    # Print out the wrestler's name and their percentage stats
    print(f"Stats for {name}")
    print(f"WIN PERCENT: {win_percent}")
    print(f"LOSS PERCENT: {loss_percent}")
    print(f"DRAW PERCENT: {draw_percent}")
    print(f"{name} is a {type_of_wrestler}")


# Read in the CSV file
with open('WWE-Data-2016.csv', 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if name_to_check == row[0]:
            print_percentages(row)
            

       
  
#from csv import DictReader
#open file in read mode
#with open(r"C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Resources\budget_data.csv", 'r') as read_obj:
    # pass the file object to Dictreader() to get the reader object
#   csv_dict_reader = DictReader(read_obj)  
        
#   for row in csv_dict_reader:
            # row variable is a dictionary that represents a row in csv
#         print(row['Date'],row['Profit/Losses'])
#         print (row[0])
            

#count = 0
#total = 0
#column

#from csv import DictReader
# open file in read mode
#with open(r"C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Resources\budget_data.csv", 'r') as read_obj:
 
    # pass the file object to Dictreader() to get the reader object
#    csv_dict_reader = DictReader(read_obj) 
#    for row in enumerate(csv_dict_reader):
#            count = count + 1
#print(count)
#    while x < count
#        total = total + int(row['Profit/Losses'])
#        print(total)
        
   
    
  