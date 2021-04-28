from django.db import models

# Create your models here.

class FileModel(models.Model):
    doc = models.FileField(upload_to='media/')