import json


def sum(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    total_sum = 0.0

    for item in data:
        if 'score' in item and 'weight' in item:
            total_sum += item['score'] * item['weight']

    return round(total_sum, 3)


json_file_path = 'input.json'
result = sum(json_file_path)
print(result)