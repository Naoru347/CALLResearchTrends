import ericAPIinterface
import time

def run_searches():
    search= 'publicationdateyear: 2013 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data1.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2013 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data2.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2013 AND issn: ISSN-0346-251X AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data3.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2013 AND issn: ISSN-0958-3440 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data4.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2013 AND source: ISSN-0742-7778 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data5.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2014 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data1.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2014 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data2.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2014 AND issn: ISSN-0346-251X AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data3.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2014 AND issn: ISSN-0958-3440 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data4.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2014 AND source: ISSN-0742-7778 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data5.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2015 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data1.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2015 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data2.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2015 AND issn: ISSN-0346-251X AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data3.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2015 AND issn: ISSN-0958-3440 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data4.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2015 AND source: ISSN-0742-7778 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data5.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2016 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data1.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2016 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data2.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2016 AND issn: ISSN-0346-251X AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data3.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2016 AND issn: ISSN-0958-3440 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data4.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2016 AND source: ISSN-0742-7778 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data5.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2022 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data1.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2022 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data2.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2022 AND issn: ISSN-0346-251X AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data3.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2022 AND issn: ISSN-0958-3440 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data4.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2022 AND source: ISSN-0742-7778 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data5.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2017 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data1.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2017 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data2.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2017 AND issn: ISSN-0346-251X AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data3.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2017 AND issn: ISSN-0958-3440 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data4.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2017 AND source: ISSN-0742-7778 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data5.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2018 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data1.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2018 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data2.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2018 AND issn: ISSN-0346-251X AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data3.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2018 AND issn: ISSN-0958-3440 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data4.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2018 AND source: ISSN-0742-7778 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data5.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2019 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data1.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2019 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data2.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2019 AND issn: ISSN-0346-251X AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data3.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2019 AND issn: ISSN-0958-3440 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data4.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2019 AND source: ISSN-0742-7778 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data5.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2020 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data1.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2020 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data2.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2020 AND issn: ISSN-0346-251X AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data3.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2020 AND issn: ISSN-0958-3440 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data4.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2020 AND source: ISSN-0742-7778 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data5.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2021 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data1.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2021 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data2.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2021 AND issn: ISSN-0346-251X AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data3.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2021 AND issn: ISSN-0958-3440 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data4.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2021 AND source: ISSN-0742-7778 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data5.json')
    print('Next API Search in 2 seconds.')

    search= 'publicationdateyear: 2023 AND issn: ISSN-0958-8221 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data1.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2023 AND issn: EISSN-1094-3501 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data2.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2023 AND issn: ISSN-0346-251X AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data3.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2023 AND issn: ISSN-0958-3440 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data4.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)

    search= 'publicationdateyear: 2023 AND source: ISSN-0742-7778 AND peerreviewed: T'
    fields=["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]
    records= ericAPIinterface.getAllERICRecords(search, fields)
    ericAPIinterface.saveToJSON(records, 'data5.json')
    print('Next API Search in 2 seconds.')
    time.sleep(2)
    return records
