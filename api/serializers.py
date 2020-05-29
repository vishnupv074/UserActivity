from rest_framework import serializers
from .models import Users, Activities


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = ['start_time', 'end_time']


class UserSerializer(serializers.ModelSerializer):
    activities =serializers.SerializerMethodField('get_activity')

    def get_activity(self, dat):
        activities = Activities.objects.filter(user=dat)
        ser = ActivitySerializer(activities, many=True)
        return ser.data

    class Meta:
        model = Users
        fields = ['id', 'real_name', 'tz', 'activities']
