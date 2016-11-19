from django.contrib import admin
from offers.models import Offer, AnswerRequest, User


class OfferAdmin(admin.ModelAdmin):
    fields = ['offer_title', 'offer_address', 'offer_date', 'offer_id_user']
    # inlines = [ArticleInline]
    # list_filter = ['article_date']


admin.site.register(Offer)
admin.site.register(AnswerRequest)
admin.site.register(User)

