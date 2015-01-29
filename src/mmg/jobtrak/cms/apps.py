from django.apps import AppConfig
from django.utils.translation import ugettext, ugettext_lazy

class LocalConfig(AppConfig):    
    name="mmg.jobtrak.cms"
    # Translators: Admin Backend - Name of the CMS app (appears in the header bar)
    verbose_name=ugettext_lazy("CMS")
    