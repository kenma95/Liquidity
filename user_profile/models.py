from __future__ import unicode_literals


from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class ConcreteUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    quota = models.IntegerField()


class ProjectUser(models.Model):
    user = models.ForeignKey( 'user_profile.ConcreteUser',        on_delete=models.CASCADE,)
    name = models.CharField(max_length=100,)
    size = models.IntegerField()
