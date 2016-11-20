import datetime
from _threading_local import local

from django.shortcuts import render, redirect
from django.http.response import HttpResponse, Http404
from django.template import RequestContext
from django.template.context_processors import csrf
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.core.paginator import Paginator

from offers.forms import OfferForm, AnsReqForm
from offers.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt, csrf_protect


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
    all_requests = AnswerRequest.objects.select_related('answer_request_id_offer__offer_id')\
        .select_related('answer_request_id_offer__offer_id_user__user_username')
    values = all_requests.values('answer_request_id_offer__offer_id_user__username',
                                 'answer_request_id_offer__offer_title',
                                 'answer_request_status', 'id')
    # print(values)
    return render_to_response('requests.html', {
        'requests': values,
        'username': auth.get_user(request).username
    })


def answers(request):
    all_answers = AnswerRequest.objects.select_related()
    # print(all_answers.get())
    return render_to_response('answers.html', {
        'answers': all_answers,
        'username': auth.get_user(request).username
    })


def my_offers(request):
    offer_form = OfferForm
    args = {}
    args.update(csrf(request))
    args['offer.id'] = 1
    args['form'] = offer_form
    args['my_offers'] = Offer.objects.all()
    # print(Offer.objects.all())
    return render_to_response('my_offers.html', args)


#
#
# def article(request, article_id=1):
#     comment_form = CommentForm
#     args = {}
#     args.update(csrf(request))
#     args['article'] = Article.objects.get(id=article_id)
#     args['comments'] = Comments.objects.filter(comments_article_id=article_id)
#     args['form'] = comment_form
#     args['username'] = auth.get_user(request).username
#     return render_to_response('article.html', args)
#
#
# def addlike(request, article_id):
#     try:
#         if article_id in request.COOKIES:
#             redirect('/')
#         else:
#             artcle = Article.objects.get(id=article_id)
#             artcle.article_likes += 1
#             artcle.save()
#             response = redirect('/')
#             response.set_cookie(article_id, 'test')
#             return response
#     except ObjectDoesNotExist:
#         raise Http404
#     return redirect('/')


def addoffer(request):
    if request.POST:
        form = OfferForm(request.POST)
        if form.is_valid():
            # offer = form.save(commit=False)
            title = request.POST.get('offer_title', '')

            address = request.POST.get('offer_address', '')
            # date = request.POST.get('offer_date', '')
            date = datetime.datetime.today()
            id_user = auth.get_user(request)
            # print(id_user)
            form = Offer(offer_title=title,
                         offer_address=address,
                         offer_date=date,
                         offer_id_user=id_user
                         )
            form.save()
    # else:
    #     form = OfferForm()
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
        # offer2_id = Offer.objects.get(id=offer_id).id
        status = 0
        form = AnswerRequest(answer_request_id_user=User(user_active_id),
                             answer_request_id_offer=Offer(offer_id),
                             answer_request_status=status,
                             )
        form.save()

    return render(request, 'offers.html', {'form': form})


from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@csrf_exempt
def approveoffer(request, request_id):
    # print(request_id)
    form = AnsReqForm(request.POST)
    # if form.is_valid():
    user_active_id = auth.get_user(request).id
    user_b = AnswerRequest.objects.get(id=request_id).answer_request_id_user
    # offer2_id = Offer.objects.get(id=request_id).id
    status = 1
    # AnswerRequest.objects.update(
    #         # answer_request_id_user=User(user_active_id),
    #         # answer_request_id_offer=Offer(offer_id),
    #         id=request_id,
    #         answer_request_status=status
    #     )
    record = AnswerRequest.objects.get(id= request_id)
    record.answer_request_status = status
    record.save()
    return render(request, 'offers.html',  {'form': form})


# @method_decorator(csrf_exempt, name='dispatch')
# def approveoffer(request, request_id):
#     form = AnsReqForm(request.POST)
#     if form.is_valid():
#         record = AnswerRequest.object.get(id=request_id)
#         record.answer_request_status = 1
#         record.save()
#         # form = AnswerRequest(answer_request_id_user=User(user_active_id),
#         #                      answer_request_id_offer=Offer(offer_id),
#         #                      answer_request_status=status,
#         #                      )
#         # form.save()

    # return render(request, 'offers.html')