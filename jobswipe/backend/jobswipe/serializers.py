from rest_framework import serializers
from .models import Job, JobList


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'ghj_id',
            'data',
        )
        model = Job


class JobListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'jobs',
            'jobseeker',
        )
        model = JobList
