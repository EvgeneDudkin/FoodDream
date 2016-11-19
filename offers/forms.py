from django.forms import Form
from .models import Offer


class OfferForm(Form):
    class Meta:
        model = Offer
        fields = ['offer_title',
                  # 'offer_address',
                  # 'offer_date',
                  # 'offer_id_user'
                  ]
