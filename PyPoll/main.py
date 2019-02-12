import csv
import os

path = os.path.join("second_election_Data_homework.csv")

def pyPoll(reader):

    #file handling
    #lists to store data
    records = []
    #col3 = set()
    #candidates = []
    candidatesResults = []

    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter = ",")
        header = next(reader)

        #Go through the csv
        for row in reader:
            #For every row in reader, create a dictionary of every record.
            record = {'Voter ID': row[0], 'County': (row[1]), 'Candidate': row[2]}
            #For every record, append it to the list of records
            records.append(record)

            #This is the total number of votes cast in the election.
            totalVotes = len(records)

            #List of Candidates
            #col3.add(record['Candidate'])
            #candidates = list(col3)

            #This is the starting value for total votes per candidate
            totalCandidateVotes = 0

            #This will tally up the occurences of each candidate name in the records
            name = record['Candidate']

            if record['Candidate'] == "Li":
                totalCandidateVotes +1

            #This is the percentage of votes per candidate of the whole
            percentOfWhole = round((totalCandidateVotes / totalVotes) * 100, 3)

            #Add each candidate dictionary to the list of candidate results
        candidateStats = {'Name':name, 'Percentage':percentOfWhole, 'Total Votes': totalCandidateVotes}
        candidatesResults.append(candidateStats)


    print(totalVotes)
    print(candidatesResults)

    #print("------------------------------")
    #print("Election Results")
    #print("------------------------------")
    #print(f"Total Votes: {totalVotes}.")
    #print("------------------------------")
    #print("Name: " + candidatesResults[0]['Name'] + " " + str(candidatesResults[0]['Percentage']) + " (" + str(candidatesResults[0]['Total Votes']) + ")")
    #print(f"{candidatesResults[1]}")
    #print(f"{candidatesResults[2]}")
    #print("------------------------------")
    #print(f"Winner: ")


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
        pyPoll(reader)