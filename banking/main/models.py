from django.db import models
from django_extensions.db.models import TimeStampedModel


class Bank(TimeStampedModel):
    name = models.CharField(max_length=1000)
    blz = models.CharField(max_length=20)
    bic = models.CharField(max_length=20)
    plz = models.CharField(max_length=10)
    city = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    short_description = models.CharField(max_length=1000)
    pan = models.IntegerField(blank=True, null=True)
    check_calculation_method = models.CharField(max_length=2)
    dataset_number = models.CharField(max_length=10)
    merkmal = models.CharField(max_length=10, choices=(('1', '1'), ('2', '2')))  # name
    change_type = models.CharField(max_length=10)  # choice?
    is_deletion = models.BooleanField(default=False)
    following_blz = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return self.name
