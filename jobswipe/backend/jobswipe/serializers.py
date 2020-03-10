from rest_framework import serializers
from .models import User, Job, NewJobList


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', )


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'ghj_id',
            'data',
        )
        model = Job


class NewJobListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'jobs',
            'owner',
        )
        model = NewJobList
