import os
import uuid

from django.db import models
from django.utils import timezone

def get_new_token():
    return uuid.uuid1()

# Create your models here.
class SingleUseToken(models.Model):
    token           = models.CharField(default=get_new_token, max_length=200)
    create_date     = models.DateTimeField(default=timezone.now)
    expiry_date     = models.DateTimeField(default=timezone.now)

class File(models.Model):
    """This is a small demo using just two fields. The slug field is really not
    necessary, but makes the code simpler. ImageField depends on PIL or
    pillow (where Pillow is easily installable in a virtualenv. If you have
    problems installing pillow, use a more generic FileField instead.

    """
    file            = models.FileField()
    slug            = models.SlugField(max_length=50, blank=True)
    token           = models.ForeignKey(SingleUseToken, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.file.name

    @models.permalink
    def get_absolute_url(self):
        return ('upload-new', )

    def save(self, *args, **kwargs):
        self.slug = self.file.name
        super(File, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """delete -- Remove to leave file."""
        self.file.delete(False)
        super(File, self).delete(*args, **kwargs)
