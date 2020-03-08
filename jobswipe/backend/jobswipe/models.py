from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.contrib.auth import get_user_model


class Job(models.Model):
    ghj_id = models.CharField(max_length=100, unique=True)
    data = JSONField()

    def __str__(self):
        return self.ghj_id


class JobList(models.Model):
    title = models.CharField(max_length=100)
    jobs = models.ManyToManyField(Job)
    jobseeker = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )


def __str__(self):
    return self.title
