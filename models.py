from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _


class Profile(models.Model):
    username = models.CharField(_('username'), max_length=100)

    def get_absolute_url(self):
        return reverse('profile_detail', args=[self.pk])

    def get_feed_url(self):
        return reverse('profile_feed', args=[self.pk])
