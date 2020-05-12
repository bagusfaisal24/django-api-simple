from django.db import models

class Buku(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=50)
    pengarang = models.TextField(max_length= 50)

    def __str__(self):
        return self.id