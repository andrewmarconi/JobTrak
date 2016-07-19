import os
from django.db import models
from datetime import datetime
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    """
    User profiles, tied one-to-one with the user auth model.
    """
    user = models.OneToOneField(User, verbose_name="Account")

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
    def __unicode__(self):
        return " ".join([self.user.first_name, self.user.last_name])
