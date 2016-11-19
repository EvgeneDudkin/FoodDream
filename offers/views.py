from django.shortcuts import render, redirect
from django.http.response import HttpResponse, Http404
from django.template.context_processors import csrf
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.core.paginator import Paginator

from offers.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import auth


def basic_one(request):
    view = "basic_one"
    html = "<html><header></header><body>Это %s вьюха</body></html>" % view
    return HttpResponse(html)


def offers(request):
    all_offers = Offer.objects.all()
    # current_page = Paginator(all_articles, 2)
    return render_to_response('offers.html', {
        # 'offers': all_offers.page(page_number),
        # 'username': auth.get_user(request).username
        'offers': all_offers,
        'username': auth.get_user(request).username
    })


def requests(request):
    all_requests = Request.objects.all()
    return render_to_response('requests.html', {
        'requests': all_requests,
        'username': auth.get_user(request).username
    })


def answers(request):
    all_answers = Answer.objects.all()
    return render_to_response('answers.html', {
        'answers': all_answers,
        'username': auth.get_user(request).username
    })


def my_offers(request):
    all_my_offers = Answer.objects.all()
    return render_to_response('my_offers.html', {
        'answers': all_my_offers,
        'username': auth.get_user(request).username
    })
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
#
#
# def addcomment(request, article_id=1):
#     if request.POST and ('pause' not in request.session):
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.comments_article = Article.objects.get(id=article_id)
#             form.save()
#             request.session.set_expiry(60)
#             request.session['pause'] = True
#     return redirect('/articles/get/%s/' % article_id)
