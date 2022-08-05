#Import dependecies 
import os 
import csv

#Set path
budget_file_path = os.path.join("Resources", "budget_data.csv")

#Define Variables
month = []
change = []
difference = []

month_count = 0
changes = 0 
net_total = 0
average_change = 0
prev_profit = 0

greatest_profit = 0 
greatest_month = " "
least_profit = 0
least_month = " "

#Open CSV reader with header
with open(budget_file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)

#Add count for total months 
    for row in csv_reader:
        month_count = month_count + 1
        net_total = net_total + int(row[1])

#Append rows for Total amount of profit/losses in dataset
        month.append(row[0])
        total = int(row[1])
        change.append(total)

#Append profit/losses changes in dataset 
        if prev_profit != 0:
            changes = total - prev_profit
            difference.append(changes)
        prev_profit = total

#Calculate and locate greatest increase/decrease profits + date when occured
        if changes > greatest_profit:
            greatest_profit = changes
            greatest_month = row[0]
    
        if changes < least_profit:
            least_profit = changes
            least_month = row[0]
            
    average_change = sum(difference)/ len(difference)

terminal_output = (
    f"```text\n"
    f"Financial Analysis\n"
    f"-----------------------------\n"
    f"Total Months: {month_count}\n"
    f"Total: ${net_total}\n"
    f"Average Changes: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_month} ($ {greatest_profit})\n"
    f"Greatest Decrease in Profits: {least_month} ($ {least_profit})\n"
    f"```\n"
)

print(terminal_output)

output_file = os.path.join("Analysis", "budget_analysis.txt")

with open(output_file, "w") as datafile:
   datafile.write(terminal_output)
