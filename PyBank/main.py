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

#Add count for total months 
    for row in csv_reder:
        month_count = month_count + 1
        net_total = net_total + int(row[1])

#Append rows for Total amount of Profit/Loses in dataset
    month.append(row[0])
    total = int(row[1])
    profits.append(total)

#Calculate Profit/Loses changes in dataset 
    changes = 0 
    if prev_profit != 0:
        changes = total - prev_profit
        difference.append(changes)
    prev_profit = total

    