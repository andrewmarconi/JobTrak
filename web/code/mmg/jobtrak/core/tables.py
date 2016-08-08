import django_tables2 as tables
from django_tables2.utils import A, Accessor
from mmg.jobtrak.core.models import *
from django.utils.translation import ugettext_lazy as _

class JobListingTable(tables.Table):
    name = tables.LinkColumn("core:job_detail",
                             kwargs={"id":A('id')},
                             text=lambda record: record.name,
                             verbose_name="Listing",
                             )
    company = tables.Column(verbose_name="Company")
    status = tables.Column(verbose_name="Status")
    date_posted = tables.DateTimeColumn(
        format="D, j N",
        verbose_name="Posted"
    )
    get_last_touch = tables.DateTimeColumn(
        format="D, j N",
        verbose_name="Updated"
    )
    can_be_remote = tables.BooleanColumn(
        verbose_name="Remote?"
    )
    class Meta:
        model = JobListing
        attrs = {"class":"table"}
        sequence = (
            "name",
            "company",
            "status",
            "sourceSite",
            "can_be_remote",
            "date_posted",
            "get_last_touch",
        )
        fields = {
            "name", "company", "status", "sourceSite", "can_be_remote", "date_posted", "get_last_touch",
        }
