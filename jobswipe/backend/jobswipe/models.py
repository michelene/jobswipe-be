from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import JSONField


class User(AbstractUser):
    pass

    def __str__(self):
        return self.email


class Job(models.Model):
    ghj_id = models.CharField(max_length=100, unique=True)
    data = JSONField()

    def __str__(self):
        return self.ghj_id


class UnreviewedJobs(models.Model):
    title = models.CharField(max_length=100, default='Unreviewed Jobs')
    jobs = models.ManyToManyField(Job)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        # get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class SavedJobs(models.Model):
    title = models.CharField(max_length=100, default='Saved Jobs')
    jobs = models.ManyToManyField(Job)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        # get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
