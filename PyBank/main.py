# -*- coding: UTF-8 -*-
"""PyBank Homework Solution."""

# Dependencies
import csv
import os

# load this file
file_to_load = ("budget_data.csv")

# output text onto this file
file_to_output = ("budget_output.txt")


# Track various financial parameters
#The total number of months included in the dataset
total_months = -1

# The net total amount of "Profit/Losses" over the entire period
total_net = 0

#Set a list for greatest increase [month, how much]
greatest_increase = ["",0]

#set a list for the greatest decrease [month, how much]
greatest_decrease = ["", 0]

#set total difference 
tot_difference = 0


#read the csv and convert it into a list of dictionaries 
with open(file_to_load) as data:
    financial_months = csv.reader(data, delimiter = ',')
    header = next(financial_months)
    prev = 867884

    for i in financial_months:
        total_months += 1
        total_net += int(i[1])
    
        difference = int(i[1])-prev

        if difference >= int(greatest_increase[1]):
            greatest_increase = [i[0], difference]

        if difference < int(greatest_decrease[1]):
            greatest_decrease = [i[0], difference]
        
        prev = int(i[1])
        tot_difference += difference

    ave_net = tot_difference / total_months
output = (f'\nFinancial Analysis\n'
f'---------------------------------\n'
f'Total months: {total_months}\n'
f'Total: {total_net}\n'
f'Average change: {ave_net:.2f}\n'
f'Greatest increase in profits: {greatest_increase[0]} {greatest_increase[1]}\n'
f'Greatest decrease in losses: {greatest_decrease[0]} {greatest_decrease[1]}\n')

print(output)
 
with open(file_to_output,"w") as file_txt:
    file_txt.write(output)