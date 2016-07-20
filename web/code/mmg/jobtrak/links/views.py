from django.shortcuts import render, redirect
from django.template import *
from django.conf import settings
from django.template import Template, Library
from django_tables2 import RequestConfig
from django.core.urlresolvers import reverse
from mmg.jobtrak.core import *
from mmg.jobtrak.links.models import *
from mmg.jobtrak.links.tables import *
register = Library()


def index(request):
    if not request.user.is_authenticated():
        return redirect(reverse('public.views.index'))
    else:
        jbtable = JobBoardTable(JobBoard.objects.all())
        RequestConfig(request).configure(jbtable)
        context = {"jbtable": jbtable}
        return render(request, 'jobtrak.link/index.html', context)
