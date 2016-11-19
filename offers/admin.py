from django.contrib import admin
from offers.models import Offer
# Register your models here.
#
#
# # class ArticleInline(admin.StackedInline):
# #     model = Comments
# #     extra = 2
#
#
class OfferAdmin(admin.ModelAdmin):
    fields = ['offer_title', 'offer_address', 'offer_date']
    # inlines = [ArticleInline]
    # list_filter = ['article_date']
#
admin.site.register(Offer)
