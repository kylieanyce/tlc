from django.db import models


class Email(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    message = models.TextField()
    design = models.BooleanField(default=False)
    installation = models.BooleanField(default=False)
    maintenance = models.BooleanField(default=False)
    hardscaping = models.BooleanField(default=False)
    sod = models.BooleanField(default=False)
    leaf_removal = models.BooleanField(default=False)
    pots = models.BooleanField(default=False)
