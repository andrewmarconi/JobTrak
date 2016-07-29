import django_tables2 as tables
from django_tables2.utils import A, Accessor
from mmg.jobtrak.links.models import *
from django.utils.translation import ugettext_lazy as _
import external_urls

class JobBoardTable(tables.Table):
    url = tables.TemplateColumn(
        '<a href="{% load external_urls %}{% external_url record.url %}" target="_blank">{{record.name}}</a>',
        verbose_name="Web Site", order_by=A('name')
        )
    last_click = tables.DateTimeColumn(
        format="D, j N",
        verbose_name="Last Visit",
        attrs={'td': {'nowrap': 'nowrap'}} )
    note = tables.Column(verbose_name="Description")

    class Meta:
        model = JobBoard
        attrs = { "class": "table" }
        fields = ('url','last_click','note',)
