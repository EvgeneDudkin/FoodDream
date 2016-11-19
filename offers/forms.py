from django.forms import Form
from .models import Offer, AnswerRequest


class OfferForm(Form):
    class Meta:
        model = Offer
        fields = ['offer_title',
                  'offer_address',
                  # 'offer_date',
                  # 'offer_id_user'
                  ]


class AnsReqForm(Form):
    class Meta:
        model = AnswerRequest
        fields = ['answer_request_id_user',
                  'answer_request_id_offer',
                  'answer_request_status',
                  ]

