from rest_framework import generics, response
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
# from django.forms.models import model_to_dict
import requests
from rest_framework.views import APIView
from rest_framework.response import Response


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

# Pulling data from GHJ:
# URL = https://jobs.github.com/positions.json?description=python&location=new+york&page=1
# r = requests.get()
# r.text <- will dump the JSON object, '[{}, {}, ...]'

# !!! This get_gh_jobs works !!!
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def get_gh_jobs(request):
#     if request.method == 'POST':
#         return JsonResponse({"message": "Got some data!", "data": request.data})
#     return JsonResponse({"message": "Hello, world!"})


# !!! The GET below works !!!
# get_gh_jobs is a function-based view, so we need the @api_views decorator:
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def get_gh_jobs(request, pk=1, search_terms=''):
    # jobs_url = 'https://jobs.github.com/positions.json?&description=toptal'
    #   For GET /positions.json:
    #     &page=(0, ...)
    #     &description=
    #     &location=
    #     &lat=
    #     &long=
    #     &full_time=
    # For GET /positions/ID.json:
    #     &markdown=(true|false) <- otherwise returns HTML markup
    base_url = 'https://jobs.github.com/positions.json?page=0'
    # search_url = 'https://jobs.github.com/positions.json?description=react&page=1'
    search_url = base_url + search_terms
    res = requests.get(search_url)
    # print(res.text)
    # res.text is '[{"id": "abcd", "key": "etc..."}, ...]'
    return JsonResponse(res.text, safe=False)
