from django.test import TestCase
from .models import Job, JobList, JobSeeker

# Create your tests here.


class JobSwipeTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        JobSeeker.objects.create(username="JohnDoe")
        JobSeeker.objects.create(email="jdoe@mail.com")

    def test_username_content(self):
        jobseeker = JobSeeker.objects.get(id=1)
        expected_object_name = f'{jobseeker.username}'
        self.assertEquals(expected_object_name, "JohnDoe")

    def test_email_content(self):
        email = JobSeeker.objects.get(id=1)
        expected_object_name = f'{jobseeker.email}'
        self.assertEquals(expected_object_name, "jdoe@email.com")
