from external_urls.signals import external_click
from django.dispatch import receiver
from django.utils import timezone
from mmg.jobtrak.links.models import *

@receiver(external_click)
def external_click_fallback(sender, url, ip, **kwargs):
    link = JobBoard.objects.get(url=url)
    link.last_click = timezone.now()
    link.save()
