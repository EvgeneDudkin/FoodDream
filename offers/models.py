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

#
# class Comments(models.Model):
#     class Meta:
#         db_table = "comments"
#
#     comments_date = models.DateTimeField(auto_now_add=True)
#     comments_text = models.TextField(verbose_name='Текст комментария')
#     comments_article = models.ForeignKey(Article)
#     comments_from = models.ForeignKey(User)
