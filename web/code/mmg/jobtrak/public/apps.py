from django.apps import AppConfig
from django.utils.translation import ugettext, ugettext_lazy

class LocalConfig(AppConfig):    
    name="mmg.jobtrak.public"
    # Translators: Admin Backend - Name of Public app (appears in the header bar)
    verbose_name=ugettext_lazy("Public")
    