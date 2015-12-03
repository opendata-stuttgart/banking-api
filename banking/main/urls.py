# coding=utf-8
from rest_framework import routers
from django.conf.urls import patterns, include, url

from .views import BankView, IbanView


router = routers.DefaultRouter()
router.register(r'bank', BankView)
router.register(r'iban', IbanView, base_name='iban')

urlpatterns = patterns(
    '',
    url(regex=r'^', view=include(router.urls)),
)
