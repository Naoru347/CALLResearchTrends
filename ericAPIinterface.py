import numpy as np
import pandas as pd
import requests
import json
import time

def getERICRecords(search, fields = None, start=0, rows=200) : 
    url = 'https://api.ies.ed.gov/eric/?'
    url = url + 'search=' + search + '&rows=' + str(rows) + '&format=json&start=' + str(start)
    if(fields):
        url = url + '&fields' + ', '.join(fields)
    responseJSON = requests.get(url).json()
    return pd.DataFrame(responseJSON)