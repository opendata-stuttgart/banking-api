import pandas as pd


def get_rows_from_blz_excel(data_file=None):
    if not data_file:
        data_file = "http://www.bundesbank.de/Redaktion/DE/Downloads/Aufgaben/Unbarer_Zahlungsverkehr/Bankleitzahlen/2016_03_06/blz_2015_12_07_xls.xlsx?__blob=publicationFile"
    data = pd.ExcelFile(data_file).parse()
    # replace float with value `nan` with None
    data_with_none = data.where((pd.notnull(data)), None)
    for index, row in data_with_none.iterrows():
        yield row


def import_blz_to_database(data_file=None):
    for row in get_rows_from_blz_excel(data_file):
        assert False
        pass
