import csv
import json

# Open the CSV file
def read_csv(file: str) -> list:
    with open(file, 'r') as file:
        # Create a CSV reader object
        reader = csv.DictReader(file)

        # Convert the CSV data to a list of dictionaries
        data = [row for row in reader]

    return data

def write_csv(file: str, data: list) -> None:
    with open(file, 'w', newline='') as file:
        # Create a CSV writer object
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Write the CSV data to the file
        writer.writerow(data)

def save(file: str, data: dict) -> None:
    with open(file, 'a') as file:
        outfile = csv.DictWriter(file, fieldnames=data.keys())
        outfile.writerow(data)

def get_new_id(file: str) -> int:
    with open(file, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]

    return len(data) + 1
