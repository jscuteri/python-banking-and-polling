# import the modules
import os
import csv

#file path to the budget data
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#make sure that is the correct file path/python has found the csv file
print(csvpath)

#leave answer spots open
total_months = []
net_total_pnl = []
average_pnl_mom = []
greatest_increase = []
greatest_decrease = []

#what do you need to calculate these things? Add to this list as you run through your program. 

month = ["January", "February", "March", "April" , "May", "June", "July", "August", "September", "October", "November", "December"]

#setting your calculations to 0
num_rows = 0
total_pnl = 0

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

    #print the rest of the rows
    for rows in csvreader:
        print(rows)

    #count the number of rows in the csv file (excluding the header since we are in the forloop that skipped the header) Position 1 is in the index position of each row
        num_rows +=1
        total_months = num_rows
       

    #sum the total pnl for each row, index position 1
        total_pnl += int(rows[1])
        net_total_pnl = total_pnl
        

### Code works up to this point ###  

    #conditional --> if previous month <> next month, then do some math
    #    for i in month:
    #        if str(i) != str(i-1):
     #           print("Not equal")


#output section
print(total_months)
print(net_total_pnl)

#Month i+1 Value - Month i Value = month over month change
#mom_change = int(rows[1]+1) - int(rows[1])

## Put each the month over month change using the append
## average out your list

#min/max for last two parts of the question