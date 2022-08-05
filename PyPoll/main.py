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
        list[row[2]] += 1


print(f"```text")
print(f"Election Results")
print(f"-----------------------------")
print(f"Total Votes: {total_vote}")
print(f"------------------------------")


#Percentage of votes won
for individual in list:
    votes = list[individual]
    percentage = votes / total_vote
    total = percentage * 100 
    print(f"{individual}: {total:.3f}% ({votes})")


#Winner based on most votes
if votes > total_won_votes:
    total_won_votes = votes
    winner = individual 

print(f"-----------------------------")
print(f"Winner: {winner}")
print(f"-----------------------------")
print(f"```")

output_file = os.path.join("Analysis", "election_Analysis.txt"

with open(output_file, "w") as datafile:
   datafile.write()
   
