# coding=utf-8
from django.core.management import BaseCommand


class Command(BaseCommand):

    help = "Import data from Bundesbank."

    def handle(self, *args, **options):
        from main.models import Bank
        from main.utils import get_rows_from_blz_excel, extract_data
        prev_bic = None
        for element in get_rows_from_blz_excel():
            d = extract_data(element)
            dataset_number = d.pop('dataset_number')
            if not d['bic'] and prev_bic:
                d['bic'] = prev_bic
            b, x = Bank.objects.get_or_create(dataset_number=dataset_number,
                                              defaults=d)
            prev_bic = d['bic']
