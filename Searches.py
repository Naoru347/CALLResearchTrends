import ericAPIinterface
import time

def run_searches():
    
    issns = ['ISSN-0958-8221', 'EISSN-1094-3501', 'ISSN-0346-251X', 'ISSN-1879-3282', 'ISSN-0958-3440', 'ISSN-0742-7778']
    years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
    fields = ["id", "author", "title", "description", "subject", "publicationdateyear", "source", "identifiersgeo"]

    file_count = 1

    for year in years:
        for issn in issns:
            search = f'publicationdateyear: {year} AND issn: {issn} AND peerreviewed: T'
            records = ericAPIinterface.getAllERICRecords(search, fields)
            filename = f'data{file_count}.json'
            ericAPIinterface.saveToJSON(records, filename)
            print('Next API Search in 2 seconds.')
            time.sleep(2)
            file_count += 1
    
    return records
