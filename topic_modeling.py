import pandas as pd
import matplotlib.pyplot as plt
import json
import time
from bertopic import BERTopic

# Load the data file by reading from the JSON into a generic data object
print("Importing data and building DataFrame:")
start_time = time.time()
with open('data/combinedData.json', 'r') as f:
    data = json.load(f)
end_time = time.time()
load_time = end_time - start_time
print("Data load time", load_time)
print(data[0])

# Convert the data to a PANDAS DataFrame for additional processing
print("Data loaded, converting to DataFrame")
start_time = time.time()
df = pd.DataFrame(data)
end_time = time.time()
convert_time = end_time - start_time
print("Data successfully converted to DataFrame. Conversion time:", convert_time)

# Confirm loading and conversion
print("Data loaded, generating head summary:")
print(df.head())
column_names = df.columns.to_list()
print(column_names)

# # Begin topic modeling by creating the model
# model = BERTopic(embedding_model="all-MiniLM-L6-v2")
# docs = df.description.to_list()
# topics, probabilities = model.fit_transform(docs)
# model.get_topic_info()

# print(model.get_topic(1))
# print(model.get_topic(2))
# print(model.get_topic(3))
# print(model.get_topic(4))
# print(model.get_topic(5))

# # # Visualizations
# model.visualize_topics()
# model.visualize_barchart()
