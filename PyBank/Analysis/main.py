# import the modules
import os
import csv

#file path to the budget data
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#make sure that is the correct file path/python has found the csv file
print(csvpath)

#leave answer spots open
total_months = 0
net_total_pnl = 0
all_monthly_change = []
months_list = []
average_pnl_mom = []
greatest_increase = ["",0]
greatest_decrease = ["",1000000000]

#open the csv and rename it as csvfile
with open(csvpath) as csvfile:
    
    #open the csv by breaking up the delimiter
    reader = csv.reader(csvfile)

    #print the csv file name. This will basically be gibberish but that's ok. At least we found the file. 
    print(reader)

    #start breaking out the data in the file
    #read the header row
    csv_header = next(reader)

    #print the header row
    print(f"CSV Header Row: {csv_header}")

    csv_first_row = next(reader)
    csv_first_row_value = int(csv_first_row[1])

    total_months +=1

    #print the rest of the rows
    for row in reader:

    #count the number of rows in the csv file (excluding the header since we are in the forloop that skipped the header) Position 1 is in the index position of each row
        total_months +=1
       

    #sum the total pnl for each row, index position 1
        net_total_pnl += int(row[1])
        
### Code works up to this point ###  

        monthly_change = int(row[1]) - csv_first_row_value
        csv_first_row_value = int(row[1])

        all_monthly_change += [monthly_change] 

        months_list += [row[0]]

        if monthly_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = monthly_change

        if monthly_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = monthly_change

print(months_list)
print(all_monthly_change)

print(total_months)
print(net_total_pnl)
print(greatest_increase)
print(greatest_decrease)