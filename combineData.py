import json
import os

def combine_files(files, output_file, unique_id_field):
    combined_data = []

    # Read the content of each JSON file and append it to combined_data
    for file in files:
        with open(file, 'r') as f:
            data = json.load(f)
            combined_data += data

    # Remove duplicates based on the unique_id_field
    unique_data = {entry[unique_id_field]: entry for entry in combined_data}.values()

    # Save the unique combined data to a new JSON file
    with open(output_file, 'w') as output:
        json.dump(list(unique_data), output)

