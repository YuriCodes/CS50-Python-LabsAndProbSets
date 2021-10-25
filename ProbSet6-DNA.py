from sys import argv, exit
from csv import reader, DictReader


def main():
    
    # Check length of the command line arguments
    if len(argv) < 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)
        
      # Open csv file and convert to dictionary for key value pairs
    with open(argv[1], "r") as CSVfile:
        reader = DictReader(CSVfile)
        CSVlist = list(reader)
        
    # Open seq file and make it a list and use .read for the .txt file 
    with open(argv[2], "r") as file:
        sequence = file.read()
        
     # For each STR value, gotten by the CSV attribute fieldnames which returns a list of headers 
     # Calculate how many times it repeats in the sequence and add it to counter array
    counter = []
    
    # Start from 1 because 0 is the persons name
    for i in range(1, len(reader.fieldnames)):
        STRs = reader.fieldnames[i]
        counter.append(0)
        
    # Inner loop to find repeated sequence of STR counts
        for j in range(len(sequence)):
            countSTR = 0
            # Check if substring matches and increment countSTR
            if sequence[j:(j + len(STRs))] == STRs:
                k = 0
                while sequence[(j + k):(j + k + len(STRs))] == STRs:
                    countSTR += 1
                    k += len(STRs)
                # Compare the value to the previous one and if bigger make it the current count
                if countSTR > counter[i - 1]:
                    counter[i - 1] = countSTR
                    
    # Now loop and compare against the database of people
    for i in range(len(CSVlist)):
        match = 0
        for j in range(1, len(reader.fieldnames)):
            # Compare it, add to matches count and print the matching name
            # cvslist is the dictionary and fieldnames is the key value
            if int(counter[j - 1]) == int(CSVlist[i][reader.fieldnames[j]]):
                match += 1
            if match == (len(reader.fieldnames) - 1):
                print(CSVlist[i]['name'])
                exit(0)
                
    # Else no match was found
    print("No match")


main()