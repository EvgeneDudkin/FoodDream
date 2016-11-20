import datetime

from django.contrib import auth
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

from offers.forms import OfferForm, AnsReqForm
from offers.models import *


def basic_one(request):
    view = "basic_one"
    html = "<html><header></header><body>Это %s вьюха</body></html>" % view
    return HttpResponse(html)


def offers(request):
    all_offers = Offer.objects.all()
    return render_to_response('offers.html', {
        'offers': all_offers,
        'username': auth.get_user(request).username
    })


def requests(request):
    all_requests = (AnswerRequest.objects.select_related('answer_request_id_offer__offer_id')
                    .select_related('answer_request_id_offer__offer_id_user__user_username')
                    .filter(answer_request_id_offer__offer_id_user=auth.get_user(request).id))

    values = all_requests.values('answer_request_id_user__username',
                                 'answer_request_id_offer__offer_title',
                                 'answer_request_status', 'id')
    for value in values:
        if value['answer_request_status'] == -1:
            value['answer_request_status'] = "отказано"
        elif value['answer_request_status'] == 0:
            value['answer_request_status'] = "рассматривается"
        elif value['answer_request_status'] == 1:
            value['answer_request_status'] = "удовлетворено"

    return render_to_response('requests.html', {
                    'requests': values,
                    'username': auth.get_user(request).username})


def answers(request):
    all_answers = (AnswerRequest.objects
                   .select_related()
                   .filter(answer_request_id_user=auth.get_user(request).id))
    for answer in all_answers:
        if answer.answer_request_status == -1:
            answer.answer_request_id_offer.offer_address = "отказано в выдаче"
        elif answer.answer_request_status == 0:
            answer.answer_request_id_offer.offer_address = "рассматривается"
    return render_to_response('answers.html', {'answers': all_answers,
                                               'username': auth.get_user(request).username})


def my_offers(request):
    offer_form = OfferForm
    args = {}
    args.update(csrf(request))
    args['offer.id'] = 1
    args['form'] = offer_form
    args['my_offers'] = Offer.objects.filter(offer_id_user=auth.get_user(request).id)
    args['username'] = auth.get_user(request).username
    return render_to_response('my_offers.html', args)


def addoffer(request):
    if request.POST:
        form = OfferForm(request.POST)
        if form.is_valid():
            title = request.POST.get('offer_title', '')
            address = request.POST.get('offer_address', '')
            date = datetime.datetime.today()
            id_user = auth.get_user(request)
            form = Offer(offer_title=title,
                         offer_address=address,
                         offer_date=date,
                         offer_id_user=id_user)
            form.save()
    else:
        form = OfferForm()
    return render(request, 'offers.html', {'form': form})


def deloffer(request, offer_id):
    if request.POST:
        Offer.objects.filter(id=offer_id).delete()
    return render(request, 'offers.html')


@csrf_exempt
def needoffer(request, offer_id):
    form = AnsReqForm(request.POST)
    if form.is_valid():
        user_active_id = auth.get_user(request).id
        status = 0
        form = AnswerRequest(answer_request_id_user=User(user_active_id),
                             answer_request_id_offer=Offer(offer_id),
                             answer_request_status=status)
        form.save()

    return render(request, 'offers.html', {'form': form})


@csrf_exempt
def approveoffer(request, request_id):
    form = AnsReqForm(request.POST)
    status = 1
    record = AnswerRequest.objects.get(id=request_id)
    record.answer_request_status = status
    record.save()
    return render(request, 'offers.html', {'form': form})
