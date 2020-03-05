from django.test import TestCase
from .models import Job, JobList, JobSeeker

# Create your tests here.


class JobSwipeTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Job.objects.create(title="Software Engineer, ReactJS")
        Job.objects.create(description="Build React apps")

    def test_title_content(self):
        todo = Todo.objects.get(id=8)
        expected_object_name = f'{job.title}'
        self.assertEquals(expected_object_name, "Software Engineer, ReactJS")

    def test_description_content(self):
        todo = Todo.objects.get(id=9)
        expected_object_name = f'{job.description}'
        self.assertEquals(expected_object_name, "Build React apps")
