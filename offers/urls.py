from django.conf.urls import url
from django.contrib import admin
from offers.views import basic_one, offers
urlpatterns = [
    url(r'^1/', basic_one),
    # url(r'^2/', template_two),
    # url(r'^3/', template_three_simple),
    url(r'^offers/all$', offers),
    # url(r'^articles/get/(?P<article_id>\d+)/$', article),
    # url(r'^articles/addlike/(?P<article_id>\d+)/$', addlike),
    # url(r'^articles/addcomment/(?P<article_id>\d+)/$', addcomment),
    # url(r'^page/(\d+)/$', articles),
    url(r'^', offers),
    ]
