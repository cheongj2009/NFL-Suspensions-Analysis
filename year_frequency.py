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

# Display years
print(years)

# Use list comprehension and set method to extract unique teams
unique_teams = [row[1] for row in nfl_suspensions]
unique_teams = set(unique_teams)

# Use list comprehension and set method to extract unique number of games
unique_games = [row[2] for row in nfl_suspensions]
unique_games = set(unique_games)

# Display unique_teams and unique_games
print(unique_teams)
print(unique_games)


# Create class for containing row information
class Suspension:
    def __init__(self, row):
        self.row = row
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        self.year = row[5]

# Example instantiation of the class
third_suspension = Suspension(nfl_suspensions[2])

# Create revised class for containing row information
class SuspensionNew():
    def __init__(self, row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year = int(row[5])
        except Exception:
            self.year = 0

    def get_year(self):
        return (self.year)

# Test out SuspensionNew class using 23rd row in data
missing_year = SuspensionNew(nfl_suspensions[22])
twenty_third_year = missing_year.get_year()