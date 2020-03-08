from django.contrib.postgres.fields import JSONField
from django.db import models


class Job(models.Model):
    ghj_id = models.CharField(max_length=100, unique=True)
    data = JSONField()

    def __str__(self):
        return self.ghj_id


# class JobSeeker(models.Model):
#     username = models.CharField(max_length=100)
#     email = models.CharField(unique=True,
#                              max_length=500)

#     def __str__(self):
#         return self.username


# class JobList(models.Model):
#     title = models.CharField(max_length=100)
#     jobs = models.ManyToManyField(Job)
#     jobseeker = models.ForeignKey(
#         CustomUser, on_delete=models.CASCADE, default=1)

#     def __str__(self):
#         return self.title
