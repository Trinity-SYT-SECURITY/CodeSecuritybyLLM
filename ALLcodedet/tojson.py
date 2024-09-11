import json
import csv

#json轉換為csv
def write_json_to_csv(json_filename, csv_filename):
    with open(json_filename, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(
            ["lang", "vulnerability", "question", "chosen", "rejected"])

        for entry in data:
            csv_writer.writerow([
                entry["lang"],
                entry["vulnerability"],
                entry["question"],
                entry["chosen"],
                entry["rejected"]
            ])


write_json_to_csv('secure_programming_out.json',
                  'secure_programming_out.csv')
