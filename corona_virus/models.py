from django.db import models

# Create your models here.

class API(models.Model):
    url = models.URLField(max_length=250)
    def __str__(self):
        return self.url
    