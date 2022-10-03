#imports
import os
import csv

#create path to PyBank budget data csv file
pybank_file_path = os.path.join("Resources", "budget_data.csv")

#create path to PyPoll election data csv file
pypoll_file_path = os.path.join("Resources", "election_data.csv")

#create path to analysis text file for output
analysis_file_path = os.path.join("Analysis", "Analysis.txt")

#---------------PYBANK PORTION OF CODE-----------------------------

#Read the PyBank budget_data csv file
with open(pybank_file_path) as file:
    pybank_file_contents = csv.reader(file, delimiter=',')

    #Skip header of file using next
    csv_header = next(pybank_file_contents)

    #Variable for counting number of rows in sheet
    number_of_rows = 0

    #List for converting the Profit/Loss column to integer
    profit_loss_list = []

    #List for tracking changes between dates
    profit_change_list = [0]

    #List for all of the dates
    dates_list = []
    
    #Variable for total profit
    total_profit = 0

    #Variable for Average change
    average_change = 0

    #Variables for Greatest Increase
    greatest_increase = 0
    greatest_increase_index = 0

    #Variables for Greatest Decrease
    greatest_decrease = 0
    greatest_decrease_index = 0

    #Loop through all the rows in the csv file
    for row in pybank_file_contents:
        profit_loss_list.append(int(row[1]))
        dates_list.append(str(row[0]))
        number_of_rows += 1
        
    #print out header for output
    print("Financial Analysis")
    print("------------------------------------")

    #print out how many rows (months) there are in the sheet
    print(f"Total Months: {number_of_rows}")
   
    #print out total profit
    total_profit = sum(profit_loss_list)
    print(f"Total: ${total_profit}")

    #Loop through profit_loss_list to create a list of changes between dates
    for i in range(0, number_of_rows - 1):
        profit_change_list.append((profit_loss_list[i+1])-(profit_loss_list[i]))
    
    #Find the average change
    average_change = sum(profit_change_list)/(number_of_rows - 1)
    print(f"Average Change: ${round(average_change,2)}")
        
    #Loop through the profit_change_list to find the greatest increase
    for j in range(0, number_of_rows):
        if (profit_change_list[j] > greatest_increase):
            greatest_increase = profit_change_list[j]
            greatest_increase_index = j

    #Print out the greatest increase
    print(f"Greatest Increase in Profits: {dates_list[greatest_increase_index]} ${greatest_increase}")

     #Loop through the profit_change_list to find the greatest decrease
    for k in range(0, number_of_rows):
        if (profit_change_list[k] < greatest_decrease):
            greatest_decrease = profit_change_list[k]
            greatest_decrease_index = k

    #Print out the greatest decrease
    print(f"Greatest Decrease in Profits: {dates_list[greatest_decrease_index]} ${greatest_decrease}")

    #Add space before PyPoll output
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")



#---------------PYPOLL PORTION OF CODE-----------------------------

#Read the PyPoll budget_data csv file
with open(pypoll_file_path) as secondfile:
    pypoll_file_contents = csv.reader(secondfile, delimiter=',')

    #Skip header of file using next
    csv_header = next(pypoll_file_contents)

    #Variable for counting number of rows in pypoll sheet
    number_of_pypoll_rows = 0

    #List for the candidates
    candidate_list = []

    #List for candidate names
    candidate_names_list = []

    #Variables to track votes for each candidate
    Charles_votes = 0
    Charles_percent = 0
    Diana_votes = 0
    Diana_percent = 0
    Raymon_votes = 0
    Raymon_percent = 0
   
    #Loop through all the rows in the csv file
    for row in pypoll_file_contents:
        candidate_list.append(str(row[2]))
        number_of_pypoll_rows += 1

    print("Election Results")
    print("------------------------------------")
    print(f"Total Votes: {number_of_pypoll_rows}")
    print("------------------------------------")
  
    #Find the number of candidates
    for x in range(0,number_of_pypoll_rows-1):
        if ((candidate_list[x+1] != candidate_list[x]) & (candidate_list[x] not in candidate_names_list)):
            candidate_names_list.append(candidate_list[x])

    #Find number of votes for Charles
    Charles_votes = candidate_list.count('Charles Casper Stockham')
    Charles_percent = (Charles_votes/number_of_pypoll_rows) * 100

    #Find number of votes for Diana
    Diana_votes = candidate_list.count('Diana DeGette')
    Diana_percent = (Diana_votes/number_of_pypoll_rows) * 100

    #Find number of votes for Raymon
    Raymon_votes = candidate_list.count('Raymon Anthony Doane')
    Raymon_percent = (Raymon_votes/number_of_pypoll_rows) * 100

    #print out election results
    print(f"Charles Casper Stockham: {round(Charles_percent,3)}% {Charles_votes}")
    print(f"Diana DeGette: {round(Diana_percent,3)}% {Diana_votes}")
    print(f"Raymon Anthony Doane: {round(Raymon_percent,3)}% {Raymon_votes}")
    print("------------------------------------")

    #Find the winner of the election
    if (Charles_votes > Diana_votes) & (Charles_votes > Raymon_votes):
        winner = "Charles Casper Stockham"
    elif (Diana_votes > Charles_votes) & (Diana_votes > Raymon_votes):
        winner = "Diana DeGette"
    elif (Raymon_votes > Charles_votes) & (Raymon_votes > Diana_votes):
        winner = "Raymon Anthony Doane"

    print(f"Winner: {winner}")

    print("------------------------------------")

    #Write to Analysis.txt output file
with open(analysis_file_path, 'w') as output_file:
    output_file.write("Financial Analysis")
    output_file.write('\n')
    output_file.write("------------------------------------")
    output_file.write('\n')
    output_file.write(f"Total Months: {number_of_rows}")
    output_file.write('\n')
    output_file.write(f"Average Change: ${round(average_change,2)}")
    output_file.write('\n')
    output_file.write(f"Greatest Increase in Profits: {dates_list[greatest_increase_index]} ${greatest_increase}")
    output_file.write('\n')
    output_file.write(f"Greatest Decrease in Profits: {dates_list[greatest_decrease_index]} ${greatest_decrease}")
    output_file.write('\n')
    output_file.write('\n')
    output_file.write('\n')
    output_file.write('\n')
    output_file.write('\n')
    output_file.write("Election Results")
    output_file.write('\n')
    output_file.write("------------------------------------")
    output_file.write('\n')
    output_file.write(f"Total Votes: {number_of_pypoll_rows}")
    output_file.write('\n')
    output_file.write("------------------------------------")
    output_file.write('\n')
    output_file.write(f"Charles Casper Stockham: {round(Charles_percent,3)}% {Charles_votes}")
    output_file.write('\n')
    output_file.write(f"Diana DeGette: {round(Diana_percent,3)}% {Diana_votes}")
    output_file.write('\n')
    output_file.write(f"Raymon Anthony Doane: {round(Raymon_percent,3)}% {Raymon_votes}")
    output_file.write('\n')
    output_file.write("------------------------------------")
    output_file.write('\n')
    output_file.write(f"Winner: {winner}")
    output_file.write('\n')
    output_file.write("------------------------------------")