import datetime

from django.contrib.auth.models import User
from django.db import models


class Offer(models.Model):
    class Meta:
        db_table = "offer"
    offer_title = models.CharField(max_length=200)
    offer_address = models.TextField()
    offer_date = models.DateTimeField()
    offer_radius = models.IntegerField()
    offer_rate = models.FloatField()


class Answer(models.Model):
    class Meta:
        db_table = "answer"
    answer_title = models.CharField(max_length=200)
    answer_status = models.CharField(max_length=20)


class Request(models.Model):
    class Meta:
        db_table = "request"
    request_title = models.CharField(max_length=200)
    request_requester = models.CharField(max_length=20)
    request_status = models.CharField(max_length=20)


class MyOffers(Offer):
    class Meta:
        db_table = "my_offers"
    my_offers_title = Offer.offer_title
    my_offers_address = Offer.offer_address
    my_offers_date = Offer.offer_date
    my_offers_radius = Offer.offer_radius
    my_offers_rate = Offer.offer_rate
