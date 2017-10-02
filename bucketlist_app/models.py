"""Definition of models for the application."""
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Bucketlist(models.Model):
    """Model definition for Bucketlist."""
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "BucketList: {}".format(self.name)


class Items(models.Model):
    """Model definition for Items."""
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    done = models.BooleanField(default=False)
    bucketlist = models.ForeignKey(Bucketlist, on_delete=models.CASCADE)

    def __str__(self):
        return "Items: {}".format(self.name)
