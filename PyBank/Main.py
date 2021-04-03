#Author: Matt Jensen

#Import dependencies for the OS and for the .csv file
import os
import csv

#Set variables
months = 0
month_number = []
net_PL = 0
change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

#Set path for .csv file
bank_csv = os.path.join( "Resources", "budget_data.csv")

with open( bank_csv) as csvfile:
    csvreader = csv.reader( csvfile, delimiter=',')
    csv_header = next( csvreader)

    #Set baseline row
    first_row = next( csvreader)
    months += 1
    net_PL += int( first_row[1])
    prior_amount = int( first_row[1])

    #Analyze each row of data
    for row in csvreader:
        months += 1  #Count the number of months

        net_PL += int( row[1])  #Sum up the net profit/loss
        
        #Calculate change for each period
        amount = int( row[1]) - prior_amount
        prior_amount = int( row[1])
        change += [amount]
        
        #Find the greatest increase
        if amount > greatest_increase[1]:
            greatest_increase[1] = amount
            greatest_increase[0] = row[0]

        #Find the greatest decrease
        if amount < greatest_decrease[1]:
            greatest_decrease[1] = amount
            greatest_decrease[0] = row[0]

#Find the average change in profit/loss
avg_change = sum( change) / len( change)

#Summary Analysis
results = (
    f"Financial Analysis\n"
    f"--------------------------------------------------\n"
    f"Total Months: {months}\n"
    f"Total: ${net_PL}\n"
    f"Average Change: ${avg_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"
    )

#Print the results to terminal
print( results)

#Export the resultsto text file
results_output = os.path.join( "Resources", "financial_analysis.txt")

with open( results_output, "w") as txt_file:
    txt_file.write( results)