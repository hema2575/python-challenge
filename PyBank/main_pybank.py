count = 0
total = 0
chng = []
change = 867884
change1 = 0
change2 = 0
change3 = 0
# create a new file with columns Date, Profit/Losses, Change. Use Udemyzip as example. 
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
#        row.append(chng)
#print(row) -- I am trying to append this list to row of reader. Like row[0] is date row[1] is profit/losses, row[2] is chng

#Trying something like this. can I print the month if I get output in this format?
#updatedfile = zip(Date, prls, chng)
#print(tuple(updatedfile))
        
#print(chng)--- this prints out the new list chng[]


#This function takes in a list, i.e row which has 2 columns and adds the 3rd
# column 'chng'

def transform_row(list):
    row.append(list)
    
def add_clmn_to_csv(inputfile, outputfile,transform_row):
    with open(r"C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Resources\budget_data.csv", mode='r') as read_obj, \
        open(r"C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Resources\budget_data_v1.csv", mode='w', newline='') as write_obj:
            reader = csv.reader(read_obj)
            header = next(reader)
            writer = csv.writer(write_obj)
            for row in reader:
                transform_row(row, reader.line_num)
                writer.writerow(row)


#def transform_row(change, change1):
        #    change = 867884 for this budget data
        #    change1 = 0 for this budget data
#        for row in reader: 
#            change = int(row[1]) - change + change1
#            change1 = change - int(row[1])
#            chng.append(change)
#           print(chng)
    
       

def add_clmn(infile, outfile, updt_row, update_column_names):
    with open(r"C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Resources\budget_data.csv", mode='r') as read_obj, \
        open(r"C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyBank\Resources\budget_data_v1.csv", mode='w', newline='') as write_obj:
            dict_reader = DictReader(read_obj)
            column_names = dict_reader.fieldnames
            update_column_names(column_names)
            dict_writer = DictWriter(write_obj, column_names)
            dict_writer.writeheader()
            # Read each row of the input csv file as list
            for row in dict_reader:
                # Modify the dictionary / row by passing it to the transform function (the callback)
                transform_row(row, dict_reader_reader.line_num)
                # Write the updated dictionary/row to the output file
                dict_writer.writerow(row)
add_clmn(infile, outfile, updt_row, update_column_names)    


#print(len(row[0])) --- this prints out 8. how?
#print(len(row)) --- this just means there are 2 columns in the row
#print(chng)
#print(min(chng))
#print(max(chng))
         
# I have to update this script to write the months against the grt inc, dec in profits. My thinking
# is to write a column using chng[] to the original file. then using the index of these values to
# find the corresponding months. Need help here!!
            

print("Financial Analysis")
print("---------------------------------")
print("Total Months: " + str(count))
print("Total: " + str(total))          
print("Average Change: " + str((change2/(len(chng)-1), 2)))
print("Greatest Increase in Profits: " + str(max(chng)))
print("Greatest Decrease in Profits: " + str(min(chng)))

python main_pybank.py >> text.log

# Read in the new CSV file, find the grtPrfInc, grpPrfDec
with open(r"C:...budget_data_1.csv", mode='r') as csvfile:
    # Split the data on commas
    bd_1reader = csv.reader(csvfile, delimiter=',')
    header = next(bd_1reader)
    # Loop through the data
    for row in bd_1reader:
        # If max(chng), min(chng) are in row[2] is equal to that which the user input, run the 'print_percentages()' function
        if max == row[2]:
            print(row)
        if min == row[2]:
            print(row)
