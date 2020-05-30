import json
from datetime import datetime
from api.models import Users, Activities


def run():
    file = open('scripts/test.json')  # Fetching the json file
    data = json.load(file)
    for i in data['members']:
        user = Users()  # Creating an user object
        user.id = i['id']
        user.email = i['email']
        user.tz = i['tz']
        user.real_name = i['real_name']
        user.save()

        for j in i['activity_periods']:
            activity = Activities()
            datetime_object = datetime.strptime(j['start_time'], '%b %d %Y %I:%M%p')  # converting given datetime format
            activity.start_time = datetime_object
            datetime_object2 = datetime.strptime(j['end_time'], '%b %d %Y %I:%M%p')
            activity.end_time = datetime_object2
            activity.user = user
            activity.save()
