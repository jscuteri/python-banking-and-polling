# import the modules
import os
import csv

#file path to the budget data
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#make sure that is the correct file path/python has found the csv file
print(csvpath)

#open the csv and rename it as csvfile
with open(csvpath) as csvfile:
    
    #open the csv by breaking up the delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    #print the csv file name. This will basically be gibberish but that's ok. At least we found the file. 
    print(csvreader)

    #start breaking out the data in the file
    #read the header row
    csv_header = next(csvreader)

    #print the header row
    print(f"CSV Header Row: {csv_header}")

    #set the number of rows to 0
    num_rows = 0

    #set total pnl to 0
    total_pnl = 0

    #print the rest of the rows
    for month in csvreader:
        print(month[0])
        dates = month[0]
print("break")
print(dates)
    #Month i+1 Value - Month i Value = month over month change
        #mom_change = int(rows[1]+1) - int(rows[1])

## Put each the month over month change using the append
## average out your list

#add to the end of the for loop (ANSWERS)
    #print the number of rows (excluding the header)
    #print(num_rows)
    #print(total_pnl)

#min/max for last two parts of the question

#final result variables
#total_pnl = [] etc...