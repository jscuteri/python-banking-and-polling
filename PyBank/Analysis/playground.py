# import the modules
import os
import csv

#file path to the budget data
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#make sure that is the correct file path/python has found the csv file
print(csvpath)

#designate answer spots/starting spots. Starting spot for total months and net_total_pnl is first row of data since you skip it on line 38-39.
# @Madison - is there a way to clean this up so I can start at 0 for both total months and net total pnl?
total_months = 1
net_total_pnl = 867884
all_monthly_change = []
months_list = []
average_pnl_mom = []
greatest_increase = ["",0]
greatest_decrease = ["",1000000000]

#open the csv and rename it as csvfile
with open(csvpath) as csvfile:
    
    #read the csv file
    reader = csv.reader(csvfile, delimiter=',')

    #print the csv file name. This will basically be gibberish but that's ok. At least we found the file. 
    print(reader)

    #start breaking out the data in the file
    #read the header row
    csv_header = next(reader)

    #print the header row
    print(f"CSV Header Row: {csv_header}")

    #get to the next row in order to set up your monthly net change
    csv_first_row = next(reader)
    csv_first_row_value = int(csv_first_row[1])

    #print the rest of the rows
    for row in reader:

    #count the number of rows in the csv file (excluding the header and first row of data)
        total_months +=1
       

    #sum the total pnl for each row (excluding header and first row of data)
        net_total_pnl += int(row[1]) 

    #set up the equation for next row minus previous row. This gives you the net change per period
        monthly_change = int(row[1]) - csv_first_row_value
        csv_first_row_value = int(row[1])

    #add each monthly change to the list
        all_monthly_change += [monthly_change] 

    #add each month to the list
        months_list += [row[0]]

    #if the monthly change is greater than 0, give me the applicable month and value
        if monthly_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = monthly_change

    #if the monthly change is less than 1000000000, give me the applicable month and value
        if monthly_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = monthly_change

    #average the monthly changes
        average = sum(all_monthly_change) / len(all_monthly_change)

#file path for where we are saving the txt file
output_path = os.path.join("analysis")

#export final results to txt
with open(output_path, 'w') as txt_file:
    txt_file.write(
        f"Financial Analysis"'\n'
        f"----------------------------"'\n'
        f"Total Months: {total_months}"'\n'
        f"Total: {net_total_pnl}"'\n'
        f"Average Change: {round(average,2)}"'\n'
        f"Greatest Increase in Profits: {greatest_increase}"'\n'
        f"Greatest Decrease in Profits: {greatest_decrease}"'\n'
        )

#print final results results in terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: " + str(net_total_pnl))
print("Average Change: " + str(round(average,2)))
print("Greatest Increase in Profits: " + str(greatest_increase))
print("Greatest Decrease in Profits: " + str(greatest_decrease))
