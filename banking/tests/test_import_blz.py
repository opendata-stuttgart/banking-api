import os.path
import pytest
from main.utils import get_rows_from_blz_excel, extract_data


@pytest.fixture
def one_line_xlsx():
    return "file://" + os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    'fixtures/',
                                    'one_line.xlsx')


class TestImportBlzFromExcel():

    @pytest.mark.parametrize(('key', 'value_type'), (
        ('BIC', str),
        ('Merkmal', int),
        ('Bank-leitzahl', int),
        ('PLZ', int),
        ('Ort', str),
    ))
    def test_import(self, one_line_xlsx, key, value_type):
        for row in get_rows_from_blz_excel(data_file=one_line_xlsx):
            keys = row.keys()
            assert key in keys
            assert isinstance(row[key], value_type)

    def test_processing(self, one_line_xlsx):
        for row in get_rows_from_blz_excel(data_file=one_line_xlsx):
            mapping = extract_data(row)
            assert len(mapping) == 13
            assert mapping['name'] == 'Bundesbank'
            break
