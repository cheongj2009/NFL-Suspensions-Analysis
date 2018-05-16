import csv

# Open csv file and convert into list of lists
f= open("nfl_suspensions_data.csv","r")
csvreader = csv.reader(f)
nfl_suspensions = list(csvreader)

# Remove first list in nfl_suspensions, which contains the header row_year
nfl_suspensions = nfl_suspensions[1:]

# Create empty dictionary
years = {}

# Loop over each row in the data and create dictionary of years and year frequency
for row in nfl_suspensions:
    row_year = row[5]
    if row_year in years:
        years[row_year] = years[row_year] + 1
    else:
        years[row_year] = 1
        
print(years)