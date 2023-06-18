import pandas as pd
import json

# Load the Excel file into a DataFrame
df = pd.read_excel('CleanedData.xlsx')

# Convert the DataFrame to a list of dictionaries
data = df.to_dict(orient='records')

# Save the data as JSON
with open('cleanedAggregateData.json', 'w') as f:
    json.dump(data, f)
print('Excel to JSON conversion complete. JSON file saved as output.json.')
