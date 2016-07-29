from django.apps import AppConfig
from django.utils.translation import ugettext, ugettext_lazy

class LocalConfig(AppConfig):
    name="mmg.jobtrak.links"
    # Translators: Admin Backend - Name of Links app (appears in the header bar)
    verbose_name=ugettext_lazy("Web Links")

    def ready(self):
        import mmg.jobtrak.links.signals
