from django.db import models

class PageContent(models.Model):
    id = models.AutoField(primary_key=True)
    class Meta:
        verbose_name='Page Content'
        verbose_name_plural='Page Content'
    def __unicode__(self):
        return u'PageContent'
        