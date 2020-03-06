from rest_framework import serializers
from .models import Job, JobList, JobSeeker


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'ghj_id',
            'type',
            'url',
            'created_at',
            'company',
            'company_url',
            'location',
            'title',
            'description',
            'how_to_apply',
            'companyLogo',
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


class JobSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'username',
            'email',
        )
        model = JobSeeker
