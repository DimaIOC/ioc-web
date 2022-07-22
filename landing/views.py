from django.shortcuts import render
from django.utils.translation import gettext as _
from .models import *
from django.shortcuts import render
from django.template import RequestContext
from django.utils import translation


def try_or(fn, default):
    try:
        return fn()
    except:
        return default

def index(request):
    news = News.objects.all().order_by('-id')[:5]

    context = {
            "title": _('Головна'),
            "statics": Statics.objects.all(),
            "questions": Questions.objects.all(),
            "partners": PartnersImage.objects.all(),
            "news_large": news[0],
            "news": news[1:5]

    }
    return render(request=request,
                  template_name='landing/index.html',
                  context=context)

def aboute(request):
    reports = TypeReporting.objects.all()
    print(reports)
    context = {"title": _("Про нас"),
               "partners": PartnersImage.objects.all(),
               "team": TeamMember.objects.all(),
               "reports": TypeReporting.objects.all()
               }
    return render(request=request,
                  template_name='landing/about.html',
                  context=context)

def eservices(request):
    context = {"title": _("є-сервіси")}
    return render(request=request,
                  template_name='landing/e_services.html',
                  context=context)

def news(request):
    context = {"title": _("Новини"),
               "news": News.objects.all()}
    return render(request=request,
                  template_name='landing/news.html',
                  context=context)

def single_news(request, pk):
    single_news = News.objects.get(id__exact=pk)
    context = {'title': single_news.title,
               'single_news': single_news}
    return render(request=request,
                  template_name='landing/single-news.html',
                  context=context)

def team(request):
    team = TeamMember.objects.all()
    context = {"title": _("Керівництво"),
               "team": team,
                              }

    return render(request=request,
                  template_name='landing/team.html',
                  context=context)







