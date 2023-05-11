import pandas as pd
import numpy as np
import json
import os
import glob
import time
from bertopic import BERTopic

#Load the data file by reading from the JSON into a generic data object
print("Importing data and building DataFrame:")
start_time = time.time()
with open ('data/combinedData.json', 'r') as f:
    data = json.load(f)
end_time = time.time()
load_time = end_time - start_time
print("Data load time", load_time)
#Convert the data to a PANDAS DataFrame for additional processing
print("Data loaded, converting to DataFrame")
start_time = time.time()
df = pd.DataFrame(data)
end_time = time.time()
convert_time = end_time - start_time
print("Data successfully converted to DataFrame. Conversion time: ", convert_time)
#Confirm loading and Conversion
print("Data loaded, generating head summary:")
print(df.head())
column_names = df.columns.to_list()
print(column_names)
#Begin topic modeling by creating the model
descriptions = df["description"].to_list()
model = BERTopic(verbose=True)
topics, probabilities = model.fit_transform(descriptions)

#Get list of topics
print(model.get_topic_freq().head(20))