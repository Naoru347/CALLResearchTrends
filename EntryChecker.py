import json

# List of JSON files
files = [
    '2013_combinedData.json',
    '2014_combinedData.json',
    '2015_combinedData.json',
    '2016_combinedData.json',
    '2017_combinedData.json',
    '2018_combinedData.json',
    '2019_combinedData.json',
    '2020_combinedData.json',
    '2021_combinedData.json',
    '2022_combinedData.json',
    '2023_combinedData.json'
]

# Loop through the files and print the number of entries
for file in files:
    with open(file, 'r') as f:
        data = json.load(f)
        num_entries = len(data)
        print(f"{file}: {num_entries} entries")
