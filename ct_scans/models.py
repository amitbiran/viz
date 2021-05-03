from django.db import models

# Create your models here.
class Scan(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    hospitalId = models.CharField(max_length=255)
    uid = models.CharField(max_length=255)
    scanId = models.CharField(max_length=255)