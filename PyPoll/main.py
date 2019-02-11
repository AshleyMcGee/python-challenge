import csv
import os
import statistics 

path = os.path.join("election_data.csv")

def pyPoll():
    voters = []
    candidates = []
    #Total Votes
    for row in reader:
        voters.append(row[0])
        
    
    totalVotes = len(voters)


    
    print("-----------------------------------")
    print("Election Results:")
    print("-----------------------------------")
    print(f"Total Voters: {totalVotes}.")
    print("-----------------------------------")
    print(f"Candidates: ")
    print("-----------------------------------")
    print(f"Winner: ")
    print(f"----------------------------------")

    #with open("PyBankFinal.txt", "w") as file:
        #file.write("-----------------------------------\n")
        #file.write("\n")
        #file.write("-----------------------------------\n")
        #file.write(f"\n")
        #file.write(f"\n")
        #file.write(f"\n")
        #file.write(f".\n")
        #file.write(f"\n")
        #file.write("-----------------------------------\n")


with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    header = next(reader)
    for row in reader:
        pyPoll()