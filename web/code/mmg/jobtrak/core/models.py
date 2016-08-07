from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext, ugettext_lazy
from datetime import datetime
from django.contrib.humanize.templatetags.humanize import naturaltime, ordinal, intcomma, naturalday
from mmg.jobtrak.contact.models import *
from mmg.jobtrak.links.models import *

class JobListingRole(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=128)
    class Meta:
        verbose_name=ugettext_lazy('Role')
        verbose_name_plural=ugettext_lazy('Roles')
    def __unicode__(self):
        return self.name

class JobStatus(models.Model):
    """JobStatus"""
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=128)
    order_id=models.IntegerField(verbose_name=ugettext_lazy('Order'))
    def get_num_jobs(self):
        ct = JobListing.objects.filter(status__exact=self).count()
        return ct
    get_num_jobs.short_description=ugettext_lazy('Jobs')
    class Meta:
        verbose_name=ugettext_lazy('Job Status')
        verbose_name_plural=ugettext_lazy('Job Statuses')
        ordering=['order_id',]
    def __unicode__(self):
        return self.name

class JobListing(models.Model):
    """(Modelname description)"""
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=128)
    status=models.ForeignKey(JobStatus, blank=True, null=True)
    ref_by=models.ForeignKey(Contact, blank=True, null=True, verbose_name=ugettext_lazy('Referred By'))
    sourceURL=models.URLField(blank=True, null=True)
    sourceSite=models.ForeignKey(JobBoard, blank=True, null=True, verbose_name=ugettext_lazy('Source'))
    date_posted=models.DateField(blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    company=models.ForeignKey(CompanyLocation, blank=True, null=True)

    def get_last_touch(self):
        rv=ActionHistory.objects.filter(joblisting__exact=self).latest().when
        return rv
    get_last_touch.short_description="Last Contact"

    class Meta:
        verbose_name='Job Listing'
        verbose_name_plural='Job Listings'

    def __unicode__(self):
        return self.name

class JobListingPerson(models.Model):
    id=models.AutoField(primary_key=True)
    # Translators: Name of a 'contact' in a job listing
    contact=models.ForeignKey(Contact, verbose_name=ugettext_lazy("Contact"))
    role=models.ForeignKey(JobListingRole, verbose_name=ugettext_lazy("Role"))
    # Translators: Reference to a single job listing
    joblisting=models.ForeignKey(JobListing, verbose_name=ugettext_lazy("Job Listing"))
    note=models.CharField(max_length=255, blank=True, null=True, verbose_name=ugettext_lazy("Note"))
    class Meta:
        verbose_name=ugettext_lazy('Associated Person')
        verbose_name_plural=ugettext_lazy('Associated People')
    def __unicode__(self):
        return ' - '.join([self.contact.first_name,self.role.name])

class ActionHistory(models.Model):
    """(Modelname description)"""
    id=models.AutoField(primary_key=True)
    when=models.DateTimeField(default=datetime.now, blank=True, null=True, verbose_name=ugettext_lazy("When"))
    who=models.ForeignKey(Contact, blank=True, null=True, verbose_name=ugettext_lazy("Contact"))
    joblisting=models.ForeignKey(JobListing, blank=True, null=True, verbose_name=ugettext_lazy("Job Listing"))
    note=models.TextField(blank=True, default='', verbose_name=ugettext_lazy("Note"))
    class Meta:
        verbose_name=ugettext_lazy('History Item')
        verbose_name_plural=ugettext_lazy('History Items')
        get_latest_by='when'
    def __unicode__(self):
        # return ' '.join([self.who.first_name,self.who.last_name,self.when.strftime('%Y-%m-%d %H:%M')])
        return self.when.strftime('%Y-%m-%d %H:%M')
