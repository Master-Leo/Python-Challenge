#Import dependecies 
import os 
import csv

#Set path
budget_file_path = os.path.join("Resources", "budget_data.csv")

#Define Variables

month = []
profits = []
difference = []

mouth_count = 0
net_total = 0
average_change = 0
prev_profit = 0
total_difference = 0

greatest_profit = 0
least_profit = 0
greatest_month = " "
least_month = " "

#Open CSV reader with header
with open(budget_file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")




