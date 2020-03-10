from rest_framework import serializers
from .models import User, Job, Saved, Unreviewed


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'saved_jobs', 'unreviewed_jobs')


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'ghj_id',
            'title',
            'company',
            'data',
        )
        model = Job


class SavedSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'jobs',
            'owner'
        )
        model = Saved


class UnreviewedSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'jobs',
            'owner'
        )
        model = Unreviewed
