import csv


def read_csv_address(file_name='csv/address_data_to_upload.csv'):
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [[row['continent'], row['country'], row['state'], row['city']] for row in reader]

    return data


def read_csv_name_surname(file_name='csv/name_surname_data_to_upload.csv'):
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [[row['name'], row['surname']] for row in reader]
    return data