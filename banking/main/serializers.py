from .models import Bank
from rest_framework import serializers


class BankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bank
        fields = ("url", "name", "blz", "bic", "zipcode", "city")


class Iban(object):
    """ fake model for create() in IbanSerializer
    """
    def __init__(self, **kwargs):
        self.country = kwargs.get('country', None)
        self.blz = kwargs.get('blz', None)
        self.account_number = kwargs.get('account_number', None)
        self.iban = kwargs.get('iban', None)


class IbanSerializer(serializers.Serializer):
    country = serializers.CharField(max_length=2)
    blz = serializers.CharField(max_length=10)
    account_number = serializers.CharField(max_length=12)
    iban = serializers.CharField(max_length=40, read_only=True)

    def create(self, validated_data):
        blz = int(validated_data['blz'])
        kto = int(validated_data['account_number'])
        country = validated_data['country']
        iban_checksum = 98 - (int('{:08d}{:010d}131400'.format(blz, kto)) % 97)
        validated_data['iban'] = '{:2s}{:02d}{:08d}{:010d}'.format(country,
                                                                   iban_checksum,
                                                                   blz, kto)
        return Iban(**validated_data)
