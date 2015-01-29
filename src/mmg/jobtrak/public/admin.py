from django.contrib import admin
from JobTrak.admin import JobTrakAdmin
#from mmg.jobtrak.links.models import *
#from mmg.jobtrak.core.models import *
from mmg.jobtrak.public.models import *

JobTrakAdmin.register(PageContent)
