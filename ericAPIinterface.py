import numpy as np
import pandas as pd
import requests
import json
import time

#Driver function to get records from the ERIC API
def getERICRecords(search, fields = None, start=0, rows=200) : 
    url = 'https://api.ies.ed.gov/eric/?'
    url = url + 'search=' + search + '&rows=' + str(rows) + '&format=json&start=' + str(start)
    if(fields):
        url = url + '&fields' + ', '.join(fields)
    responseJSON = requests.get(url).json()
    return pd.DataFrame(responseJSON)

'''
Helper function to get records counts so that successive API calls
can iterate through the entire set of results for a specific search
'''
def getRecordCount(search):
    dataFrame = getERICRecords(search)
    totalRecords = dataFrame.loc['numFound'][0]
    print('Search', search, 'return', '{:,}'.format(totalRecords), 'records')
    return totalRecords

'''
Takes input 'x', returns it unchanged if not a list, or returns a comma-separated
string if it's an empty list or contains only an empty string.
'''
def cleanElementsUsingList(x): 
    if(not isinstance(x, list)):
        return x
    if(not x or (len(x) == 1 and x[0] == '')):
        return ', '.join(x)

#Helper function to get all results related to a specific search
def getAllERICRecords(search, fields = None, cleanElements = True):
    startTime = time.time()
    nextFirstRecord = 0
    numRecordsReturnedPerCall = 200
    totalRecords = getRecordCount(search)
    if(totalRecords == 0):
        print('Search', search, 'has no results')
        return []
    while(nextFirstRecord < totalRecords):
        dataFrame = getERICRecords(search, fields, nextFirstRecord)
        if(nextFirstRecord == 0):
            records = pd.DataFrame(dataFrame.loc['docs'][0])
        else:
            records = pd.concat([records, pd.DataFrame(dataFrame.loc['docs'][0])], sort=False, ignore_index=True)
        nextFirstRecord += numRecordsReturnedPerCall
    print('Took', '{:,.1f}'.format(time.time() - startTime), 'seconds')
    return records.applymap(cleanElementsUsingList) if cleanElements else records

