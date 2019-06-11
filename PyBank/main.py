# Imports
import os,csv

#set the csv filename (no path)
csvpath="budget_data.csv"
output_file=os.path.join("budget_data.txt")

with open( output_file, "w", newline="", encoding="utf8" ) as data_file:

    # print the header rows
    data_file.write("Financial Analysis\n")
    data_file.write("-" * 15 + "\n")
    
    print("Financial Analysis")
    print("-" * 15)

    #read in the csv file
    with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader( csvfile, delimiter=",")

        monthname = ""
        nummonths = 0

        #skip the header row
        csv_header = next(csvreader)
        #print the total number of months
        for row in csvreader:
            if row[0] != monthname:
                nummonths = nummonths + 1
                monthname = row[0]

        print("Total Months:  " + str(nummonths) )
        data_file.write("Total Months:  " + str(nummonths) + "\n" )

    with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader( csvfile, delimiter=",")

        #skip the header row
        csv_header = next(csvreader)
        #print the net total
        total = 0
        for row in csvreader:
            total = total + float(row[1])

        print("Total:  " + str(total) )
        data_file.write("Total:  " + str(total) + "\n")

    with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader( csvfile, delimiter=",")

        #skip the header row
        csv_header = next(csvreader)
        #print average of the changes in profit/losses
        oldvalue = 0
        newvalue = 0
        change = 0
        count = 0
        for row in csvreader:
            newvalue = float(row[1])
            change += abs(newvalue - oldvalue)
            oldvalue = newvalue
            count = count + 1

        print("Average Change:  " + str(round(change/count,2)) )
        data_file.write("Average Change:  " + str(round(change/count,2)) + "\n")
        # print("Total Change was " + str(change) )
        # print("Count is " + str(count)) 

    with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader( csvfile, delimiter=",")

        #skip the header row
        csv_header = next(csvreader)
        #print greatest increase in profits with month/year
        oldvalue = 0
        newvalue = 0
        monthyear = ""
        greatestvalue = 0
        for row in csvreader:
            newvalue = float(row[1])
            if float(greatestvalue) < newvalue:
                monthyear = row[0]
                greatestvalue = row[1]
        
        print("Greatest Increase in Profits:  " + monthyear + " ($" + str(greatestvalue) + ")")
        data_file.write("Greatest Increase in Profits:  " + monthyear + " ($" + str(greatestvalue) + ")\n")

    with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader( csvfile, delimiter=",")

        #skip the header row
        csv_header = next(csvreader)
        #print greatest increase in profits with month/year
        oldvalue = 0
        newvalue = 0
        monthyear = ""
        leastvalue = 0
        for row in csvreader:
            newvalue = float(row[1])
            if float(leastvalue) > newvalue:
                monthyear = row[0]
                leastvalue = row[1]
        
        print("Greatest Decrease in Profits:  " + monthyear + " ($" + str(leastvalue) + ")")
        data_file.write("Greatest Decrease in Profits:  " + monthyear + " ($" + str(leastvalue) + ")\n")
