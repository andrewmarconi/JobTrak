from django.apps import AppConfig
from django.utils.translation import ugettext, ugettext_lazy

class LocalConfig(AppConfig):
    name="mmg.jobtrak.contact"
    # Translators: Admin Backend - Name of Contact app (appears in the header bar)
    verbose_name=ugettext_lazy("Contact")
