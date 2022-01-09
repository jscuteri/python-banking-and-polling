# import the modules
import os
import csv

#file path to the budget data
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

#make sure that is the correct file path/python has found the csv file
print(csvpath)

#designate answer spots/starting spots. Starting spot for total months and net_total_pnl is first row of data since you skip it on line 38-39.

total_votes = 0
unique_candidates = []
candidate_votes = []
election_results = {}

khan_count = 0
correy_count = 0
li_count = 0
otooley_count = 0

khan_percent = 0
correy_percent = 0
li_percent = 0
otooley_percent = 0

winner = []

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

    #print the rest of the rows
    for row in reader:

    #count the number of rows in the csv file (excluding the header)
        total_votes +=1

    #add all the candidates to a list
        candidate_name = row[2]

    #pick out the individual values to avoid repeating
        if candidate_name not in unique_candidates:
            unique_candidates.append(candidate_name) 

    #all vote names
        candidate_votes.append(row[2])
    
    #find the number of votes won for each candidate

    khan_count = candidate_votes.count('Khan')
    correy_count = candidate_votes.count('Correy')
    li_count = candidate_votes.count('Li')
    otooley_count = candidate_votes.count("O'Tooley")

    #votes won by candidate / total number of votes

    khan_percent = khan_count / total_votes
    correy_percent = correy_count / total_votes
    li_percent = li_count / total_votes
    otooley_percent = otooley_count / total_votes

    #format percentages

    khan_format = "{:.4%}".format(khan_percent)
    correy_format = "{:.4%}".format(correy_percent)
    li_format = "{:.4%}".format(li_percent)
    otooley_format = "{:.4%}".format(otooley_percent)

    #bring it into election results dictionary

    election_results = {
        f"Khan: {khan_format}" : f"({khan_count})",
        f"Correy: {correy_format}" : f"({correy_count})",
        f"Li: {li_format}" : f"({li_count})",
        f"O'Tooley: {otooley_format}" : f"({otooley_count})",
    }

    #winner

    if khan_count > correy_count or li_count or otooley_count:
        winner = "Khan"
    elif correy_count > khan_count or li_count or otooley_count:
        winner = "Correy"
    elif li_count > khan_count or correy_count or otooley_count:
        winner = "Li"
    else:
        winner = "O'Tooley"

#Election Results to txt file

#file path for where we are saving the txt file
output_path = os.path.join("analysis")

#export final results to txt
with open(output_path, 'w') as txt_file:
    txt_file.write(
        f"Election Results"'\n'
        f"-------------------------"'\n'
        f"Total Votes: {total_votes}"'\n'
        f"-------------------------"'\n'
        f"{election_results}"'\n'
        f"-------------------------"'\n'
        f"Winner: {winner}"'\n'
        f"-------------------------"'\n'
        )

#Election Results to Terminal

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
print(election_results)
print("-------------------------")
print("Winner: " + str(winner))
print("-------------------------")