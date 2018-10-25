from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.mail import send_mail
from .models import Post,Letter,Word,About,Services,Learn
from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import strip_tags
from .forms import NameForm
# Create your views here.


def index(request):
    return render(request, 'polls/index.html')


def header(request):
    return render(request, 'polls/header.html')

def about(request):
    about_list = About.objects.all()
    return render(request, 'polls/about.html', context = {'about_list':about_list})

def xidmet(request):
    #xidmet_list = Services.objects.all()
    xidmet_list = Services.objects.values()
    context = {'xidmet_list':xidmet_list}
    return render(request, 'polls/xidmet.html', context )

def contact(request):
    return render(request, 'polls/contact.html')

def dictionary(request):
    word_l = Letter.objects.all()
    word_e = Word.objects.all()
    context = {'word_l':word_l,'word_e':word_e}
    return render(request, 'polls/luget.html', context)

def learn(request):
    title = Learn.objects.values()
    #title_c = Learn.objects.values('content_l')
    context = {'title':title}
    return render(request, 'polls/oyren.html', context)









