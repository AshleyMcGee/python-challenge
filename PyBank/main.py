import csv
import os
import statistics

path = os.path.join("profit_loss.csv")
    
def pyBank():
    #For loop for totalMonths and netIncome
    profitLoss = []

    for row in reader:
        profitLoss.append(int(row[1]))

    #total months
    totalMonths = len(profitLoss)

    #netIncome
    netIncome = sum(profitLoss)

    #Average Change
    startValue = profitLoss[0]
    endValue = profitLoss[-1]
    averageChange = (endValue - startValue) / (len(profitLoss) - 1)

    #Maximum and Minimum Deltas
    previous_value = profitLoss[0]
    largest_delta = 0
    smallest_delta = 0

    for i in profitLoss:
        delta = i - previous_value
        if delta > largest_delta:
            largest_delta = delta

        elif delta < smallest_delta:
            smallest_delta = delta
        
        if largest_delta == delta:
            monthLargestDelta = row[0]
        
        elif smallest_delta == delta:
            monthSmallestDelta = row[0]
        
        previous_value = i
  
    #Print statements to the console and text file
    print("-----------------------------------")
    print("Financial Analysis")
    print("-----------------------------------")
    print(f"Total Months: {totalMonths}.")
    print(f"Total: ${netIncome}.")
    print(f"Average Change: ${round(averageChange,2)}.")
    #So close! It's taking the last month of the csv!
    print(f"Greatest Increase in Profits: {monthLargestDelta} ${largest_delta}.")
    print(f"Greatest Decrease in Profits: {monthSmallestDelta} ${smallest_delta}.")
    print("-----------------------------------")


    with open("PyBankFinal.txt", "w") as file:
        file.write("-----------------------------------\n")
        file.write("Financial Analysis\n")
        file.write("-----------------------------------\n")
        file.write(f"Total Months: {totalMonths}.\n")
        file.write(f"Total: ${netIncome}.\n")
        file.write(f"Average Change: ${round(averageChange,2)}.\n")
        file.write(f"Greatest Increase in Profits: {monthLargestDelta}: ${largest_delta}.\n")
        file.write(f"Greatest Decrease in Profits: {monthSmallestDelta}: ${smallest_delta}.\n")
        file.write("-----------------------------------\n")




with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    #next(reader)
    for row in reader:
        pyBank()


    
