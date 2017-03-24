import pandas as pd


def get_rows_from_blz_excel(data_file=None):
    if not data_file:
        data_file = "https://www.bundesbank.de/Redaktion/DE/Downloads/Aufgaben/Unbarer_Zahlungsverkehr/Bankleitzahlen/2017_06_04/blz_2017_03_06_xls.xlsx?__blob=publicationFile"
    data = pd.ExcelFile(data_file).parse()
    # replace float with value `nan` with None
    data_with_none = data.where((pd.notnull(data)), None)
    for index, row in data_with_none.iterrows():
        yield row


def extract_data(row):
    return {
        'name': row['Bezeichnung'],
        'blz': row['Bank-leitzahl'],
        'bic': row['BIC'],
        'zipcode': row['PLZ'],
        'city': row['Ort'],
        'short_description': row['Kurzbezeichnung'],
        'pan': row['PAN'],
        'check_calculation_method': row['Prüfziffer-berechnungs-methode'],
        'dataset_number': row['Datensatz-nummer'],
        'merkmal': row['Merkmal'],
        'change_type': row['Änderungs-kennzeichen'],
        'is_deletion': row['Bankleitzahl-löschung'],
        'following_blz': row['Nachfolge-Bankleitzahl'],
    }
