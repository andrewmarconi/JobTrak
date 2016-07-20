from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import pgettext_lazy
from django.contrib.humanize.templatetags.humanize import naturaltime, ordinal, intcomma, naturalday
from mmg.jobtrak.core.models import *
from mmg.jobtrak.contact.models import *

class WebLinkType(models.Model):
    """Social Media Connections"""
    id=models.AutoField(primary_key=True)
    name=models.CharField(_("Name"), max_length=128)
    note=models.CharField(_("Note"), max_length=255, blank=True, null=True)
    base_url=models.URLField(_("Base URL"), blank=True, null=True)
    def get_account_count(self):
        # TODO get_account_count method
        return 0
    get_account_count.short_description=_('Number of Accounts')

    class Meta:
        verbose_name=_('Web Link Type')
        verbose_name_plural=_('Web Link Types')
    def __unicode__(self):
        return self.name

class WebLinkAccount(models.Model):
    id=models.AutoField(primary_key=True)
    web_link_type=models.ForeignKey(WebLinkType)
    contact=models.ForeignKey(Contact, null=True, blank=True, verbose_name=ugettext_lazy('Contact'))
    company=models.ForeignKey(Company, null=True, blank=True, verbose_name=ugettext_lazy('Company'))
    company_location=models.ForeignKey(CompanyLocation, null=True, blank=True, verbose_name=ugettext_lazy('Company Location'))

    local_url_data=models.CharField(max_length=128, verbose_name=ugettext_lazy('Account'))
    class Meta:
        verbose_name=ugettext_lazy('Web Link Account')
        verbose_name_plural=ugettext_lazy('Web Link Accounts')
    def __unicode__(self):
        return ' - '.join([self.web_link_type.name,self.local_url_data])

class JobBoard(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(_("Name"), max_length=128)
    note = models.TextField(_("Note"), blank=True)
    url = models.URLField(_("URL"))
    class Meta:
        verbose_name=_("Job Board")
        verbose_name_plural=(_("Job Boards"))
    def __unicode__(self):
        return self.name
