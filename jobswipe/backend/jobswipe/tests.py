from django.test import TestCase
from .models import User, Job, UnreviewedJobs, SavedJobs

# Create your tests here.


class JobSwipeTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Job.objects.create(ghj_id="12345")
        Job.objects.create(data="[{"title": "something", "description": "something else"}]")

    def test_ghj_id_content(self):
        job = Job.objects.get(id=1)
        expected_object_name = f'{job.ghj_id}'
        self.assertEquals(expected_object_name, "12345")

    def test_data_content(self):
        job = Job.objects.get(id=1)
        expected_object_name = f'{job.data}'
        self.assertEquals(expected_object_name, "[{"title": "something", "description": "something else"}]")
