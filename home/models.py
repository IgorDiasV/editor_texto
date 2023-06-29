from django.db import models

# Create your models here.

class Texto(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.TextField()