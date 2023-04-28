import combineData
import cleanup
import os
import searches

#Run the searches
records = searches.runSearches()

#Data compilation
print('Combining data files into single JSON file: combinedData.json')
directory = '.'
json_files = [f for f in os.listdir(directory) if f.endswith('.json')]
unique_id_field = 'title' 
output_file = 'combinedData.json'
combineData.combineFiles(json_files, output_file, unique_id_field)

#Clean up repo
print('Starting clean up routine')
cleanup.cleanup()
# print(records.head())
# print(records)
