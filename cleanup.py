#A function to clean up json's mess
import glob
import os

def deleteAll(): 
    pattern = "*.json"
    jsonFiles = glob.glob(pattern)
    for jsonFile in jsonFiles:
        os.remove(jsonFile)
        print(f"Deleted: {jsonFile}")