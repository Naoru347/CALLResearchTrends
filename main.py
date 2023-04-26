import ericAPIinterface
import combineData
import cleanup
import time
import os

#search1
search= 'author: `Kasumi Yamazaki`'
fields=["author", "title", "description", "subject", "publicationdateyear", "source"]
records= ericAPIinterface.getAllERICRecords(search, fields)
ericAPIinterface.saveToJSON(records, 'data1.json')
print('Next API Search in 10 seconds.')
time.sleep(10)

#search2
search= 'subject: Computer mediated Instruction AND subject: language teaching AND description: systematic review'
fields=["author", "title", "description", "subject", "publicationdateyear", "source"]
records=ericAPIinterface.getAllERICRecords(search, fields)
ericAPIinterface.saveToJSON(records, 'data2.json')
print('Next API Search in 10 seconds.')
time.sleep(10)

#search 20
search= 'subject: computer assisted instruction AND subject: language teaching AND author: Kasumi Yamazaki AND peerreviewed: T'
fields=["author", "title", "description", "subject", "publicationdateyear", "source"]
records= ericAPIinterface.getAllERICRecords(search, fields)
ericAPIinterface.saveToJSON(records, 'data20.json')
print('Searches complete.')

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
