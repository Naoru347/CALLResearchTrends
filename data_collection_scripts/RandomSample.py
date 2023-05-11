import json
import random

def random_sample(input_file, output_file, sample_size = 100):
    with open(input_file, 'r') as json_file:
        data =json.load(json_file)
    if len(data) < sample_size:
        print("Warning: Population size too small for desired sample size.")
        sample_size = len(data)
    random_sample = random.sample(data, sample_size)
    with open(output_file, 'w') as json_file:
        json.dump(random_sample, json_file)
    print("Random sampling complete. Data sample of size", len(random_sample), " created")