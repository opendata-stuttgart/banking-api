from django.contrib import admin
from main.models import Bank


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'blz', 'bic')
