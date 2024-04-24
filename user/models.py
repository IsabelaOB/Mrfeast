from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    restrictions = models.JSONField()

    def __str__(self):
        return self.name

