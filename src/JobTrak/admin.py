from django.contrib import admin
from django.contrib import auth
from django.utils.translation import ugettext, ugettext_lazy

class LocalizedAdminSite(admin.AdminSite):
    # Translators: Admin Backend - Appears in the Browser Title Bar
    site_title = ugettext('manager_title')
    # Translators: Admin Backend - Appears in the Masthead
    site_header = ugettext('manager_header')
    # Translators: Admin Backend - Title ("H1") of the Home Page
    index_title = ugettext('manager_indextitle')

JobTrakAdmin = LocalizedAdminSite(name='JobTrakAdmin')
admin.autodiscover()
admin.register(auth)
