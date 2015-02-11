from django.shortcuts import render, redirect
from django.template import *
from django.conf import settings
from django.template import Template, Library
from django_tables2   import RequestConfig
from django.core.urlresolvers import reverse
from mmg.jobtrak.contact.models import *
from mmg.jobtrak.contact.tables import *
register = Library()

def contact_list(request):
    if not request.user.is_authenticated():
        return redirect(reverse('public.views.list'))
    else:
        contact_table = ContactTable(Contact.objects.all())
        RequestConfig(request).configure(contact_table)
        context = {
            "contact_table": contact_table
        }
        return render(request, 'jobtrak.contact/list.html', context)

def contact_detail(request):
    if not request.user.is_authenticated():
        return redirect(reverse('public.views.list'))
    else:
        contact = {}
        return render(request, 'jobtrak.contact/detail.html', context)
