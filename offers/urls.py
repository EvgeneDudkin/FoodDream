from django.conf.urls import url
from django.contrib import admin
from offers.views import basic_one, offers, answers, requests, my_offers, addoffer, deloffer
urlpatterns = [
    url(r'^1/', basic_one),
    url(r'^offers/$', offers),
    url(r'^answers/$', answers),
    url(r'^requests/$', requests),
    url(r'^my_offers/$', my_offers),
    url(r'^addoffer/$', addoffer),
    url(r'^deloffer/(?P<offer_id>\d+)/$', deloffer),
    url(r'^', offers),
    # url(r'^offers/get/(?P<article_id>\d+)/$', offers),
    # url(r'^articles/addlike/(?P<article_id>\d+)/$', addlike),

    # url(r'^page/(\d+)/$', articles),
    ]
