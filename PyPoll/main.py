#Import dependencies
import os
import csv

#Set path
data_path = os.path.join("Resources", "election_data.csv")

#Set variables to calculate for votes and names
total_vote = 0
candidates = ""

#Declare final values of candidates in dictionary 
list = {}

#Declare values to set winner values
won_votes = 0
winner = " "

#Open and read CSV
with open(data_path) as csv_file:
     csv_reader = csv.reader(csv_file, delimiter=",")
     csv_header = next(csv_file)
