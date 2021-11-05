from sys import argv
from sys import exit
import csv

if len(argv) != 3:
    print("Usage: dna.py csv txt")
    exit(1)

# open the DNA sequence and read its contents into memory.
txtfile = open(argv[2], "r")
if not txtfile:
    print("Could not open file.")
    exit(1)
dna = txtfile.read()


# For each of the STRs, compute the longest run of consecutive repeats of the STR in the DNA sequence to identify
keys = ["AGATC", "AATG", "TATC"]
keysMax = [0, 0, 0]
for j in range(len(keys)):
    for i in range(len(dna)):
        count = 0
        if dna[i:i+len(keys[j])]  == keys[j]:
            while dna[i:i+len(keys[j])]  == keys[j]:
                i += len(keys[j])
                count += 1
            if count > keysMax[j]:
                keysMax[j] = count


# If the STR counts match exactly with any of the individuals in the CSV file, print out the name of the matching individual.
csvfile = open('databases/small.csv', newline='')
reader = csv.DictReader(csvfile)
found = False

#Compare each row of CSV with STR results
for row in reader:
    if int(row['AGATC']) == keysMax[0] and int(row['AATG']) == keysMax[1] and int(row['TATC']) == keysMax[2]:
        match = row['name']
        found = True

# Print match
if found == True:
    print(match)
else:
    print("No match.")

print(len(reader.fieldnames))
first = reader.fieldnames
del first[0]
print(first)