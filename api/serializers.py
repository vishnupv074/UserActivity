from rest_framework import serializers
from .models import Users, Activities


# Serializer for the activity objects
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = ['start_time', 'end_time']


# Serializer for user objects
class UserSerializer(serializers.ModelSerializer):
    activity_periods =serializers.SerializerMethodField('get_activity')

    # Function for returning the corresponding activity of a user with this serializer
    def get_activity(self, dat):
        activities = Activities.objects.filter(user=dat)
        ser = ActivitySerializer(activities, many=True)
        return ser.data

    class Meta:
        model = Users
        fields = ['id', 'real_name', 'tz', 'activity_periods']
