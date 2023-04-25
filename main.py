import ericAPIinterface

search='author: Megan Sizcek'
fields=["title", "author", "description", "publicationdateyear"]
records = ericAPIinterface.getAllERICRecords(search, fields)
ericAPIinterface.saveToJSON(records, 'test2.json')
# print(records.head())
# print(records)
