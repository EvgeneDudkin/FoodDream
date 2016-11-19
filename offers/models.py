from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        swappable = 'AUTH_USER_MODEL'
        db_table = "user"
    user_address = models.TextField()
    # user_distr_rate = models.FloatField()
    # user_buyer_rate = models.FloatField()


class Offer(models.Model):
    class Meta:
        db_table = "offer"
    offer_title = models.CharField(max_length=200)
    offer_address = models.TextField()
    offer_date = models.DateTimeField()
    offer_id_user = models.ForeignKey(User, to_field='id')
    # offer_radius = models.IntegerField()


class AnswerRequest(models.Model):
    class Meta:
        db_table = "answer_request"
    answer_request_id_user = models.ForeignKey(User,
                                               to_field='id',
                                               related_name='answer_request_id_user')
    answer_request_id_offer = models.ForeignKey(Offer,
                                                to_field='id',
                                                related_name='answer_request_id_offer'
                                                )
    answer_request_comment = models.TextField()
    answer_request_status = models.IntegerField()





# class Answer(models.Model):
#     class Meta:
#         db_table = "answer"
#     answer_title = models.CharField(max_length=200)
#     answer_status = models.CharField(max_length=20)
#
#
# class Request(models.Model):
#     class Meta:
#         db_table = "request"
#     request_title = models.CharField(max_length=200)
#     request_requester = models.CharField(max_length=20)
#     request_status = models.CharField(max_length=20)
#
#
# class MyOffers(Offer):
#     class Meta:
#         db_table = "my_offers"
#     my_offers_title = Offer.offer_title
#     my_offers_address = Offer.offer_address
#     my_offers_date = Offer.offer_date
#     my_offers_radius = Offer.offer_radius
#     my_offers_rate = Offer.offer_rate
