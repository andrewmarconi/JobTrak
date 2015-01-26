from django.shortcuts import render
from django.template import *
from django.conf import settings
from django.template import Template, Library
from mmg.jobtrak.public import *
register = Library()

def index(request):
    context = {}
    return render(request, 'jobtrak.public/index.html', context)