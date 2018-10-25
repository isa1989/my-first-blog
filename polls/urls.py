from django.urls import path

from . import views
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    #path('', views.get_name, name='get_name'),
    path('head', views.header, name='header'),
    path('about', views.about, name='about'),
    path('xidmet', views.xidmet, name='xidmet'),
    path('contact', views.contact, name='contact'),
    path('luget', views.dictionary, name='dictionary'),
    path('learn', views.learn, name='learn'),

]



