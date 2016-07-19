from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator
from django.utils.translation import ugettext, ugettext_lazy
from django.contrib.humanize.templatetags.humanize import naturaltime, ordinal, intcomma, naturalday
from mmg.jobtrak.core.models import *
from mmg.jobtrak.contact.models import *

class WebLinkType(models.Model):
    """Social Media Connections"""
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=128, verbose_name=ugettext_lazy('Name'))
    note=models.CharField(max_length=255, blank=True, null=True, verbose_name=ugettext_lazy('Note'))
    base_url=models.URLField(blank=True, null=True, verbose_name='Base URL')
    def get_account_count(self):
        return 0
    get_account_count.short_description=ugettext_lazy('Number of Accounts')

    class Meta:
        verbose_name=ugettext_lazy('Web Link Type')
        verbose_name_plural=ugettext_lazy('Web Link Types')
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
