from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator
from pprint import pprint
from django.contrib.humanize.templatetags.humanize import naturaltime, ordinal, intcomma, naturalday 
from mmg.jobtrak.core.models import *
from mmg.jobtrak.contact.models import *

class WebLinkType(models.Model):
    """Social Media Connections"""
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=128)
    note=models.CharField(max_length=255, blank=True, null=True)
    base_url=models.URLField(blank=True, null=True)
    class Meta:
        verbose_name='Web Link Type'
        verbose_name_plural='Web Link Types'
    def __unicode__(self):
        return self.name
        
class WebLinkAccount(models.Model):
    id=models.AutoField(primary_key=True)
    web_link_type=models.ForeignKey(WebLinkType)

    contact=models.ForeignKey(Contact, null=True, blank=True)
    company=models.ForeignKey(Company, null=True, blank=True)
    company_location=models.ForeignKey(CompanyLocation, null=True, blank=True)

    local_url_data=models.CharField(max_length=128, verbose_name='Account')
    class Meta:
        verbose_name='Web Link Account'
        verbose_name_plural='Web Link Accounts'
    def __unicode__(self):
        return ' - '.join([self.web_link_type.name,self.local_url_data])
