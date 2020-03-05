from django.db import models

# Create your models here.


class Keyword(models.Model):
    keyword = models.CharField(max_length=100)

    def __str__(self):
        return self.keyword


class Job(models.Model):
    ghj_id = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    created_at = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    company_url = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    how_to_apply = models.CharField(max_length=100)
    companyLogo = models.CharField(max_length=100)
    keywords = models.ManyToManyField(Keyword, related_name='jobs')

    def __str__(self):
        return self.title


class JobList(models.Model):
    title = models.CharField(max_length=100)
    jobs = models.ManyToManyField(Job, related_name='joblists')

    def __str__(self):
        return self.title


class JobSeeker(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=500)
    saved_jobs = models.ForeignKey(
        JobList, on_delete=models.CASCADE, related_name='job_seekers')

    def __str__(self):
        return self.username
