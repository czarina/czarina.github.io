"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from commissions import views as views_commissions
from accounts import views as views_accounts
from orders import views as views_orders
admin.autodiscover()
from django.contrib.auth import views as auth_views

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL =  'home'


urlpatterns = [
	url(r'^$', views_commissions.index, name='index'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    url(r'^search/$', views_commissions.search, name='search'),
    url(r'^order/(?P<id>\d+)/$', views_orders.order, name='order'),
    url(r'^commission/(?P<id>\d+)/request_form$', views_commissions.create_request, name='create_request'),
    url(r'^commission/(?P<id>\d+)/request_confirmation$', views_commissions.request_confirmation, name='request_confirmation'),
    url(r'^commission/(?P<id>\d+)/$', views_commissions.commission, name='commission'),
    url(r'^user/(?P<id>\d+)/portfolio/$', views_accounts.store_portfolio, name='store_portfolio'),
    url(r'^user/(?P<id>\d+)/feed/$', views_accounts.store_feed, name='store_feed'),
    url(r'^user/(?P<id>\d+)/reviews$', views_accounts.store_reviews, name='store_reviews'),
    url(r'^user/(?P<id>\d+)/about$', views_accounts.store_about, name='store_about'),
    url(r'^user/(?P<id>\d+)/$', views_accounts.store, name='store'),
	url(r'^admin/', include(admin.site.urls)),

]
