# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join(r"C:\Users\fjrui\OneDrive\Documents\Desktop\Bootcamp\Assignment\module3\Starter_Code\PyBank\Resources\budget_data.csv")  # Input file path
file_to_output = os.path.join(r"C:\Users\fjrui\OneDrive\Documents\Desktop\Bootcamp\Assignment\module3\Starter_Code\PyBank\analysis\budget_data.txt.")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
change_total = 0
dates = []
profit = []

# Open and read the csv
with open(file_to_load) as financial_data:
    csvreader = csv.reader(financial_data, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    # Extract first row to initialize variables
    first_row = next(csvreader)
    total_months = 1
    total_net += int(first_row[1])
    value = int(first_row[1])
    dates.append(first_row[0])
    profit.append(0)  # Change in profit for the first month is 0

    # Track the total and net change
    for row in csvreader:
        total_months += 1
        dates.append(row[0])
        total_net += int(row[1])
        change_total = int(row[1]) - value
        profit.append(change_total)
        value = int(row[1])  # Update value for the next row

    # Calculate the greatest increase in profits (month and amount)
    greatest_increase = max(profit)
    greatest_index = profit.index(greatest_increase)
    greatest_date = dates[greatest_index]

    # Calculate the greatest decrease in losses (month and amount)
    greatest_decrease = min(profit)
    lowest_index = profit.index(greatest_decrease)
    lowest_date = dates[lowest_index]

# Calculate the average net change across the months
average_change = sum(profit[1:]) / len(profit)-1

# Generate the output summary
output_lines = [
    "Financial Analysis",
    "---------------------",
    f"Total Months: {total_months}",
    f"Total: ${total_net}",
    f"Average Change: ${round(average_change, 2)}",
    f"Greatest Increase in Profits: {greatest_date} (${greatest_increase})",
    f"Greatest Decrease in Profits: {lowest_date} (${greatest_decrease})"
]

# Print the output
for line in output_lines:
    print(line)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    for line in output_lines:
        txt_file.write(line + "\n")