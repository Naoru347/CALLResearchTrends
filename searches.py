import ericAPIinterface
import time

def runSearches():
    #search1
    search= 'subject: Computer assisted instruction AND publicationdateyear: 2023'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data1.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    # #search2
    search= 'subject: Computer mediated Instruction AND subject: language teaching AND description: systematic review'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source"]
    records=ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data2.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    # #search 20
    search= 'subject: computer assisted instruction AND subject: language teaching AND author: Kasumi Yamazaki AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data20.json')
    print('Searches complete.')

    return records
