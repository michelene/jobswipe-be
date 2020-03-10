from rest_framework import generics, response
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
# from django.forms.models import model_to_dict
import requests
import json
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import User, Job, Saved, Unreviewed
from .serializers import UserSerializer, JobSerializer, SavedSerializer, UnreviewedSerializer

# Create your views here.


class ListUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListJob(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class DetailJob(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class ListSaved(generics.ListCreateAPIView):
    queryset = Saved.objects.all()
    serializer_class = SavedSerializer


class DetailSaved(generics.RetrieveUpdateDestroyAPIView):
    queryset = Saved.objects.all()
    serializer_class = SavedSerializer


class ListUnreviewed(generics.ListCreateAPIView):
    queryset = Unreviewed.objects.all()
    serializer_class = UnreviewedSerializer


class DetailUnreviewed(generics.RetrieveUpdateDestroyAPIView):
    queryset = Unreviewed.objects.all()
    serializer_class = UnreviewedSerializer


# Pulling data from GHJ:
# URL = https://jobs.github.com/positions.json?description=python&location=new+york&page=1
# r = requests.get()
# r.text <- will dump the JSON object, '[{}, {}, ...]'
#
# get_gh_jobs is a function-based view, so we need the @api_view decorator:
# By default, the @api_view decorator will catch any error
#  and return a 400 Bad Request response
#
# This view will behave the same for GET and POST
# That is because we are GETting from GHJ API, and POSTint to postgres
#
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def get_gh_jobs(request, search_terms=''):
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
    params = search_terms
    print(params)
    current_user = request.user
    # print(current_user.id)
    base_url = 'https://jobs.github.com/positions.json?page=0'
    # search_url = 'https://jobs.github.com/positions.json?description=react&page=1'
    search_url = base_url + search_terms
    res = requests.get(search_url)
    # If this user does not yet have a Saved list, create one:
    for job in json.load(res.text):
        ghj_id = job['id']
        # ghj_title = job['title']
        print('Saving ', ghj_id)
        print('User is ', current_user.id, current_user.username)
        # job_instance = Job.objects.create(ghj_id=ghj_id, data=job)

    # print(res.text)
    # res.text is '[{"id": "abcd", "key": "etc..."}, ...]'
    # Now here we need to validate the res.text and then store it to the DB:
    # job_instance = Job.objects.create(ghj_id="this is a test", data=res.text)

    return JsonResponse(res.text, safe=False)
