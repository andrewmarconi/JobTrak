from django.shortcuts import render, redirect, get_object_or_404
from django.template import *
from django.conf import settings
from django.template import Template, Library
from django_tables2 import RequestConfig
from django.core.urlresolvers import reverse
from mmg.jobtrak.core.tables import *
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
        jtable = JobListingTable(JobListing.objects.all())
        jtable.paginate(page=request.GET.get('page',1), per_page=50)
        RequestConfig(request).configure(jtable)
        context = {"jtable": jtable}
        return render(request, 'jobtrak.core/job_list.html', context)

def job_detail(request, id):
    if not request.user.is_authenticated():
        return redirect(reverse('public.views.index'))
    else:
        job = get_object_or_404(JobListing, id=id)
        context = {"job": job}
        return render(request, 'jobtrak.core/job_detail.html', context)

def contact_list(request):
    if not request.user.is_authenticated():
        return redirect(reverse('public.views.index'))
    else:
        context = {}
        return render(request, 'jobtrak.core/contact_list.html', context)
