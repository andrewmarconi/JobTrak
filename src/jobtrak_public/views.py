from django.shortcuts import render
from django.template import *
from django.conf import settings
from django.template import Template, Library
from jobtrak_public import *
register = Library()

def index(request):
    context = {}
    return render(request, 'jobtrak_public/index.html', context)