import csv

input_file = 'H:/DATA SCIENCE/DataProj/SMS-Data-Projects/pgADMIN/funding_table.csv'
output_file = 'H:/DATA SCIENCE/DataProj/SMS-Data-Projects/pgADMIN/funding_table_clean.csv'

expected_column_count = 7  # Update this to the actual number of columns

with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        # Trim extra empty columns
        row = row[:expected_column_count]
        writer.writerow(row)
