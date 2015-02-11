import django_tables2 as tables
from django_tables2.utils import A
from mmg.jobtrak.contact.models import *

class ContactTable(tables.Table):
    get_name_lastfirst = tables.LinkColumn('contact:contact_detail', args=[A('pk')], order_by=('last_name','first_name'), verbose_name="Name" )
    title = tables.Column(verbose_name="Title")
    company = tables.Column(verbose_name="Company")
    contact_type = tables.Column(verbose_name="Contact Type")
    get_last_contact = tables.DateTimeColumn()

    class Meta:
        model=Contact
        attrs = {"class": "table table-condensed"}
        fields = ('get_name_lastfirst','title','company','get_last_contact')
