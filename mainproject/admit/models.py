from django.db import models

# Create your models here.
class Universitiy(models.Model):
    name = models.CharField(max_length=300)