import ericAPIinterface
import time

def run_searches():
    #2013
    search= 'subject: Applied Linguistics AND publicationdateyear: 2013 AND source: Computer Assisted Language Learning AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data1.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Applied Linguistics AND publicationdateyear: 2013 AND source: Language Learning & Technology AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data2.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Applied Linguistics AND publicationdateyear: 2013 AND source: SYSTEM AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data3.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Applied Linguistics AND publicationdateyear: 2013 AND source: ReCALL AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data4.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Applied Linguistics AND publicationdateyear: 2013 AND source: CALICO AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data5.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Assisted Instruction AND publicationdateyear: 2013 AND source: Computer Assisted Language Learning AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data6.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Assisted Instruction AND publicationdateyear: 2013 AND source: Language Learning & Technology AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data7.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Assisted Instruction AND publicationdateyear: 2013 AND source: SYSTEM AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data8.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Assisted Instruction AND publicationdateyear: 2013 AND source: ReCALL AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data9.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Assisted Instruction AND publicationdateyear: 2013 AND source: CALICO AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data10.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Mediated Communication AND publicationdateyear: 2013 AND source: Computer Assisted Language Learning AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data11.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Mediated Communication AND publicationdateyear: 2013 AND source: Language Learning & Technology AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data12.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Mediated Communication AND publicationdateyear: 2013 AND source: SYSTEM AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data13.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Mediated Communication AND publicationdateyear: 2013 AND source: ReCALL AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data14.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Mediated Communication AND publicationdateyear: 2013 AND source: CALICO AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data15.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Simulation AND publicationdateyear: 2013 AND source: Computer Assisted Language Learning AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data16.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Simulation AND publicationdateyear: 2013 AND source: Language Learning & Technology AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data17.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Simulation AND publicationdateyear: 2013 AND source: SYSTEM AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data18.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Simulation AND publicationdateyear: 2013 AND source: ReCALL AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data19.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Simulation AND publicationdateyear: 2013 AND source: CALICO AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data20.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Educational Technology AND publicationdateyear: 2013 AND source: Computer Assisted Language Learning AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data21.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Educational Technology AND publicationdateyear: 2013 AND source: Language Learning & Technology AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data22.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Educational Technology AND publicationdateyear: 2013 AND source: SYSTEM AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data23.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Educational Technology AND publicationdateyear: 2013 AND source: ReCALL AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data24.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Educational Technology AND publicationdateyear: 2013 AND source: CALICO AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data25.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English(Second Language) AND publicationdateyear: 2013 AND source: Computer Assisted Language Learning AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data26.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English(Second Language) AND publicationdateyear: 2013 AND source: Language Learning & Technology AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data27.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English(Second Language) AND publicationdateyear: 2013 AND source: SYSTEM AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data28.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English(Second Language) AND publicationdateyear: 2013 AND source: ReCALL AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data29.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English(Second Language) AND publicationdateyear: 2013 AND source: CALICO AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data30.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English as a Foreign Language Teachers AND publicationdateyear: 2013 AND source: Computer Assisted Language Learning AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data31.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English as a Foreign Language Teachers AND publicationdateyear: 2013 AND source: Language Learning & Technology AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data32.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English as a Foreign Language Teachers AND publicationdateyear: 2013 AND source: SYSTEM AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data33.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English as a Foreign Language Teachers AND publicationdateyear: 2013 AND source: ReCALL AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data34.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English as a Foreign Language Teachers AND publicationdateyear: 2013 AND source: CALICO AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data35.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English as a Second Language Teachers AND publicationdateyear: 2013 AND source: Computer Assisted Language Learning AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data36.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English as a Second Language Teachers AND publicationdateyear: 2013 AND source: Language Learning & Technology AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data37.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English as a Second Language Teachers AND publicationdateyear: 2013 AND source: SYSTEM AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data38.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English as a Second Language Teachers AND publicationdateyear: 2013 AND source: ReCALL AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data39.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English as a Second Language Teachers AND publicationdateyear: 2013 AND source: CALICO AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data40.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Instruction AND publicationdateyear: 2013 AND source: Computer Assisted Language Learning AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data41.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Instruction AND publicationdateyear: 2013 AND source: Language Learning & Technology AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data42.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Instruction AND publicationdateyear: 2013 AND source: SYSTEM AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data43.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Instruction AND publicationdateyear: 2013 AND source: ReCALL AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data44.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Instruction AND publicationdateyear: 2013 AND source: CALICO AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data45.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Instruction AND publicationdateyear: 2013 AND source: Computer Assisted Language Learning AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data46.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Learning AND publicationdateyear: 2013 AND source: Language Learning & Technology AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data47.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Learning AND publicationdateyear: 2013 AND source: SYSTEM AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data48.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Learning AND publicationdateyear: 2013 AND source: ReCALL AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data49.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Learning AND publicationdateyear: 2013 AND source: CALICO AND peerreviewed: T'
    fields=["author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data50.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    return records
