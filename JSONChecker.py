import json

def fix_json_file(file_path):
    with open(file_path, 'r') as f:
        try:
            data = json.load(f)
            # Check if the loaded data is a list of dictionaries
            if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                # File is valid JSON, no fixes needed
                return True
            else:
                # File is not valid JSON, handle the error or fix the data
                # Here, you can implement your logic to fix incomplete or malformed JSON
                # For example, you can add missing closing braces to complete the JSON objects
                fixed_data = data + [{}]
                # Save the fixed data back to the file
                with open(file_path, 'w') as f:
                    json.dump(fixed_data, f)
                    return True
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return False

# Usage
file_path = 'data/cleanedAggregateData.json'
if fix_json_file(file_path):
    print("JSON file is valid or fixed successfully.")
else:
    print("Error in JSON file, please check and fix the file.")
