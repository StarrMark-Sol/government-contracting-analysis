import csv

print("Starting the CSV cleaning process...")

input_file = 'H:/DATA SCIENCE/DataProj/SMS-Data-Projects/pgADMIN/labor_standard_table.csv'
output_file = 'H:/DATA SCIENCE/DataProj/SMS-Data-Projects/pgADMIN/labor_standard_table_clean.csv'

expected_column_count = 2  # Number of columns in labor_standard_table

def clean_cell(cell):
    # Remove quotes from all cells
    cleaned_cell = cell.replace('"', '')
    # Remove any non-UTF-8 characters
    cleaned_cell = cleaned_cell.encode('utf-8', 'ignore').decode('utf-8')
    return cleaned_cell

with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    print("Files opened successfully.")

    for row in reader:
        # Clean each cell in the row
        row = [clean_cell(cell) for cell in row]
        # Ensure the row has the correct number of columns by padding with empty strings
        while len(row) < expected_column_count:
            row.append('')
        row = row[:expected_column_count]
        writer.writerow(row)
        print(f"Processed row: {row}")

print("CSV cleaning process completed.")

