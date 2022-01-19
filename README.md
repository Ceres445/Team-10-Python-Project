# EduOrange
Your classroom made online

A simple school portal website for students and teachers

# Project Structure
```
SchoolApp
├── SchoolApp
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps
│   ├── __init__.py
│   ├── classes
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── migrations
│   │   │   ├── 0001_squashed_0009_delete_classtime.py
│   │   │   ├── 0002_alter_upload_created_at.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── home
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── map.py
│   │   ├── migrations
│   │   │   ├── 0001_squashed_0003_profile_avatar.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── templatetags
│   │   │   ├── __init__.py
│   │   │   └── tags.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── public_api
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── filters.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── timetable
│       ├── __init__.py
│       ├── admin.py
│       ├── announcer.py
│       ├── apps.py
│       ├── forms.py
│       ├── migrations
│       │   ├── 0001_initial.py
│       │   └── __init__.py
│       ├── models.py
│       ├── tests.py
│       ├── urls.py
│       ├── utils.py
│       └── views.py
├── manage.py
├── static
│   ├── home
│   │   ├── css
│   │   │   ├── base.css
│   │   │   ├── forms.css
│   │   │   ├── index.css
│   │   │   └── posts.css
│   │   └── js
│   │       ├── classes_view.js
│   │       ├── modules
│   │       │   ├── constants.js
│   │       │   └── functions.js
│   │       ├── post_view_detail.js
│   │       ├── posts.js
│   │       └── view_user_posts.js
│   ├── svg
│   │   ├── logo.png
│   │   └── logo.svg
│   └── timetable
│       ├── css
│       │   └── timetable.css
│       └── js
│           └── timetable.js
└── templates
    ├── base.html
    ├── classes
    │   ├── assignment_create.html
    │   ├── assignment_submit.html
    │   ├── classes_detail.html
    │   ├── classes_view.html
    │   ├── invite_users.html
    │   ├── view_submissions.html
    │   └── wrong_email.html
    ├── emails
    │   ├── email_invite_message.html
    │   └── email_invite_subject.txt
    ├── home
    │   ├── avatar_change.html
    │   ├── edit_profile.html
    │   ├── index.html
    │   ├── posts.html
    │   ├── posts_detail.html
    │   ├── profile.html
    │   ├── robots.txt
    │   └── view_user_posts.html
    ├── registration
    │   ├── login.html
    │   ├── password_change_done.html
    │   ├── password_change_form.html
    │   ├── password_reset_done.html
    │   ├── password_reset_form.html
    │   ├── register.html
    │   └── registration_base.html
    └── timetable
        ├── create.html
        └── view_timetable.html
```
# Running a local instance

1. Clone the repository
2. Set up venv
    `python3 -m venv venv`
3. Activate the venv 
     `source venv/bin/activate`
4. Install dependencies
    `python3 -m pip install -r requirements.txt`
5. Setup local server
    `cd SchoolApp`
    `python manage.py migrate`
    `python manage.py createsuperuser`
6. Setup config
Create a `.env` file to load environment variables.

```
HOST='local'
EMAIL_HOST_USER='google_smtp_email'
EMAIL_HOST_PASSWORD='google_smtp_password'
DROPBOX_ACCESS_TOKEN='dropbox_token'
```
`EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD`  are only required if you are going to reset password, 
`DROPBOX_ACCESS_TOKEN` is required for any file operations,
the website works without those options. 

7. Run the local server
    `python manage.py runserver`


# Requirements
Python 3.8+ (The project was built with python 3.9.5 but 3.8+ should work fine)
