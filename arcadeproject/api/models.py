from django.db import models


# Create your models here.
class Pair(models.Model):
    key = models.CharField(max_length=255)
    value = models.IntegerField()

    def __str__(self):
        return f"{self.key} = {self.value}"
