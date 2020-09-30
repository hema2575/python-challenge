count = 0
cnd = []
cnewlist =[]
#calculating count, total. Populating the list named chng[]
import os
import csv
from collections import Counter
#create the results
with open(r"C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyPoll\Resources\election_data.csv", mode='r') as csv_file:
    pollreader = csv.reader(csv_file)
    header = next(pollreader)   
    for row in pollreader: 
        count = count + 1
        cnd.append(row[2])
#print(count)


#Create a key-value pair of cset, the dict. Key = cset,Value= total number of votes 
#This is the list created out of row[2] which is candidates
#print(cnd)
#using set to get a dictionary of unique candidates
cset = set(cnd)
#print(cset) 
#Converting the dictionary of unique candidates to a list
cnewlist = list(cset)
#print(cnewlist)
# This will produce a dict that looks like Counter({'khan':2218231, ....})
countofeachcandidate = Counter(cnd)
#print(countofeachcandidate)

#creating an accessible list out of the list cnd

    
#k = countofeachcandidate.most_common()
#print(k)

#print(k[0])
#print(k[1])

#This is another way to find distinct candidates       
#def unique(candidateslist): 
    # intilize a null list intended to be unique list
#    cndte = [] 
     
    # traverse for all elements 
#    for x in candidateslist: 
        # check if exists in the unique list or not 
#        if x not in cndte:
#            cndte.append(x)
#    print(cndte)

#unique(cnd)  



# writing the output to a text file inside Analysis folder. 
o = open(r'C:\Users\muthukumar\Desktop\02_SaveNWBCSHere\03_Activities&HW\Week3\python-challenge\PyPoll\Analysis\outfile','w')

print("Election Results", file=o)
print("---------------------------------", file=o)
print("Total Votes: " + str(count), file=o)
print("---------------------------------", file=o)
cnd1 = cnewlist
for cand in cnd1:
    print(cand, countofeachcandidate[cand], file=o )
o.close()

