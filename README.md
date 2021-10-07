# EduOrange
A simple school portal website for students and teachers


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
Python 3.6+ (The project was built with python 3.9.5 but 3.6+ should work fine)
