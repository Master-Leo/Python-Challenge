#Import dependencies
import os
import csv


#Set path
data_path = os.path.join("Resources", "election_data.csv")

output_file = os.path.join("Analysis", "election_Analysis.txt")

#Set variables to calculate and list for votes,percentages,names
total_vote = 0
candidates = ""

list = {}

votes_won = 0
winner = ""

#Open and read CSV
with open(data_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

    for row in csv_reader:
        #Row count of votes
        total_vote = total_vote + 1

    #Total candidates who recieved votes and votes on for each
        candidates = row[2]
        if candidates in list:
            list[candidates] += 1
        else:
            list[candidates] = 1

print(f"```text")
print(f"Election Results")
print(f"-----------------------------")
print(f"Total Votes: {total_vote}")
print(f"------------------------------")

output = (
    f"```text\n"
    f"Election Results\n"
    f"-----------------------------\n"
    f"Total Votes: {total_vote}\n"
    f"------------------------------\n"
)

with open(output_file, "w") as datafile:
    datafile.write(output)

#Percentage of votes won
for individual in list:
    percentage = (list[candidates]/total_vote)*100

    print(f"{individual}: {percentage:.3f}% ({list[candidates]})\n")

    output_two = (f"{individual}: {percentage:.3f}% ({[candidates]})\n")

    #Winner based on most votes
    if list[candidates] > votes_won:
        votes_wone = list[candidates]
        winner = candidates 

    with open(output_file, "a") as datafile:
        datafile.write(output_two)


output_three = (
    f"-----------------------------\n"
    f"Winner: {winner}\n"
    f"-----------------------------\n"
    f"```\n"
)
print(output_three)

with open(output_file, "a") as datafile:
    datafile.write(output_three)