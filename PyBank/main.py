import csv
import os
import math

path = os.path.join("profit_loss.csv")

def pyBank():
    #count of all rows minus the header
    totalMonths = len(list(reader))
    #sum of the row values of "Profit/Loss"
    netIncome = 0
    netIncome += int(row[1])
    #Average change over the course of 86 months
    avgChange = netIncome / totalMonths
    #Maximum increase in profits
    maxChange = max(netIncome)
    #Minimum decrease in profits

    #Print statements to the console and text file
    print("-----------------------------------")
    print("Financial Analysis")
    print("-----------------------------------")
    print(f"Total Months: {totalMonths}.")
    print(f"Total: ${netIncome}.")
    print(f"Average Change: ${avgChange}.")
    print(maxChange)


with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    next(reader)
    for row in reader:
        pyBank()
