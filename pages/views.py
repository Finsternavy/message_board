from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# We need a HomePageView and an AboutPageView
# Consider: all the different things needed for these to become accessible through our web browser

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'