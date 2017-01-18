from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', 'products.views.index', name='index'),
    url(r'^s/$', 'products.views.search', name='search'),
]

