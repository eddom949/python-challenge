# Imports
import os,csv

#set the csv filename (no path)
csvpath="election_data.csv"
output_file=os.path.join("election_data.txt")

with open( output_file, "w", newline="", encoding="utf8" ) as data_file:

    candidates = {}
    votelist = []

    # print the header rows
    data_file.write("Election Results\n")
    data_file.write("-" * 15 + "\n")
    
    print("Election Results")
    print("-" * 15)

    #read in the csv file
    with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader( csvfile, delimiter=",")

        numvotes=0

        #skip the header row
        csv_header = next(csvreader)
        #print the total number of votes
        for row in csvreader:
            numvotes = numvotes + 1

        print("Total Votes:  " + str(numvotes) )
        print("-" * 15)
        data_file.write("Total Votes:  " + str(numvotes) + "\n" )
        data_file.write("-" * 15 + "\n")


    with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader( csvfile, delimiter=",")
        
        #skip the header row
        csv_header = next(csvreader)
        for row in csvreader:
            candidates.update( { row[2]: 0} )
            
        #debugging print("Candidates:  " + str(candidates) )
        
        csvfile.seek(0)
        csv_header = next(csvreader)
        for row in csvreader:
            candidates[row[2]] += 1

        # debugging print("Candidates:  " + str(candidates ) )
    winner=""
    winningvotes = 0
    for entry in candidates:
        #old print( entry + ": %5d %2.3f" % (candidates[entry],100*candidates[entry]/numvotes))
        print( entry + ": %2.3f%% (%5d)" % (100*candidates[entry]/numvotes,candidates[entry]))
        data_file.write(entry + ": %2.3f%% (%5d)" % (100*candidates[entry]/numvotes,candidates[entry]) + "\n")
        if candidates[entry] > winningvotes:
            winner = entry
            winningvotes = candidates[entry]
    print("-" * 15 )
    print( "Winner: " + winner )
    print("-" * 15 )
    data_file.write("-" * 15 + "\n")
    data_file.write("Winner: " + winner + "\n")
    data_file.write("-" * 15 + "\n")
    