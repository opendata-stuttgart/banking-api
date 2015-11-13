from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', RedirectView.as_view(url='/v1/', permanent=False)),
    url(r'^v1/', include('main.urls')),
    url(r'^auth/', include('rest_framework.urls',
                           namespace='rest_framework')),
    url(r'^get-auth-token/', obtain_auth_token),
]
