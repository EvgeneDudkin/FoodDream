from django.conf.urls import url
from django.contrib import admin
from offers.views import basic_one, offers, requests, answers
urlpatterns = [
    url(r'^1/', basic_one),
    url(r'^offers/$', offers),
    url(r'^answers/$', answers),
    url(r'^requests/$', requests),
    url(r'^', offers),
    # url(r'^articles/get/(?P<article_id>\d+)/$', article),
    # url(r'^articles/addlike/(?P<article_id>\d+)/$', addlike),
    # url(r'^articles/addcomment/(?P<article_id>\d+)/$', addcomment),
    # url(r'^page/(\d+)/$', articles),
    ]
