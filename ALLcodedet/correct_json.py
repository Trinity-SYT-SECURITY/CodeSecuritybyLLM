import json

with open('secure_programming_dpo.json', 'r') as f:
    data = f.readlines()

python_data = []

for line in data:
    if line.startswith('{"lang": "'):
        python_data.append(json.loads(line))

with open('secure_programming_dpo_out.json', 'w') as f:
    json.dump(python_data, f, indent=4)
