# UserActivity
This is an API based web app for returning users of this app and their activity
periods.

## Installation
To install this in local server after downloading and extracting the respo.
1. Create a python 3.7 virtualenv and activate
2. Then run
    ```commandline
   cd UserActivity
   pip install -r requirements.txt 
   ```
3. Create mysql database and configure in setings.py
    ```json
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'actions_db',
            'HOST':'localhost',
            'USER':'root',
            'PASSWORD':''
        }
    }
    ```
4. Make migrations and migrate
    ```commandline
   python manage.py makemigrations
   python manage.py migrate
    ```
5. Insert dummy data.
    ```commandline
   python manage.py runscripts script
    ```
   Dummy data is stores in `test.json` file which is store inside the diresctory `scripts`.
   When this command runs the file `scripts/script.py` executed and dummy data will be stored in db.
   
6. Running the local server
    ```commandline
   python manage.py runserver
    ```
   
7. Calling the API

    Calling the api will return all the Users and their corresponding activity periods.
    ```html
   http://127.0.0.1:8000/api/
    ```
    this will return json like below.
    ```json
   {
    "ok": true,
    "members": [
        {
            "id": "W012A3CDE",
            "real_name": "Egon Spengler",
            "tz": "America/Los_Angeles",
            "activities": [
                    {
                        "start_time": "2020-02-01T13:33:00Z",
                        "end_time": "2020-02-01T13:54:00Z"
                    },
                    {
                        "start_time": "2020-03-01T11:11:00Z",
                        "end_time": "2020-03-01T14:00:00Z"
                    },
                    {
                        "start_time": "2020-03-16T17:33:00Z",
                        "end_time": "2020-03-16T20:02:00Z"
                    }
                ]
            }
        ]
    }
    ```
   
   Call the api followed by object id will return specific object
   
   ```html
   http://127.0.0.1:8000/api/W012A3CDE
    ```
   Returns NotFound error when the object with given id is not in db.
