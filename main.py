import ericAPIinterface
import cleanup

search = 'subject: Computer mediated instruction AND subject: language teaching AND peerreviewed: T'
fields=["title", "author", "description", "publicationdateyear"]
records = ericAPIinterface.getAllERICRecords(search, fields)
ericAPIinterface.saveToJSON(records, 'test2.json')
# cleanup.deleteAll()
# print(records.head())
# print(records)
