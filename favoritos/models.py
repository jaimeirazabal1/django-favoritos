from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/4.1/topics/db/models/
# https://docs.djangoproject.com/en/4.1/ref/models/fields/
class Favoritos(models.Model):
    nombre = models.CharField(max_length=50, blank=True)
    url = models.URLField()