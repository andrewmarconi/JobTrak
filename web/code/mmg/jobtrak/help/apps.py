from django.apps import AppConfig
from django.utils.translation import ugettext, ugettext_lazy

class LocalConfig(AppConfig):    
    name="mmg.jobtrak.help"
    # Translators: Admin Backend - Name of Help app (appears in the header bar)
    verbose_name=ugettext_lazy("Help")
    