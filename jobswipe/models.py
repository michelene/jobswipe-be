from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import JSONField


class Job(models.Model):
    ghj_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=100, default='')
    company = models.CharField(max_length=100, default='')
    data = JSONField()

    def __str__(self):
        return self.ghj_id


class User(AbstractUser):
    pass

    def __str__(self):
        return self.email


class Saved(models.Model):
    title = models.CharField(max_length=100, default="Saved Jobs")
    jobs = models.ManyToManyField(Job)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        unique=True
    )

    def __str__(self):
        return "%s Saved" % self.owner.username


class Unreviewed(models.Model):
    title = models.CharField(
        max_length=100, default="Unreviewed Jobs")
    jobs = models.ManyToManyField(Job)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        unique=True
    )

    def __str__(self):
        return "%s Unreviewed" % self.owner.username
