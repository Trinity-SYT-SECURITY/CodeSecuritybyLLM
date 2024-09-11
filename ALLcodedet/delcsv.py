import csv


def trim_csv(input_filename, output_filename, max_rows=1500):
    with open(input_filename, 'r', encoding='utf-8') as input_csv:
        csv_reader = csv.reader(input_csv)
        rows = list(csv_reader)

    trimmed_rows = rows[:max_rows]

    with open(output_filename, 'w', newline='', encoding='utf-8') as output_csv:
        csv_writer = csv.writer(output_csv)
        csv_writer.writerows(trimmed_rows)


trim_csv('ALL_code.csv', 'ALL_codedel.csv')
