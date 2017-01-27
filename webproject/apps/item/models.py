from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.name
