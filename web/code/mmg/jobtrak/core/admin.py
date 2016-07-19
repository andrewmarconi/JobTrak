from django.contrib import admin
from JobTrak.admin import JobTrakAdmin
from mmg.jobtrak.links.models import *
from mmg.jobtrak.core.models import *
#from pprint import pprint

class CompanyLocationAdmin(admin.ModelAdmin):
    list_display=('name','company','note')
    list_filter=['company']

class CompanyLocationInline(admin.TabularInline):
    model=CompanyLocation
    extra=1

class WebLinkForContactInline(admin.TabularInline):
    model=WebLinkAccount
    extra=1
    exclude=('company','company_location')

class WebLinkForCompanyInline(admin.TabularInline):
    model=WebLinkAccount
    extra=1
    exclude=('contact','company_location')

class WebLinkForCompanyLocationInline(admin.TabularInline):
    model=WebLinkAccount
    extra=1
    exclude=('contact','company')

class JobStatusAdmin(admin.ModelAdmin):
    list_display=['order_id','name','get_num_jobs']

class CompanyAdmin(admin.ModelAdmin):
    list_display=['name','company_type','note']
    fieldsets=[
        (None, {'fields': ['name','note','company_type']}),
    ]
    list_filter=['company_type']
    inlines=[CompanyLocationInline, WebLinkForCompanyInline]
    class Meta:
        verbose_name='Company'
        verbose_name_plural='Companies'

class ContactHistoryInline(admin.TabularInline):
    model=ActionHistory
    extra=1

class ContactAdmin(admin.ModelAdmin):
    list_display=('get_name_lastfirst','company','title','contact_type','get_last_contact')
    list_filter=['company__company','contact_type']
    fieldsets=[
        (None, {
            'fields':
                ['first_name','last_name','title','company','contact_type','birthday','note']}),
        ('Contact', {
            'fields':
                ['email_address','office_tel','mobile_tel','office_fax']}),
    ]
    inlines=[WebLinkForContactInline, ContactHistoryInline]

# class JobListingPersonInline(admin.TabularInline):
#     model=JobListingPerson
#     extra=1
#     def get_filters(self, obj):
#         return (('joblisting', dict(<filters>)))
#
class JobListingPersonInline(admin.TabularInline):
    model=JobListingPerson
    extra=1

class JobListingHistoryInline(admin.TabularInline):
    model=ActionHistory
    extra=1
# BUG - Issue #15 - Filter user list to only those who are associated with joblisting
#     def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
#         field = super(JobListingHistoryInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
#
#         if db_field.name == 'who':
#             if request._obj_ is not None:
#                 # print "[YES]"
#                 # print db_field
#                 # pprint(request._obj_.)
#                 field.queryset = field.queryset.filter(joblistingperson = request._obj_)
# #                field.queryset = field.queryset.filter(id__exact = request._obj_)
#             else:
#                 print "[NO]"
#                 field.queryset = field.queryset.none()
#         return field

class JobListingAdmin(admin.ModelAdmin):
    list_display=('name','company','status','get_last_touch')
    list_filter=['company__company']
    fieldsets=[
        (None, {
            'fields':
                ['name','company','date_posted','status','description','sourceURL']
        }),
    ]
#    inlines=[JobListingHistoryInline]
    inlines=[JobListingPersonInline,JobListingHistoryInline]
    # def get_form(self, request, obj=None, **kwargs):
    #    request._obj_ = obj
    #    return super(JobListingAdmin, self).get_form(request, obj, **kwargs)



# class LimitedAdminInlineMixin(object):
#     """
#     InlineAdmin mixin limiting the selection of related items according to
#     criteria which can depend on the current parent object being edited.
#
#     A typical use case would be selecting a subset of related items from
#     other inlines, ie. images, to have some relation to other inlines.
#
#     Use as follows::
#
#         class MyInline(LimitedAdminInlineMixin, admin.TabularInline):
#             def get_filters(self, obj):
#                 return (('<field_name>', dict(<filters>)),)
#
#     """
#
#     @staticmethod
#     def limit_inline_choices(formset, field, empty=False, **filters):
#         """
#         This function fetches the queryset with available choices for a given
#         `field` and filters it based on the criteria specified in filters,
#         unless `empty=True`. In this case, no choices will be made available.
#         """
#         assert formset.form.base_fields.has_key(field)
#
#         qs = formset.form.base_fields[field].queryset
#         if empty:
#             logger.debug('Limiting the queryset to none')
#             formset.form.base_fields[field].queryset = qs.none()
#         else:
#             qs = qs.filter(**filters)
#             logger.debug('Limiting queryset for formset to: %s', qs)
#
#             formset.form.base_fields[field].queryset = qs
#
#     def get_formset(self, request, obj=None, **kwargs):
#         """
#         Make sure we can only select variations that relate to the current
#         item.
#         """
#         formset = \
#             super(LimitedAdminInlineMixin, self).get_formset(request,
#                                                              obj,
#                                                              **kwargs)
#
#         for (field, filters) in self.get_filters(obj):
#             if obj:
#                 self.limit_inline_choices(formset, field, **filters)
#             else:
#                 self.limit_inline_choices(formset, field, empty=True)
#
#         return formset
#
#     def get_filters(self, obj):
#         """
#         Return filters for the specified fields. Filters should be in the
#         following format::
#
#             (('field_name', {'categories': obj}), ...)
#
#         For this to work, we should either override `get_filters` in a
#         subclass or define a `filters` property with the same syntax as this
#         one.
#         """
#         return getattr(self, 'filters', ())
#
#


JobTrakAdmin.register(Company, CompanyAdmin)
JobTrakAdmin.register(ContactType)
JobTrakAdmin.register(ActionHistory)
JobTrakAdmin.register(Country)
#JobTrakAdmin.register(StateProvince)
JobTrakAdmin.register(Address)
JobTrakAdmin.register(CompanyLocation, CompanyLocationAdmin)
JobTrakAdmin.register(CompanyType)

JobTrakAdmin.register(Contact, ContactAdmin)

JobTrakAdmin.register(JobStatus, JobStatusAdmin)
JobTrakAdmin.register(JobListing, JobListingAdmin)
JobTrakAdmin.register(JobListingRole)
JobTrakAdmin.register(JobListingPerson)
