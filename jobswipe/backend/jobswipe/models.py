from django.contrib.postgres.fields import JSONField
from django.db import models


# Create your models here.


class Job(models.Model):
    ghj_id = models.CharField(max_length=100)
    data = JSONField()

    def __str__(self):
        return self.ghj_id


class JobSeeker(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=500)

    def __str__(self):
        return self.username


class JobList(models.Model):
    title = models.CharField(max_length=100)
    jobs = models.ManyToManyField(Job)
    jobseeker = models.ForeignKey(
        JobSeeker, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
