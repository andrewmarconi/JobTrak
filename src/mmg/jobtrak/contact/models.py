from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator
from pprint import pprint
from django.contrib.humanize.templatetags.humanize import naturaltime, ordinal, intcomma, naturalday 

class Country(models.Model):
    """Model for countries"""
    iso_code=models.CharField(max_length=2, primary_key=True)
    name=models.CharField(max_length=45, blank=False)
    class Meta:
        verbose_name_plural="Countries"
        ordering=["name", "iso_code"]
    def __unicode__(self):
        return self.name
        
class Address(models.Model):
    """Model to store addresses for accounts"""
    address_line1=models.CharField("Address line 1", max_length=45)
    address_line2=models.CharField("Address line 2", max_length=45,
        blank=True)
    city=models.CharField(max_length=50, blank=False)
    state_province=models.CharField("State/Province", max_length=40,
        blank=True)
    country=models.ForeignKey(Country, blank=False)
    postal_code=models.CharField("Postal Code", max_length=10, blank=True)
    class Meta:
        verbose_name_plural="Addresses"
        unique_together=("address_line1", "address_line2", "postal_code",
                           "city", "state_province", "country")
    def __unicode__(self):
        return "%s, %s, %s %s" % (self.address_line1, self.city, self.state_province,
                              str(self.country))


class CompanyType(models.Model):
    """CompanyType - defines company classifications"""
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=64)
    class Meta:
        verbose_name='Company Type'
        verbose_name_plural='Company Types'
    def __unicode__(self):
        return self.name
        
        
class Company(models.Model):
    """(Modelname description)"""
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=128)
    note=models.TextField(blank=True, null=True)
    company_type=models.ManyToManyField(CompanyType, blank=True, null=True)
    class Meta:
        verbose_name='Company'
        verbose_name_plural='Companies'
    def __unicode__(self):
        return self.name
        
        
class CompanyLocation(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=128)
    company=models.ForeignKey('Company', null=True)
    address=models.ForeignKey('Address', null=True, blank=True)
    note=models.TextField(blank=True, null=True)
    class Meta:
        verbose_name='Company Location'
        verbose_name_plural='Company Locations'
    def __unicode__(self):
        return ' - '.join([self.company.name,self.name])


class ContactType(models.Model):
    """(Modelname description)"""
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=128)
    class Meta:
        verbose_name='Contact Type'
        verbose_name_plural='Contact Types'
    def __unicode__(self):
        return self.name


class Contact(models.Model):
    """(Modelname description)"""
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=128)
    last_name=models.CharField(max_length=128)
    contact_type=models.ForeignKey('ContactType')
    title=models.CharField(max_length=128, blank=True, null=True)
    company=models.ForeignKey(CompanyLocation, blank=True, null=True)
    email_address=models.EmailField(blank=True)
    phone_regex=RegexValidator(regex=r'^\+?1?\d{9,15}$', 
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    office_tel=models.CharField(validators=[phone_regex], max_length=15, blank=True, verbose_name="Office Phone") 
    mobile_tel=models.CharField(validators=[phone_regex], max_length=15, blank=True, verbose_name="Mobile Phone")
    office_fax=models.CharField(validators=[phone_regex], max_length=15, blank=True, verbose_name="Office Fax")
    birthday=models.DateField(blank=True, null=True)
    note=models.TextField(blank=True)
    class Meta:
        verbose_name='Contact'
        verbose_name_plural='Contacts'
    def get_name_lastfirst(self):
        return ', '.join([self.last_name,self.first_name])
    get_name_lastfirst.short_description='Full Name'

    def get_name_firstlast(self):
        return ' '.join([self.first_name,self.last_name])
    get_name_firstlast.short_description='Full Name'
    
    def get_last_contact(self):
        try:
            obj=ActionHistory.objects.filter(who_id__exact=self.id).latest()
            rv=naturaltime(obj.when)
        except:
            rv=u'Never'
        return rv
    get_last_contact.short_description='Last Contact'
        
    def __unicode__(self):
        return ' '.join([self.company.company.name, u'-', self.company.name, u'-',self.first_name, self.last_name])
