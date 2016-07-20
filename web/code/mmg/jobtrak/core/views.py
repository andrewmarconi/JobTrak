from django.shortcuts import render, redirect
from django.template import *
from django.conf import settings
from django.template import Template, Library
from django.core.urlresolvers import reverse
from mmg.jobtrak.core import *
register = Library()

def index(request):
    if not request.user.is_authenticated():
        return redirect(reverse('public.views.index'))
    else:
        context = {}
        return render(request, 'jobtrak.core/index.html', context)

def job_list(request):
    if not request.user.is_authenticated():
        return redirect(reverse('public.views.index'))
    else:
        context = {}
        return render(request, 'jobtrak.core/job_list.html', context)

def contact_list(request):
    if not request.user.is_authenticated():
        return redirect(reverse('public.views.index'))
    else:
        context = {}
        return render(request, 'jobtrak.core/contact_list.html', context)
