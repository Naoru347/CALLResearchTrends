import CombineData
import RandomSample
import Cleanup
import Searches
import os
import time
import json

#Run the searches
# start_time = time.time()
# records = Searches.run_searches()

#Data compilation
print('Combining data files into single JSON file: combinedData.json')
directory = '.'
json_files = [f for f in os.listdir(directory) if f.endswith('.json')]
unique_id_field = 'id' 
output_file = 'combinedData.json'
CombineData.combine_files(json_files, output_file, unique_id_field)

#Creating a training set of 100 random items (if needed)
# RandomSample.random_sample("combinedData.json", "trainingData.json", 100)

#Clean up repo
print('Starting clean up routine')
# Cleanup.cleanup()
# time.sleep(10)

#Get total results count and program runtime
with open('combinedData.json') as f:
    data = json.load(f)
num_entries = len(data)
# end_time = time.time() - start_time
print('Total records return: ', num_entries)
# print('Program runtime: ', end_time)
# print(records.head())
# print(records)
