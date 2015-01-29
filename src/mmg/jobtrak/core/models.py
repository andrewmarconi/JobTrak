from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext
from datetime import datetime
from django.contrib.humanize.templatetags.humanize import naturaltime, ordinal, intcomma, naturalday 
from mmg.jobtrak.contact.models import *
from mmg.jobtrak.links.models import *


# class StateProvince(models.Model):
#     """Model for states and provinces"""
#     iso_code=models.CharField(max_length=3, primary_key=True)
#     name=models.CharField(max_length=55, blank=False)
#     country=models.ForeignKey(Country, to_field="iso_code")
#     class Meta:
#         verbose_name="State or province"
#         """the admin site dies when I try this. apparantely support for
#            ordering by foreign keys is broken. uncomment when fixed
#            ordering=["-country", "name"]
#         """
#     def __unicode__(self):
#         return self.name

class JobListingRole(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=128)
    class Meta:
        verbose_name=ugettext('Role')
        verbose_name_plural=ugettext('Roles')
    def __unicode__(self):
        return self.name

class JobStatus(models.Model):
    """JobStatus"""
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=128)
    order_id=models.IntegerField(verbose_name="Order")
    def get_num_jobs(self):
        ct = JobListing.objects.filter(status__exact=self).count()
        return ct
    get_num_jobs.short_description="Jobs"
    class Meta:
        verbose_name='Job Status'
        verbose_name_plural='Job Statuses'
        ordering=['order_id',]
    def __unicode__(self):
        return self.name
    
class JobListing(models.Model):
    """(Modelname description)"""
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=128)
    status=models.ForeignKey(JobStatus, blank=True, null=True)
    ref_by=models.ForeignKey(Contact, blank=True, null=True, verbose_name=u'Referred By')
    sourceURL=models.URLField(blank=True, null=True)
    date_posted=models.DateField(blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    company=models.ForeignKey(CompanyLocation, blank=True, null=True)
    class Meta:
        verbose_name='Job Listing'
        verbose_name_plural='Job Listings'
    def __unicode__(self):
        return self.name

class JobListingPerson(models.Model):
    id=models.AutoField(primary_key=True)
    contact=models.ForeignKey(Contact, verbose_name="Contact")
    role=models.ForeignKey(JobListingRole, verbose_name="Role")
    joblisting=models.ForeignKey(JobListing, verbose_name="Job Listing")
    note=models.CharField(max_length=255, blank=True, null=True, verbose_name="Note")
    class Meta:
        verbose_name='Associated Person'
        verbose_name_plural='Associated People'
    def __unicode__(self):
        return ' - '.join([self.contact.first_name,self.role.name])
        
class ActionHistory(models.Model):
    """(Modelname description)"""
    id=models.AutoField(primary_key=True)
    when=models.DateTimeField(default=datetime.now, blank=True, null=True, verbose_name="When")
    who=models.ForeignKey(Contact, blank=True, null=True, verbose_name="Contact")
    joblisting=models.ForeignKey(JobListing, blank=True, null=True, verbose_name="Job Listing")
    note=models.TextField(blank=True, default='', verbose_name="Note")
    class Meta:
        verbose_name='History Item'
        verbose_name_plural='History Items'
        get_latest_by='when'
    def __unicode__(self):
        return ' '.join([self.who.first_name,self.who.last_name,self.when.strftime('%Y-%m-%d %H:%M')])