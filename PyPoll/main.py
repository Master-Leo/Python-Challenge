#Import dependencies
import os
import csv

#Set path
data_path = os.path.join("Resources", "election_data.csv")

#Set variables to calculate and list for votes,percentages,names
total_vote = 0
candidates = []
votes_earned = 0 
list = {}
total_won_votes = 0
winner = " "

#Open and read CSV
with open(data_path) as csv_file:
     csv_reader = csv.reader(csv_file, delimiter=",")
     csv_header = next(csv_file)

     for row in csv_reader:
        #Row count of votes
        total_vote = total_vote + 1

    #Total candidates who recieved votes and votes on for each
        if row[2] not in candidates:
            candidates.append(row[2])
            list[row[2]] = 0
        list[row[2]] = list + 1
#Percentage of votes won
for individual in list:
    votes = votes_earned[individual]
    percentage = votes / total_vote
    total = percentage * 100   

output_one = (
    f"```text\n"
    f"Election Results\n"
    f"-----------------------------\n"
    f"Total Votes: {total_vote}\n"
    f"-----------------------------\n"
)

output_two = (
    f"{individual}: {total:.3f}% ({votes}"
)

output_three = (
    f"-----------------------------\n"
    f"Winner: {winner}\n"
    f"-----------------------------\n"
    f"```/n"
)

print(output_one)
print(output_two)
print(output_three)
