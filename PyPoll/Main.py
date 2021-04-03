# Author: Matt Jensen
# Importing dependencies for OS and for .csv files
import os
import csv

# Set variables
candidates = []
vote_count = []
vote_percent = []
total_votes = 0

# Path for .csv file
data_path = os.path.join( 'Resources', "election_data.csv")

# Open/read .csv file
with open( data_path, newline = "") as csvfile:
    csvreader = csv.reader( csvfile, delimiter = ",")
    csv_header = next( csvreader)

    for row in csvreader:

        # Compile candidate list and add votes to each candidate
        total_votes += 1
        if row[2] not in candidates:
            candidates.append( row[2])
            candidate_index = candidates.index( row[2])
            vote_count.append(1)

        else:
            candidate_index = candidates.index( row[2])
            vote_count[ candidate_index] += 1

    # Calculate vote percentages
    for votes in vote_count:
        percentage = "{:.3%}".format( votes / total_votes)
        vote_percent.append( percentage)

    # Find the winning candidate
    winner = max( vote_count)
    candidate_index = vote_count.index( winner)
    winning_candidate = candidates[ candidate_index]

# Compile the election results
results = []

results.append( "Election Results\n-------------------------")
results.append( f"\nTotal Votes: {total_votes}\n-------------------------")
for x in range( len( candidates)):
    results.append( f"\n{candidates[x]}: {vote_percent[x]} ({vote_count[x]})")
results.append( "\n-------------------------\n")
results.append( f"Winner: {winning_candidate}\n-------------------------")

# Print the election results
print( *results)

# Export the results to text file
results_output = os.path.join( "Election_Results.txt")

with open( results_output, "w") as txt_file:
    for result in results:
        txt_file.write( result)