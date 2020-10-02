count = 0
cnd = []
cnewlist =[]

#calculating count, total. Populating the list named chng[]
import csv
import collections
#Find total votes cast, create list cnd[]
with open(r"C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyPoll\Resources\election_data.csv", mode='r') as csv_file:
    pollreader = csv.reader(csv_file)
    header = next(pollreader)   
    for row in pollreader: 
        count = count + 1
        cnd.append(row[2])
# This will produce a dict that looks like Counter({'khan':2218231, ....}). We will use this to create the summary of poll results.
vtpercandidate = collections.Counter(cnd)
#Determine the winner
w = vtpercandidate.most_common(1)[0][0]
#Create results
print("\n")
print("Election Results")
print("---------------------------------")
print("Total Votes: " + str(count))
print("---------------------------------")    
for x in vtpercandidate:
    print(f"{x}:  {(round(((vtpercandidate[x]/count)*100),4))}%  ({vtpercandidate[x]})")
print("---------------------------------")
print("Winner: " + w)
print("---------------------------------")

# writing the output to a text file inside Analysis folder. 
o = open(r'C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyPoll\Analysis\outfile','w')
print("\n")
print("Election Results", file=o)
print("---------------------------------", file=o)
print("Total Votes: " + str(count), file=o)
print("---------------------------------", file=o)
for x in vtpercandidate:
    print(f"{x}:  {(round(((vtpercandidate[x]/count)*100),4))}%  ({vtpercandidate[x]})", file=o)
print("---------------------------------", file=o)
print("Winner: " + w, file=o)
print("---------------------------------", file=o)
print("\n")
print("output to txtfile successful")
o.close()

