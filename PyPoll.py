# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = "/Users/tylerengalla/Desktop/Data_Bootcamp/Analysis_Projects/Election_Analysis/Resources/election_results.csv"

# Assign a variable to save the file to a path
file_to_save = "/Users/tylerengalla/Desktop/Data_Bootcamp/Analysis_Projects/Election_Analysis/election_analysis.txt"

# Open the election results and read the file
with open(file_to_load) as election_data:
    #print(election_data)
    # To do: read and analyze the data here.

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Print each row in the CSV file.
    #for row in file_reader:
        #print(row)

    #Read and print the header row.
    headers = next(file_reader)
    print(headers)

#with open(file_to_save, "w") as txt_file:
    #writing to election_analysis 
    #txt_file.write("Counties in the Election\n--------------------------\nArapahoe\nDenver\nJefferson")
    




# 1. The total number of votes cast 

# 2. A complete list of candidates who received votes

# 3. The percentage of votes each candidate won

# 4. The total number of votes each candidate won

# 5. The winner of the electoin based on popular vote 

