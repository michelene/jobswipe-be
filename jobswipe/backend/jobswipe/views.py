from rest_framework import generics

from .models import Job, JobList, JobSeeker
from .serializers import JobSerializer, JobListSerializer, JobSeekerSerializer

# Create your views here.


class ListJobs(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class DetailJob(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class ListJobLists(generics.ListCreateAPIView):
    queryset = JobList.objects.all()
    serializer_class = JobListSerializer


class DetailJobList(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobList.objects.all()
    serializer_class = JobListSerializer


class ListJobSeekers(generics.ListCreateAPIView):
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerSerializer


class DetailJobSeeker(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerSerializer
