from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from apps.home.models import Classes

DEFAULT_MESSAGE = """Class - {0}\nSubject - {1}\nDay - {2}\nLink - [here]({3})"""


class ClassTime(models.Model):
    key_class = models.ForeignKey(Classes, on_delete=models.CASCADE)
    subject = models.TextField(max_length=50)
    permanent = models.BooleanField(default=True)

    class Day(models.IntegerChoices):
        Monday = 0
        Tuesday = 1
        Wednesday = 2
        Thursday = 3
        Friday = 4
        Saturday = 5
        Sunday = 6

    day = models.IntegerField(choices=Day.choices)
    time = models.TimeField(auto_now=False)
    link = models.TextField(max_length=400)


# class PostAnnouncementDiscord(models.Model):
#     link = models.TextField(max_length=400)
#     key_class = models.ForeignKey(Classes, on_delete=models.CASCADE, related_name='announcements')
#     message = models.TextField(max_length=120, default=DEFAULT_MESSAGE)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
