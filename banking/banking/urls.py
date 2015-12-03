from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', RedirectView.as_view(url='/v1/', permanent=False)),
    url(r'^v1/', include('main.urls')),
]
