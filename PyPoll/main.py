count = 0
cnd = []
cnewlist =[]

#calculating count, total. Populating the list named chng[]
import os
import csv
import collections
import operator
from collections import Counter, OrderedDict
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
vtpercandidate = Counter(cnd)
#print(vtpercandidate)
#This is the summary of poll results***
for x in vtpercandidate:
    print(f"{x}:  {(round(((vtpercandidate[x]/count)*100),4))}%  ({vtpercandidate[x]})")


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
for x in vtpercandidate:
    print(f"{x}:  {(round(((vtpercandidate[x]/count)*100),4))}%  ({vtpercandidate[x]})", file=o)
print("---------------------------------", file=o)
print("Winner: " + x[0], file=o)
print("---------------------------------", file=o)
print("output to txtfile successful")
o.close()

