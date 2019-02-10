import csv
import os
import statistics

path = os.path.join("profit_loss.csv")

def pyBank():
    #For loop for totalMonths and netIncome
    profitLoss = []
    for row in reader:
        profitLoss.append(int(row[1]))

    #totalMonths
    totalMonths = len(profitLoss)+1

    #netIncome
    netIncome = sum(profitLoss)

    #For loop 
    for row in reader:


    #Average Increase
    #averageChange = netIncome / totalMonths
    #averageChange = []
    #for i in profitLoss:
        #monthOverMonth = lambda: row[i] + 1
        #averageChange.append(monthOverMonth)

    #average = statistics.mean(averageChange)
    
    #Maximum Change
    maximumIncrease = max(profitLoss)

    #Maximum Profit Loss
    maximumDecrease = min(profitLoss)

    #Print statements to the console and text file
    print("-----------------------------------")
    print("Financial Analysis")
    print("-----------------------------------")
    print(f"Total Months: {totalMonths}.")
    print(f"Total: ${netIncome}.")
    #print(f"Average Change: ${round(average, 2)}.")
    print(f"Maximum Increase in Profits: ${maximumIncrease}.")
    print(f"Minimum Decrease in Profits: ${maximumDecrease}.")
    print("-----------------------------------")


with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    next(reader)
    for row in reader:
        pyBank()

    
