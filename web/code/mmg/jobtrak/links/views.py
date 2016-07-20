from django.shortcuts import render, redirect
from django.template import *
from django.conf import settings
from django.template import Template, Library
from django.core.urlresolvers import reverse
from mmg.jobtrak.core import *
from mmg.jobtrak.links import *

def index(request):
    if not request.user.is_authenticated():
        return redirect(reverse('public.views.index'))
    else:
        context = {}
        return render(request, 'jobtrak.link/index.html', context)
