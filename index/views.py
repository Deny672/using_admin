from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

from index.models import Text

class IndexView(ListView):
    template_name = 'index.html'
    model = Text
    ordering = ('-id')