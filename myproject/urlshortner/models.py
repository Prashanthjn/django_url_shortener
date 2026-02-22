from django.db import models

# Create your models here.

from django.db import models

class Url(models.Model):
    long_url=models.URLField()
    short_url=models.CharField(max_length=13,unique=True)

    def __str__(self):
        return self.short_url