from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomePageView(TemplateView):   # TODO-04 use built-in TemplateView
    template_name = 'home.html'

class AboutPageView(TemplateView):  # TODO-08 about
    template_name = 'about.html'
