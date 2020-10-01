# python-challenge
Python challeges using budget_data.csv and election_data.csv are complete.

PyBank:
I have 2 solutions out of which main-v2.py is the one I like. Here, I find the differences in profit/losses and append to a list. Then use the list index to locate the greatest and lowest increase. Use that index to write the date and the difference to the output file. 

In the main.py, the approach is to create a new budget_data_1.csv with 3 columns titled: Date, Profit/Losses, Difference. The third column is constructed using a list called chng[] by find the differences in the profit/losses. I have 2 functions that return only the Date and Difference from the new csv. I then read the results and export to output file. 

PyPoll:
I imported the Collections module and used the Counter to find candidates with their votes. I used the most_common() function to determine the winner. I used the reader module and iterated to find the total number of votes cast. The results are written to a text file in the required format. 
