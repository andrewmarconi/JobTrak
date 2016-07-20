import django_tables2 as tables
from django_tables2.utils import A
from mmg.jobtrak.links.models import *
from django.utils.translation import ugettext_lazy as _

# class ContactTable(tables.Table):
#     get_name_lastfirst = tables.LinkColumn(
#         'contact:contact_detail',
#         args=[A('pk')],
#         order_by=('last_name','first_name'),
#         verbose_name="Name"
#     )
#     title = tables.Column(verbose_name="Title")
#     company = tables.Column(verbose_name="Company")
#     contact_type = tables.Column(verbose_name="Contact Type")
#     get_last_contact = tables.DateTimeColumn()


class JobBoardTable(tables.Table):
    name = tables.Column()
    url = tables.URLColumn()
    note = tables.Column(verbose_name="Description")

    class Meta:
        model = JobBoard
        attrs = {
            "class": "table table-condensed"
        }
        fields = ('name','note','url',)
