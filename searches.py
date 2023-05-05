import ericAPIinterface
import time

def run_searches():
    search= 'subject: Applied Linguistics AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data1.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Applied Linguistics AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data2.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Applied Linguistics AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data3.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Applied Linguistics AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data4.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Applied Linguistics AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data5.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Assisted Instruction AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data6.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Assisted Instruction AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data7.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Assisted Instruction AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data8.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Assisted Instruction AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data9.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Assisted Instruction AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data10.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Mediated Communication AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data11.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Mediated Communication AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data12.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Mediated Communication AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data13.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Mediated Communication AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data14.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Mediated Communication AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data15.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Simulation AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data16.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Simulation AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data17.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Simulation AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data18.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Simulation AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data19.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Computer Simulation AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data20.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Educational Technology AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data21.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Educational Technology AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data22.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Educational Technology AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data23.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Educational Technology AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data24.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Educational Technology AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data25.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English(Second Language) AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data26.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English(Second Language) AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data27.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English(Second Language) AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data28.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English(Second Language) AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data29.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English(Second Language) AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data30.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English as a Foreign Language Teachers AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data31.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English as a Foreign Language Teachers AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data32.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English as a Foreign Language Teachers AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data33.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English as a Foreign Language Teachers AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data34.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English as a Foreign Language Teachers AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data35.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English as a Second Language Teachers AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data36.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English as a Second Language Teachers AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data37.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English as a Second Language Teachers AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data38.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English as a Second Language Teachers AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data39.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: English as a Second Language Teachers AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data40.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Instruction AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data41.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Instruction AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data42.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Instruction AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data43.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Instruction AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data44.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Instruction AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data45.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Instruction AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data46.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Learning AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data47.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Learning AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data48.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Learning AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data49.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Learning AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data50.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Teachers AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data51.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Teachers AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data52.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Teachers AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data53.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Teachers AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data54.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Teachers AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data55.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Teaching AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data56.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Teaching AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data57.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Teaching AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data58.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Teaching AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data59.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Language Teaching AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data60.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Languages AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data61.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Languages AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data62.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Languages AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data63.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Languages AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data64.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Foreign Languages AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data65.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Game Based Learning AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data66.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Game Based Learning AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data67.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Game Based Learning AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data68.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Game Based Learning AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data69.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Game Based Learning AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data70.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Hypermedia AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data71.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Hypermedia AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data72.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Hypermedia AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data73.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Hypermedia AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data74.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Hypermedia AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data75.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Acquisition AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data76.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Acquisition AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data77.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Acquisition AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data78.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Acquisition AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data79.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Acquisition AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data80.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Fluency AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data81.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Fluency AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data82.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Fluency AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data83.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Fluency AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data84.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Fluency AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data85.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Input AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data86.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Input AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data87.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Input AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data88.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Input AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data89.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Input AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data90.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Learning (Foreign) AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data91.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Learning (Foreign) AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data92.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Learning (Foreign) AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data93.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Learning (Foreign) AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data94.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Learning (Foreign) AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data95.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Proficiency AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data96.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Proficiency AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data97.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Proficiency AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data98.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Proficiency AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data99.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Proficiency AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data100.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Research AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data101.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Research AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data102.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Research AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data103.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Research AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data104.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Research AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data105.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Skills AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data106.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Skills AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data107.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Skills AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data108.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Skills AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data109.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Skills AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data110.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Teachers AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data111.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Teachers AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data112.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Teachers AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data113.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Teachers AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data114.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Teachers AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data115.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Usage AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data116.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Usage AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data117.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Usage AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data118.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Usage AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data119.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Language Usage AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data120.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Languages AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data121.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Languages AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data122.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Languages AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data123.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Languages AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data124.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Languages AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data125.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Linguistic Competence AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data126.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Linguistic Competence AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data127.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Linguistic Competence AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data128.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Linguistic Competence AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data129.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Linguistic Competence AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data130.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Linguistic Input AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data131.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Linguistic Input AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data132.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Linguistic Input AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data133.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Linguistic Input AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data134.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Linguistic Input AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data135.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Linguistic Research AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data136.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Linguistic Research AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data137.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Linguistic Research AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data138.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Linguistic Research AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data139.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Linguistic Research AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data140.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Linguistics AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data141.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Linguistics AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data142.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Linguistics AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data143.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Linguistics AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data144.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Linguistics AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data145.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Simulation AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data146.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Simulation AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data147.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Simulation AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data148.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Simulation AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data149.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Simulation AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data150.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Teaching Language AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data151.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Teaching Language AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data152.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Teaching Language AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data153.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Teaching Language AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data154.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Teaching Language AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data155.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Virtual Classrooms AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data156.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Virtual Classrooms AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data157.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Virtual Classrooms AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data158.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Virtual Classrooms AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data159.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Virtual Classrooms AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data160.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Virtual Environments AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data161.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Virtual Environments AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data162.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Virtual Environments AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data163.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Virtual Environments AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data164.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Virtual Environments AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data165.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Virtual Reality AND publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data166.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Virtual Reality AND publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data167.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Virtual Reality AND publicationdateyear: 2015 AND source: SYSTEM AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data168.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Virtual Reality AND publicationdateyear: 2015 AND source: ReCALL AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data169.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'subject: Virtual Reality AND publicationdateyear: 2015 AND source: CALICO AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data170.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    return records
