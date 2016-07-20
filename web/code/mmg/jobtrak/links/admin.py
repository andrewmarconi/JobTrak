from django.contrib import admin
from JobTrak.admin import JobTrakAdmin
from mmg.jobtrak.links.models import *
from mmg.jobtrak.core.models import *

class WebLinkAccountAdmin(admin.ModelAdmin):
    list_display=[
        'web_link_type', 'local_url_data', 'contact', 'company','company_location'
    ]

class WebLinkTypeAdmin(admin.ModelAdmin):
    list_display=[
        'name', 'note', 'base_url', 'get_account_count'
    ]

class JobBoardAdmin(admin.ModelAdmin):
    pass

JobTrakAdmin.register(WebLinkAccount, WebLinkAccountAdmin)
JobTrakAdmin.register(WebLinkType, WebLinkTypeAdmin)
JobTrakAdmin.register(JobBoard, JobBoardAdmin)
