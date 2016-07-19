from django.apps import AppConfig
from django.utils.translation import ugettext, ugettext_lazy

class LocalConfig(AppConfig):    
    name="mmg.jobtrak.util"
    # Translators: Admin Backend - Name of Util app (appears in the header bar)
    verbose_name=ugettext_lazy("Utility")
    