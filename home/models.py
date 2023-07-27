from django.db import models


class Texto(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.TextField()