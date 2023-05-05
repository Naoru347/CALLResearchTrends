import json

# Set of target source values
acceptable_sources = {"ReCALL", "Computer Assisted Language Learning", "Journal of Educational Technology Systems", "CALICO Journal", "Language Learning & Technology", "System: An International Journal of Educational Technology and Applied Linguistics"}

# Read data from the JSON file
with open('rawAggregateData.json', 'r') as file:
    data = json.load(file)

# Filter out entries with non-matching source values
filtered_data = [entry for entry in data if entry.get("source") in acceptable_sources]

# Save the filtered data back to the JSON file (or another file if needed)
with open('cleanedAggregateData.json', 'w') as file:
    json.dump(filtered_data, file, indent=2)

print("Cleaed data has been saved to 'cleanedAggregateData.json'.")
print("Final sample size: " + len(cleanedAggregateData.json))
