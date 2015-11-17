import pytest
from main.serializers import IbanSerializer


class TestSepa:

    @pytest.fixture(params=[
        ('DE', '64090100', '1234567', 'DE80640901000001234567'),
        ('DE', 64090100, 1234567, 'DE80640901000001234567'),
        ('DE', 11111111, 1111111111, 'DE63111111111111111111'),
    ])
    def iban_fixture(self, request):
        return dict(zip(('country', 'blz', 'account_number', 'iban'), request.param))

    def test_iban_creation(self, iban_fixture):
        iban = iban_fixture.pop('iban')
        x = IbanSerializer().create(iban_fixture)
        assert x.iban == iban
