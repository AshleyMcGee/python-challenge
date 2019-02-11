import csv
import os
import statistics 

path = os.path.join("second_election_Data_homework.csv")

def pyPoll():
    votes = []

    #Total Votes
    for row in reader:
        votes.append(row[0])
    
    #Candidate list
    col3 = set()
    candidates = []
    
    #Get the candidates, update candidate list
    for row in reader:
        col3.add(row[2])
        candidates = list(col3)
        
    
        
    totalVotes = len(votes)


    
    print("-----------------------------------")
    print("Election Results:")
    print("-----------------------------------")
    print(f"Total Voters: {totalVotes}.")
    print("-----------------------------------")
    print(f"Candidates: \n")
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