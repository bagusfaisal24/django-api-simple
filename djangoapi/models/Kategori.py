from django.db import models

class Kategori(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField