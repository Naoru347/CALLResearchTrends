import ericAPIinterface
import time

def run_searches():
    #search1
    search= 'subject: Computer assisted instruction AND subject: language teaching AND publicationdateyear: 2023'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data1.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer assisted instruction AND subject: language teaching AND publicationdateyear: 2022'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data2.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer assisted instruction AND subject: language teaching AND publicationdateyear: 2021'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data3.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer assisted instruction AND subject: language teaching AND publicationdateyear: 2020'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data4.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer assisted instruction AND subject: language teaching AND publicationdateyear: 2019'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data5.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer assisted instruction AND subject: language teaching AND publicationdateyear: 2018'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data6.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer assisted instruction AND subject: language teaching AND publicationdateyear: 2017'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data7.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer assisted instruction AND subject: language teaching AND publicationdateyear: 2015'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data8.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer assisted instruction AND subject: language teaching AND publicationdateyear: 2014'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data9.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer assisted instruction AND subject: language teaching AND publicationdateyear: 2013'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data10.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    return records
