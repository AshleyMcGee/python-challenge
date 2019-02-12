import csv
import os
import statistics

path = os.path.join("profit_loss.csv")

def pyBank(reader):
    #For loop for totalMonths and netIncome
    records = []

    for row in reader:
        record = {'date': row[0], 'profit_loss': int(row[1])}
        records.append(record)

    #total months
    totalMonths = len(records)

    #netIncome
    netIncome = sum([record['profit_loss'] for record in records])

    #Average Change
    startValue = records[0]['profit_loss']
    endValue = records[-1]['profit_loss']
    averageChange = (endValue - startValue) / (len(records) - 1)

    #Maximum and Minimum Deltas
    previous_value = records[0]['profit_loss']
    largest_delta = 0
    smallest_delta = 0

    for record in records:
        date = record['date']
        value = record['profit_loss']

        delta = value - previous_value
        if delta > largest_delta:
            largest_delta = delta
        elif delta < smallest_delta:
            smallest_delta = delta
        
        if largest_delta == delta:
            monthLargestDelta = date
        elif smallest_delta == delta:
            monthSmallestDelta = date        

        previous_value = value
  
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
    next(reader) # skip header
    pyBank(reader)


    
