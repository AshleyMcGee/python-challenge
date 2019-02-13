import csv
import os
import statistics

path = os.path.join("second_election_Data_homework.csv")

def pyPoll():

    records = []

    c1 = {'Name': 'Li', 'Votes': 0}
    c2 = {'Name': 'Khan', 'Votes': 0}
    c3 = {'Name': "O'Tooley", 'Votes': 0}
    c4 = {'Name': 'Correy', 'Votes': 0}

    candidates = [c1,c2,c3,c4]

    #File handling
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter = ",")
        header = next(reader)

        #Loop through file and assign all records to a dictionary
        for row in reader:
            record = {'Voter ID': row[0], 'County': (row[1]), 'Candidate': row[2]}
            #Append to records list
            records.append(record)
            #Take the total votes as the length of records
            totalVotes = len(records)

            #Loop through the candidates and check if the candidate name matches 
            for candidate in candidates:
                if candidate['Name'] == row[2]:
                    #Update the candidate total votes in their respective dictionaries
                    candidate['Votes'] += 1

            #Candidate percentages
            li_percent = "{:.3%}".format(c1['Votes'] / totalVotes)
            khan_percent = "{:.3%}".format(c2['Votes'] / totalVotes)
            correy_percent = "{:.3%}".format(c4['Votes'] / totalVotes)
            otooley_percent = "{:.3%}".format(c3['Votes'] / totalVotes)
            
            #Find the Winner
            winner = max(candidates, key=lambda x:x['Votes'])
            
    print("------------------------------")
    print("Election Results")
    print("------------------------------")
    print(f"Total Votes: {totalVotes}.")
    print("------------------------------")
    print(f"Name: {c2['Name']} {khan_percent} ({c2['Votes']})")
    print(f"Name: {c4['Name']} {correy_percent} ({c4['Votes']})")
    print(f"Name: {c1['Name']} {li_percent} ({c1['Votes']})")
    print(f"Name: {c3['Name']} {otooley_percent} ({c3['Votes']})")
    print("------------------------------")
    print('Winner: {Name}'.format(**winner))
    print("------------------------------")


    with open("PyPollFinal2.txt", "w") as file:
        file.write("-----------------------------------\n")
        file.write("Election Results\n")
        file.write("-----------------------------------\n")
        file.write(f"Total Votes: {totalVotes}.\n")
        file.write(f"Name: {c2['Name']} {khan_percent} ({c2['Votes']})\n")
        file.write(f"Name: {c4['Name']} {correy_percent} ({c4['Votes']})\n")
        file.write(f"Name: {c1['Name']} {li_percent} ({c1['Votes']})\n")
        file.write(f"Name: {c3['Name']} {otooley_percent} ({c3['Votes']})\n")
        file.write("-------------------------------------\n")
        file.write('Winner: {Name}\n'.format(**winner))
        file.write("-----------------------------------\n")


pyPoll()


