from rest_framework import serializers
from .models import Job
# from .models import Job, JobList, JobSeeker


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'ghj_id',
            'data',
        )
        model = Job


# class JobListSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = (
#             'id',
#             'title',
#             'jobs',
#             'jobseeker',
#         )
#         model = JobList


# class JobSeekerSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = (
#             'id',
#             'username',
#             'email',
#         )
#         model = JobSeeker
